import { useRef } from 'react'
import { documentDownloadUrl } from '../../api/documents'
import type { RowStatus } from '../../hooks/useJourneyDocuments'

const ROW_STATUS_CONFIG: Record<RowStatus, { label: string; pill: string; filter: string }> = {
  missing: { label: 'Missing', pill: 'not_started', filter: 'missing' },
  uploaded: { label: 'Uploaded', pill: 'in_progress', filter: 'uploaded' },
  verifying: { label: 'In Review', pill: 'needs_verification', filter: 'verifying' },
  verified: { label: 'Verified', pill: 'completed', filter: 'verified' },
  rejected: { label: 'Rejected', pill: 'blocked', filter: 'rejected' },
}

interface DocumentRowProps {
  requirement: string
  stepTitle: string
  phaseName: string
  rowStatus: RowStatus
  filename: string | null
  documentId: number | null
  uploadedAt: string | null
  uploading: boolean
  busy: boolean
  onUpload: (file: File) => void
  onVerify: () => void
  onReject: () => void
  onDelete: () => void
}

function formatDate(iso: string | null): string {
  if (!iso) return '—'
  return new Date(iso).toLocaleDateString(undefined, { day: 'numeric', month: 'short', year: 'numeric' })
}

export default function DocumentRow({
  requirement,
  stepTitle,
  phaseName,
  rowStatus,
  filename,
  documentId,
  uploadedAt,
  uploading,
  busy,
  onUpload,
  onVerify,
  onReject,
  onDelete,
}: DocumentRowProps) {
  const inputRef = useRef<HTMLInputElement>(null)

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) onUpload(file)
    e.target.value = ''
  }

  const config = ROW_STATUS_CONFIG[rowStatus]

  return (
    <tr>
      <td style={{ fontWeight: 600 }}>
        {requirement}
        <div className="text-sm text-muted" style={{ fontWeight: 400, marginTop: 2 }}>
          {phaseName} · Step {stepTitle}
        </div>
      </td>
      <td>
        <span className={`status-pill ${config.pill}`}>{config.label}</span>
      </td>
      <td className="text-muted text-sm">
        {filename ?? '—'}
        {filename && uploadedAt ? (
          <div className="text-sm text-muted">{formatDate(uploadedAt)}</div>
        ) : null}
      </td>
      <td>
        <div style={{ display: 'flex', gap: 6, justifyContent: 'flex-end' }}>
          <input
            ref={inputRef}
            type="file"
            style={{ display: 'none' }}
            onChange={handleFileChange}
          />
          <button
            className="btn btn-sm"
            disabled={uploading || busy}
            onClick={() => inputRef.current?.click()}
          >
            {uploading ? 'Uploading…' : filename ? 'Replace' : 'Upload'}
          </button>
          {documentId != null && (
            <>
              <a className="btn btn-sm btn-secondary" href={documentDownloadUrl(documentId)}>
                Download
              </a>
              <button
                className="btn btn-sm btn-secondary"
                disabled={busy}
                onClick={onVerify}
                title="Mark as verified"
              >
                Verify
              </button>
              <button
                className="btn btn-sm btn-secondary"
                disabled={busy}
                onClick={onReject}
                title="Mark as rejected"
              >
                Reject
              </button>
              <button className="btn btn-sm btn-ghost" disabled={busy} onClick={onDelete} title="Delete">
                Delete
              </button>
            </>
          )}
        </div>
      </td>
    </tr>
  )
}