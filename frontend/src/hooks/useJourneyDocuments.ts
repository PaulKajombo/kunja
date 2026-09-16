import { useCallback, useEffect, useMemo, useState } from 'react'
import {
  listDocuments,
  uploadDocument,
  updateDocumentStatus,
  deleteDocument,
} from '../api/documents'
import { listJourneys } from '../api/journeys'
import type { Document, DocumentStatus, Journey } from '../api/types'

export interface RequiredDoc {
  stepId: number
  stepTitle: string
  phaseName: string
  requirement: string
}

export interface DocumentRow {
  rowKey: string
  requirement: string
  stepId: number
  stepTitle: string
  phaseName: string
  document: Document | null
  rowStatus: RowStatus
}

export type RowStatus = 'missing' | 'uploaded' | 'verifying' | 'verified' | 'rejected'

const STATUS_TO_ROW: Record<DocumentStatus, RowStatus> = {
  MISSING: 'missing',
  UPLOADED: 'uploaded',
  IN_REVIEW: 'verifying',
  VERIFIED: 'verified',
  REJECTED: 'rejected',
}

export function useJourneyDocuments() {
  const [journeys, setJourneys] = useState<Journey[]>([])
  const [activeJourneyId, setActiveJourneyId] = useState<number | null>(null)
  const [documents, setDocuments] = useState<Document[]>([])
  const [loading, setLoading] = useState(true)
  const [uploadingKey, setUploadingKey] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  const activeJourney = useMemo(
    () => journeys.find((j) => j.id === activeJourneyId) ?? null,
    [journeys, activeJourneyId],
  )

  const loadJourneys = useCallback(async () => {
    try {
      const data = await listJourneys()
      setJourneys(data.journeys)
      setActiveJourneyId((current) => current ?? data.journeys[0]?.id ?? null)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Failed to load journeys')
    } finally {
      setLoading(false)
    }
  }, [])

  const loadDocuments = useCallback(async (journeyId: number) => {
    try {
      const data = await listDocuments(journeyId)
      setDocuments(data.documents)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Failed to load documents')
    }
  }, [])

  useEffect(() => {
    void loadJourneys()
  }, [loadJourneys])

  useEffect(() => {
    if (activeJourneyId != null) void loadDocuments(activeJourneyId)
  }, [activeJourneyId, loadDocuments])

  const requiredDocs: RequiredDoc[] = useMemo(() => {
    if (!activeJourney) return []
    const rows: RequiredDoc[] = []
    for (const phase of activeJourney.phases) {
      for (const step of phase.steps) {
        for (const requirement of step.documents_needed ?? []) {
          rows.push({
            stepId: step.id,
            stepTitle: step.title,
            phaseName: phase.name,
            requirement,
          })
        }
      }
    }
    return rows
  }, [activeJourney])

  const rows: DocumentRow[] = useMemo(() => {
    const byStepRequirement = new Map<string, Document>()
    for (const doc of documents) {
      byStepRequirement.set(`${doc.step_id}:${doc.requirement}`, doc)
    }
    return requiredDocs.map((r) => {
      const doc = byStepRequirement.get(`${r.stepId}:${r.requirement}`) ?? null
      return {
        ...r,
        rowKey: `${r.stepId}:${r.requirement}`,
        document: doc,
        rowStatus: doc ? STATUS_TO_ROW[doc.status] : 'missing',
      }
    })
  }, [requiredDocs, documents])

  const upload = useCallback(
    async (row: RequiredDoc, file: File) => {
      if (!activeJourneyId) return null
      setUploadingKey(`${row.stepId}:${row.requirement}`)
      setError(null)
      try {
        await uploadDocument({
          file,
          journeyId: activeJourneyId,
          stepId: row.stepId,
          requirement: row.requirement,
        })
        await loadDocuments(activeJourneyId)
        return true
      } catch (e) {
        setError(e instanceof Error ? e.message : 'Upload failed')
        return false
      } finally {
        setUploadingKey(null)
      }
    },
    [activeJourneyId, loadDocuments],
  )

  const updateStatus = useCallback(
    async (document: Document, status: DocumentStatus) => {
      if (!activeJourneyId) return
      try {
        await updateDocumentStatus({ documentId: document.id, status })
        await loadDocuments(activeJourneyId)
      } catch (e) {
        setError(e instanceof Error ? e.message : 'Failed to update status')
      }
    },
    [activeJourneyId, loadDocuments],
  )

  const removeDocument = useCallback(
    async (document: Document) => {
      if (!activeJourneyId) return
      try {
        await deleteDocument(document.id)
        await loadDocuments(activeJourneyId)
      } catch (e) {
        setError(e instanceof Error ? e.message : 'Failed to delete document')
      }
    },
    [activeJourneyId, loadDocuments],
  )

  return {
    journeys,
    activeJourneyId,
    setActiveJourneyId,
    activeJourney,
    rows,
    loading,
    uploadingKey,
    error,
    setError,
    upload,
    updateStatus,
    removeDocument,
  }
}