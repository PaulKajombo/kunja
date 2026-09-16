import { useMemo, useState } from 'react'
import DocumentRow from '../components/documents/DocumentRow'
import { useJourneyDocuments } from '../hooks/useJourneyDocuments'
import type { RowStatus } from '../hooks/useJourneyDocuments'
import type { DocumentStatus } from '../api/types'

const FILTERS: { key: RowStatus | 'all'; label: string }[] = [
  { key: 'all', label: 'All' },
  { key: 'missing', label: 'Missing' },
  { key: 'uploaded', label: 'Uploaded' },
  { key: 'verifying', label: 'Needs Review' },
  { key: 'verified', label: 'Verified' },
  { key: 'rejected', label: 'Rejected' },
]

export default function Documents() {
  const {
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
  } = useJourneyDocuments()

  const [filter, setFilter] = useState<RowStatus | 'all'>('all')
  const [busyKey, setBusyKey] = useState<string | null>(null)

  const counts = useMemo(() => {
    const c: Record<string, number> = { all: rows.length }
    for (const r of rows) c[r.rowStatus] = (c[r.rowStatus] ?? 0) + 1
    return c
  }, [rows])

  const visibleRows = filter === 'all' ? rows : rows.filter((r) => r.rowStatus === filter)

  return (
    <div>
      <div className="flex-between mb-3" style={{ flexWrap: 'wrap', gap: 12 }}>
        <div>
          <h1 style={{ fontSize: '1.4rem', fontWeight: 700, marginBottom: '4px' }}>Documents</h1>
          <p className="text-sm text-muted">Track and manage your compliance documents</p>
        </div>
        <div className="flex-between" style={{ gap: 10 }}>
          {journeys.length > 1 && (
            <label className="text-sm text-muted" style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
              Journey
              <select
                className="form-input"
                style={{ padding: '7px 10px', borderRadius: 8, border: '1px solid var(--border, #e5e7eb)' }}
                value={activeJourneyId ?? ''}
                onChange={(e) => setActiveJourneyId(Number(e.target.value))}
              >
                {journeys.map((j) => (
                  <option key={j.id} value={j.id}>
                    {j.company_name} · {j.target_country} (#{j.id})
                  </option>
                ))}
              </select>
            </label>
          )}
          <div className="text-sm text-muted" style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            {counts.missing ?? 0} of {counts.all ?? 0} docs still missing
          </div>
        </div>
      </div>

      {error && (
        <div className="notice-error mb-3" style={{ padding: '10px 14px', borderRadius: 8, background: 'var(--danger-bg, #fee2e2)', color: 'var(--danger, #dc2626)' }}>
          {error}
          <button className="btn btn-sm btn-ghost" style={{ marginLeft: 10 }} onClick={() => setError(null)}>
            Dismiss
          </button>
        </div>
      )}

      {/* Filters */}
      <div className="doc-filters">
        {FILTERS.map((f) => (
          <button
            key={f.key}
            className={`doc-filter-btn ${filter === f.key ? 'active' : ''}`}
            onClick={() => setFilter(f.key)}
          >
            {f.label} ({counts[f.key as string] ?? 0})
          </button>
        ))}
      </div>

      {/* Document table */}
      <div className="card" style={{ padding: 0, overflow: 'hidden' }}>
        {loading ? (
          <div className="empty-state">
            <div className="spinner" />
            <p className="text-sm text-muted">Loading documents…</p>
          </div>
        ) : visibleRows.length === 0 ? (
          <div className="empty-state">
            <h3>No documents found</h3>
            {rows.length === 0 ? (
              <p className="text-sm text-muted">
                {activeJourney
                  ? 'No required documents were generated for this journey yet.'
                  : 'Create a journey to generate your compliance document list.'}
              </p>
            ) : (
              <p className="text-sm text-muted">No documents match this filter.</p>
            )}
          </div>
        ) : (
          <table className="doc-table">
            <thead>
              <tr>
                <th>Required document</th>
                <th>Status</th>
                <th>Uploaded file</th>
                <th style={{ textAlign: 'right' }}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {visibleRows.map((row) => (
                <DocumentRow
                  key={row.rowKey}
                  requirement={row.requirement}
                  stepTitle={row.stepTitle}
                  phaseName={row.phaseName}
                  rowStatus={row.rowStatus}
                  filename={row.document?.filename ?? null}
                  documentId={row.document?.id ?? null}
                  uploadedAt={row.document?.created_at ?? null}
                  uploading={uploadingKey === row.rowKey}
                  busy={busyKey === row.rowKey}
                  onUpload={(f) => {
                    void upload(row, f)
                  }}
                  onVerify={() => {
                    if (!row.document) return
                    setBusyKey(row.rowKey)
                    setError(null)
                    void updateStatus(row.document, 'VERIFIED' as DocumentStatus).finally(() => setBusyKey(null))
                  }}
                  onReject={() => {
                    if (!row.document) return
                    setBusyKey(row.rowKey)
                    setError(null)
                    void updateStatus(row.document, 'REJECTED' as DocumentStatus).finally(() => setBusyKey(null))
                  }}
                  onDelete={() => {
                    if (!row.document) return
                    setBusyKey(row.rowKey)
                    setError(null)
                    void removeDocument(row.document).finally(() => setBusyKey(null))
                  }}
                />
              ))}
            </tbody>
          </table>
        )}
      </div>

      <p className="text-sm text-muted" style={{ marginTop: 12 }}>
        Uploaded documents are stored securely and used by Kunja's compliance engine to track which
        requirements you have fulfilled for {activeJourney?.target_country ?? 'your target market'}.
      </p>
    </div>
  )
}