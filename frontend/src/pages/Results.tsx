import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { api, SubmitResult } from '../lib/api'

function Results() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [result, setResult] = useState<SubmitResult | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [showGaps, setShowGaps] = useState(false)

  useEffect(() => {
    // Fetch stored results from the backend (no re-submission)
    api<SubmitResult>(`/api/v1/checklists/${id}/results`)
      .then(setResult)
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }, [id])

  if (loading) return <div className="card">Loading results...</div>
  if (error) return <div className="card error-box">{error}</div>
  if (!result) return null

  const scoreColor =
    result.compliance_level === 'high' ? '#1a6b3c' :
    result.compliance_level === 'medium' ? '#b8860b' : '#e63946'

  return (
    <div>
      <a href="/" style={{ color: 'var(--primary)', textDecoration: 'none' }}>← Back home</a>
      <header>
        <h1>Your Compliance Score</h1>
      </header>

      <div className="card" style={{ textAlign: 'center' }}>
        <div style={{ fontSize: '4rem', fontWeight: 700, color: scoreColor }}>
          {result.compliance_score}%
        </div>
        <p style={{ fontSize: '1.2rem', marginTop: '10px' }}>
          {result.compliance_level === 'high' && '🟢 Good standing - minor gaps to close'}
          {result.compliance_level === 'medium' && '🟡 Moderate risk - several gaps to address'}
          {result.compliance_level === 'low' && '🔴 High risk - critical gaps need attention'}
        </p>
        <p style={{ color: '#666' }}>
          {result.critical_gaps_count} critical gap(s) found
        </p>
      </div>

      <div className="card">
        <h2>Category Breakdown</h2>
        {Object.values(result.category_scores).map((cat: any) => (
          <div key={cat.name} style={{ marginBottom: '15px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <strong>{cat.name}</strong>
              <span>{cat.score}% ({cat.passed}/{cat.total})</span>
            </div>
            <div className="progress-bar">
              <div
                className="progress-fill"
                style={{ width: `${cat.score}%`, background: cat.score >= 80 ? '#1a6b3c' : cat.score >= 50 ? '#b8860b' : '#e63946' }}
              />
            </div>
            <small style={{ color: '#666' }}>{cat.regulation}</small>
          </div>
        ))}
      </div>

      <div className="card">
        <h2>Gap Analysis</h2>
        <button className="btn" onClick={() => setShowGaps((s) => !s)}>
          {showGaps ? 'Hide gaps' : `Show gaps (${result.gaps.length})`}
        </button>

        {showGaps && (
          <div style={{ marginTop: '15px' }}>
            {result.gaps.length === 0 && <p>✅ No gaps found!</p>}
            {result.gaps.map((gap) => (
              <div
                key={gap.question_id}
                style={{
                  padding: '12px',
                  margin: '8px 0',
                  background: gap.critical ? '#fff5f5' : '#f8f8f8',
                  borderLeft: `4px solid ${gap.critical ? 'var(--secondary)' : '#ccc'}`,
                  borderRadius: '4px',
                }}
              >
                <p><strong>{gap.question}</strong></p>
                <p style={{ fontSize: '0.9rem', color: '#555' }}>{gap.requirement}</p>
                {gap.resource && (
                  <p style={{ fontSize: '0.85rem' }}>
                    <a href={gap.resource} target="_blank" rel="noreferrer" style={{ color: 'var(--primary)' }}>
                      Official resource →
                    </a>
                  </p>
                )}
              </div>
            ))}
          </div>
        )}
      </div>

      <div style={{ display: 'flex', gap: '10px' }}>
        <button className="btn" onClick={() => navigate('/checklists/new')}>
          Start Another Checklist
        </button>
        <button className="btn-secondary" onClick={() => navigate('/')}>
          Back to Home
        </button>
      </div>
    </div>
  )
}

export default Results