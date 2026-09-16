import { api, apiVoid } from './client'
import type {
  Document,
  DocumentDelete,
  DocumentList,
  DocumentStatus,
} from './types'

export async function listDocuments(journeyId?: number): Promise<DocumentList> {
  const query = journeyId != null ? `?journey_id=${journeyId}` : ''
  return api<DocumentList>(`/api/v1/documents${query}`)
}

export async function getDocument(id: number): Promise<Document> {
  return api<Document>(`/api/v1/documents/${id}`)
}

export interface UploadDocumentInput {
  file: File
  journeyId: number
  stepId?: number | null
  requirement?: string | null
}

export async function uploadDocument({
  file,
  journeyId,
  stepId = null,
  requirement = null,
}: UploadDocumentInput): Promise<Document> {
  const form = new FormData()
  form.append('journey_id', String(journeyId))
  if (stepId != null) form.append('step_id', String(stepId))
  if (requirement) form.append('requirement', requirement)
  form.append('file', file)

  const res = await fetch(`${import.meta.env.VITE_API_URL || ''}/api/v1/documents`, {
    method: 'POST',
    body: form,
  })
  if (!res.ok) {
    let message = `Upload failed (${res.status})`
    try {
      const data = await res.json()
      if (typeof data?.detail === 'string') message = data.detail
    } catch {
      /* keep default */
    }
    throw new Error(message)
  }
  return res.json() as Promise<Document>
}

export interface UpdateStatusInput {
  documentId: number
  status: DocumentStatus
}

export async function updateDocumentStatus({
  documentId,
  status,
}: UpdateStatusInput): Promise<Document> {
  return apiVoid<Document>(`/api/v1/documents/${documentId}/status`, {
    method: 'PATCH',
    body: { status },
  })
}

export async function deleteDocument(documentId: number): Promise<DocumentDelete> {
  return apiVoid<DocumentDelete>(`/api/v1/documents/${documentId}`, { method: 'DELETE' })
}

export function documentDownloadUrl(documentId: number): string {
  return `${import.meta.env.VITE_API_URL || ''}/api/v1/documents/${documentId}/download`
}