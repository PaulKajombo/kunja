import { useState } from 'react'


interface DocItem {
  id: string
  name: string
  requirement: string
  status: 'complete' | 'in_progress' | 'missing' | 'needs_review'
  date?: string
}

const MOCK_DOCS: DocItem[] = [
  { id: '1', name: 'Company Registration', requirement: 'Step: Register your company', status: 'complete', date: '2026-09-10' },
  { id: '2', name: 'Tax Registration (TPIN)', requirement: 'Step: Register for tax', status: 'complete', date: '2026-09-12' },
  { id: '3', name: 'Certificate of Origin', requirement: 'Step: Obtain certificate of origin', status: 'in_progress' },
  { id: '4', name: 'Commercial Invoice', requirement: 'Step: Prepare shipping documents', status: 'missing' },
  { id: '5', name: 'Packing List', requirement: 'Step: Prepare shipping documents', status: 'missing' },
  { id: '6', name: 'Product Certification', requirement: 'Step: Product standards compliance', status: 'needs_review' },
]

const FILTERS = ['all', 'complete', 'in_progress', 'missing', 'needs_review'] as const

const STATUS_MAP = {
  complete: { label: 'Complete', color: 'completed' },
  in_progress: { label: 'In Progress', color: 'in_progress' },
  missing: { label: 'Missing', color: 'not_started' },
  needs_review: { label: 'Needs Review', color: 'needs_verification' },
} as const

export default function Documents() {
  const [filter, setFilter] = useState<string>('all')

  const docs = filter === 'all' ? MOCK_DOCS : MOCK_DOCS.filter((d) => d.status === filter)

  const counts = {
    all: MOCK_DOCS.length,
    complete: MOCK_DOCS.filter((d) => d.status === 'complete').length,
    in_progress: MOCK_DOCS.filter((d) => d.status === 'in_progress').length,
    missing: MOCK_DOCS.filter((d) => d.status === 'missing').length,
    needs_review: MOCK_DOCS.filter((d) => d.status === 'needs_review').length,
  }

  return (
    <div>
      <div className="flex-between mb-3">
        <div>
          <h1 style={{ fontSize: '1.4rem', fontWeight: 700, marginBottom: '4px' }}>Documents</h1>
          <p className="text-sm text-muted">Track and manage your compliance documents</p>
        </div>
        <button className="btn" disabled>
          Upload document
        </button>
      </div>

      {/* Filters */}
      <div className="doc-filters">
        {FILTERS.map((f) => (
          <button
            key={f}
            className={`doc-filter-btn ${filter === f ? 'active' : ''}`}
            onClick={() => setFilter(f)}
          >
            {f === 'all' ? 'All' : f === 'in_progress' ? 'In Progress' : f === 'needs_review' ? 'Needs Review' : f.charAt(0).toUpperCase() + f.slice(1)}
            {' '}({counts[f]})
          </button>
        ))}
      </div>

      {/* Document table */}
      <div className="card" style={{ padding: 0, overflow: 'hidden' }}>
        {docs.length === 0 ? (
          <div className="empty-state">
            <h3>No documents found</h3>
            <p className="text-sm text-muted">No documents match this filter.</p>
          </div>
        ) : (
          <table className="doc-table">
            <thead>
              <tr>
                <th>Document</th>
                <th>Requirement</th>
                <th>Status</th>
                <th>Date</th>
              </tr>
            </thead>
            <tbody>
              {docs.map((doc) => (
                <tr key={doc.id}>
                  <td style={{ fontWeight: 600 }}>{doc.name}</td>
                  <td className="text-muted">{doc.requirement}</td>
                  <td>
                    <span className={`status-pill ${STATUS_MAP[doc.status].color}`}>
                      {STATUS_MAP[doc.status].label}
                    </span>
                  </td>
                  <td className="text-muted text-sm">
                    {doc.date || '—'}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  )
}
