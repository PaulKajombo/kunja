import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { api, Journey } from '../lib/api'

export default function Dashboard() {
  const navigate = useNavigate()
  const [journeys, setJourneys] = useState<Journey[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    api<{ journeys: Journey[]; total: number }>('/api/v1/journeys')
      .then((d) => setJourneys(d.journeys))
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }, [])

  const latest = journeys[0]
  const pct = latest?.progress.percentage ?? 0

  return (
    <div>
      <div className="flex-between mb-3">
        <div>
          <h1 style={{ fontSize: '1.4rem', fontWeight: 700, marginBottom: '4px' }}>Dashboard</h1>
          <p className="text-sm text-muted">Your market entry journeys</p>
        </div>
        <button className="btn" onClick={() => navigate('/journeys/new')}>
          + Start Journey
        </button>
      </div>

      {loading ? (
        <div className="card text-center">Loading...</div>
      ) : error ? (
        <div className="card empty-state">
          <h3>Couldn't load your journeys</h3>
          <p className="mt-1 mb-2 text-sm text-muted">{error}</p>
          <button className="btn" onClick={() => window.location.reload()}>
            Try again
          </button>
        </div>
      ) : journeys.length === 0 ? (
        <div className="card empty-state">
          <h3>No journeys yet</h3>
          <p className="mt-1 mb-2">Start your first market-entry journey and we'll map the complete path.</p>
          <button className="btn" onClick={() => navigate('/journeys/new')}>
            Start your first journey
          </button>
        </div>
      ) : (
        <>
          {/* Active journey hero card */}
          {latest && (
            <div className="card" style={{ cursor: 'pointer' }} onClick={() => navigate(`/journeys/${latest.id}`)}>
              <div className="flex-between mb-1">
                <span className="status-pill" style={{ fontSize: '0.7rem' }}>
                  Latest Journey
                </span>
                <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                  {latest.status.replace(/_/g, ' ')}
                </span>
              </div>

              <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '16px' }}>
                <span style={{ fontSize: '1.8rem' }}>
                  {latest.origin_country === 'malawi' ? '🇲🇼' : '🇿🇲'}
                </span>
                <span style={{ color: 'var(--text-muted)', fontSize: '1.2rem' }}>→</span>
                <span style={{ fontSize: '1.8rem' }}>
                  {latest.target_country === 'zambia' ? '🇿🇲' : '🇲🇼'}
                </span>
                <div style={{ marginLeft: '8px' }}>
                  <div style={{ fontWeight: 600, fontSize: '1rem' }}>{latest.company_name}</div>
                  <div className="text-sm text-muted">
                    {latest.industry.replace(/_/g, ' ').replace(/\b\w/g, (c: string) => c.toUpperCase())} · {latest.business_model_label}
                  </div>
                </div>
              </div>

              <div className="flex-between mb-1">
                <span style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                  Your Market Entry Progress
                </span>
                <span style={{ fontSize: '1.4rem', fontWeight: 700, color: 'var(--primary)' }}>
                  {pct}%
                </span>
              </div>
              <div className="progress-bar progress-bar-lg">
                <div
                  className="progress-fill"
                  style={{ width: `${pct}%`, background: pct >= 80 ? 'var(--completed)' : 'var(--primary)' }}
                />
              </div>
              <div className="flex-between mt-1">
                <span className="text-sm text-muted">
                  {latest.progress.completed_steps} completed ·{' '}
                  {latest.progress.in_progress_steps} in progress ·{' '}
                  {latest.progress.total_steps - latest.progress.completed_steps - latest.progress.in_progress_steps} pending
                </span>
              </div>
            </div>
          )}

          {/* Next Steps */}
          {latest && latest.progress.next_step_id && (
            <div className="card">
              <h2 style={{ marginBottom: '14px' }}>Your next steps</h2>
              <div className="next-steps-list">
                {latest.phases
                  .flatMap((phase) =>
                    phase.steps
                      .filter((s) => s.status === 'not_started' || s.status === 'in_progress')
                      .slice(0, 4)
                      .map((s) => ({ ...s, phaseName: phase.name }))
                  )
                  .map((step, i) => (
                    <button
                      key={step.id}
                      className="next-step-card"
                      onClick={() => navigate(`/journeys/${latest.id}`)}
                    >
                      <div className="next-step-num">{i + 1}</div>
                      <div className="next-step-info">
                        <strong>{step.title}</strong>
                        <span>{step.phaseName}</span>
                      </div>
                      <span className="next-step-arrow">→</span>
                    </button>
                  ))}
              </div>
            </div>
          )}

          {/* All journeys list */}
          {journeys.length > 1 && (
            <div className="card">
              <h2 style={{ marginBottom: '14px' }}>All Journeys</h2>
              {journeys.map((j) => (
                <button
                  key={j.id}
                  className="step-card"
                  onClick={() => navigate(`/journeys/${j.id}`)}
                >
                  <div className={`step-status ${j.status === 'completed' ? 'completed' : 'in_progress'}`}>
                    {j.status === 'completed' ? '✓' : j.progress.percentage + '%'}
                  </div>
                  <div className="step-card-body">
                    <div className="step-card-title">
                      {j.origin_country === 'malawi' ? '🇲🇼' : '🇿🇲'} →{' '}
                      {j.target_country === 'zambia' ? '🇿🇲' : '🇲🇼'} {j.company_name}
                    </div>
                    <div className="step-card-subtitle">
                      {j.industry.replace(/_/g, ' ').replace(/\b\w/g, (c: string) => c.toUpperCase())} · {j.business_model_label}
                    </div>
                  </div>
                  <span className="step-card-arrow">→</span>
                </button>
              ))}
            </div>
          )}
        </>
      )}
    </div>
  )
}
