import { useState, useEffect, useCallback } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { api, Journey, JourneyStep } from '../lib/api'

const STATUS_ICONS: Record<string, string> = {
  completed: '✓',
  in_progress: '●',
  needs_verification: '⚠',
  not_started: '✕',
  blocked: '🔒',
  skipped: '–',
}

const STATUS_LABELS: Record<string, string> = {
  completed: 'Complete',
  in_progress: 'In progress',
  needs_verification: 'Needs verification',
  not_started: 'Not started',
  blocked: 'Blocked by previous step',
  skipped: 'Skipped',
}

function JourneyView() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()

  const [journey, setJourney] = useState<Journey | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  // Step detail drawer
  const [activeStep, setActiveStep] = useState<JourneyStep | null>(null)
  const [updatingStep, setUpdatingStep] = useState(false)
  const [stepNotes, setStepNotes] = useState('')

  // Ask Kunja
  const [askQuestion, setAskQuestion] = useState('')
  const [askAnswer, setAskAnswer] = useState('')
  const [asking, setAsking] = useState(false)

  const loadJourney = useCallback(() => {
    api<Journey>(`/api/v1/journeys/${id}`)
      .then(setJourney)
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }, [id])

  useEffect(() => {
    loadJourney()
  }, [loadJourney])

  const openStep = (step: JourneyStep) => {
    setActiveStep(step)
    setStepNotes(step.user_notes || '')
    setAskQuestion('')
    setAskAnswer('')
  }

  const closeStep = () => {
    setActiveStep(null)
  }

  const updateStepStatus = async (status: string) => {
    if (!activeStep || !journey) return
    setUpdatingStep(true)
    setError('')
    try {
      const updated = await api<Journey>(`/api/v1/journeys/${journey.id}/steps/${activeStep.id}`, {
        method: 'PATCH',
        body: JSON.stringify({ status, user_notes: stepNotes || null }),
      })
      setJourney(updated)
      // Refresh the active step from the updated journey
      for (const phase of updated.phases) {
        const found = phase.steps.find((s) => s.id === activeStep.id)
        if (found) {
          setActiveStep(found)
          setStepNotes(found.user_notes || '')
          break
        }
      }
    } catch (e: any) {
      setError(e.message)
    } finally {
      setUpdatingStep(false)
    }
  }

  const askKunja = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!journey || !askQuestion.trim()) return
    setAsking(true)
    setError('')
    setAskAnswer('')
    try {
      const res = await api<{ answer: string }>(`/api/v1/journeys/${journey.id}/ask`, {
        method: 'POST',
        body: JSON.stringify({
          step_id: activeStep?.id ?? null,
          question: askQuestion,
        }),
      })
      setAskAnswer(res.answer)
    } catch (err: any) {
      setError(err.message)
    } finally {
      setAsking(false)
    }
  }

  if (loading) return <div className="card">Loading journey...</div>
  if (error && !journey) return <div className="card error-box">{error}</div>
  if (!journey) return null

  // ── Progress bar colors ──
  const pct = journey.progress.percentage
  const progressColor = pct >= 80 ? '#1a6b3c' : pct >= 40 ? '#b8860b' : '#e63946'

  return (
    <div>
      <a href="/" className="breadcrumb">← Back home</a>
      <header>
        <h1>
          {journey.phases.length > 0 ? (
            <>
              {journey.origin_country === 'malawi' ? '🇲🇼' : '🇿🇲'} {journey.company_name}
            </>
          ) : (
            journey.company_name
          )}
        </h1>
        <p>
          {journey.origin_country === 'malawi' ? 'Malawi' : 'Zambia'} →{' '}
          {journey.target_country === 'zambia' ? 'Zambia' : 'Malawi'} ·{' '}
          {journey.business_model_label}
        </p>
      </header>

      {error && <div className="card error-box">{error}</div>}

      {/* Progress overview */}
      <div className="card">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h2>Market Entry Journey</h2>
          <span style={{ fontSize: '2rem', fontWeight: 700, color: progressColor }}>
            {pct}%
          </span>
        </div>
        <div className="progress-bar" style={{ marginTop: '10px' }}>
          <div
            className="progress-fill"
            style={{ width: `${pct}%`, background: progressColor }}
          />
        </div>
        <p style={{ color: '#666', marginTop: '8px' }}>
          {journey.progress.completed_steps} of {journey.progress.total_steps} steps complete
          {journey.progress.next_step_title && (
            <> · Next: <strong>{journey.progress.next_step_title}</strong></>
          )}
        </p>
      </div>

      {/* Roadmap timeline */}
      {journey.phases.map((phase) => {
        const phaseCompleted = phase.steps.filter((s) => s.status === 'completed').length
        const phasePct = phase.steps.length > 0
          ? Math.round((phaseCompleted / phase.steps.length) * 100)
          : 0

        return (
          <div className="card" key={phase.id}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h2 style={{ margin: 0 }}>
                {phase.name}
              </h2>
              <span style={{ fontSize: '0.9rem', color: '#666' }}>
                {phaseCompleted}/{phase.steps.length}
              </span>
            </div>
            <p style={{ color: '#666', fontSize: '0.95rem', margin: '8px 0 15px' }}>
              {phase.description}
            </p>

            {/* Phase progress mini-bar */}
            <div className="progress-bar" style={{ height: '6px', marginBottom: '15px' }}>
              <div
                className="progress-fill"
                style={{ width: `${phasePct}%`, background: phasePct === 100 ? '#1a6b3c' : '#2a9d5c' }}
              />
            </div>

            {/* Steps */}
            <div>
              {phase.steps.map((step) => (
                <button
                  key={step.id}
                  className={`journey-step-row ${step.status}`}
                  onClick={() => openStep(step)}
                  title={STATUS_LABELS[step.status] || step.status}
                >
                  <span className={`step-status-icon ${step.status}`}>
                    {STATUS_ICONS[step.status] || '•'}
                  </span>
                  <span className="step-title">{step.title}</span>
                  {step.status === 'blocked' && (
                    <span className="step-blocked-hint">requires previous step</span>
                  )}
                </button>
              ))}
            </div>
          </div>
        )
      })}

      <div style={{ display: 'flex', gap: '10px', marginTop: '20px' }}>
        <button className="btn" onClick={() => navigate('/journeys/new')}>
          Start Another Journey
        </button>
      </div>

      {/* ── Step detail drawer ── */}
      {activeStep && (
        <div className="drawer-overlay" onClick={closeStep}>
          <div className="drawer" onClick={(e) => e.stopPropagation()}>
            <div className="drawer-header">
              <div>
                <h3>{activeStep.title}</h3>
                <span className={`status-pill ${activeStep.status}`}>
                  {STATUS_LABELS[activeStep.status] || activeStep.status}
                </span>
              </div>
              <button className="drawer-close" onClick={closeStep}>×</button>
            </div>

            <div className="drawer-body">
              {/* 1. What is this */}
              {activeStep.description && (
                <div className="step-section">
                  <h4>What is this?</h4>
                  <p>{activeStep.description}</p>
                </div>
              )}

              {/* 2. Why do I need it */}
              {activeStep.why_needed && (
                <div className="step-section">
                  <h4>Why do I need it?</h4>
                  <p>{activeStep.why_needed}</p>
                </div>
              )}

              {/* 3. Who is responsible */}
              {activeStep.authority && (
                <div className="step-section">
                  <h4>Who is responsible?</h4>
                  <p><strong>{activeStep.authority}</strong></p>
                </div>
              )}

              {/* 4. What do I need */}
              {activeStep.documents_needed && activeStep.documents_needed.length > 0 && (
                <div className="step-section">
                  <h4>What do I need?</h4>
                  <ul>
                    {activeStep.documents_needed.map((doc, i) => (
                      <li key={i}>{doc}</li>
                    ))}
                  </ul>
                </div>
              )}

              {/* 5. How do I do it */}
              {activeStep.instructions && (
                <div className="step-section">
                  <h4>How do I do it?</h4>
                  <div
                    style={{ whiteSpace: 'pre-wrap', lineHeight: 1.6 }}
                    dangerouslySetInnerHTML={{
                      __html: activeStep.instructions
                        .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
                        .replace(/\n/g, '<br/>'),
                    }}
                  />
                </div>
              )}

              {/* 6+7. Cost & Timeline */}
              <div style={{ display: 'flex', gap: '20px', flexWrap: 'wrap' }}>
                {activeStep.estimated_cost && (
                  <div className="step-section" style={{ flex: 1, minWidth: '180px' }}>
                    <h4>Estimated cost</h4>
                    <p>{activeStep.estimated_cost}</p>
                  </div>
                )}
                {activeStep.estimated_timeline && (
                  <div className="step-section" style={{ flex: 1, minWidth: '180px' }}>
                    <h4>Estimated timeline</h4>
                    <p>{activeStep.estimated_timeline}</p>
                  </div>
                )}
              </div>

              {/* Official source */}
              {activeStep.official_source && (
                <div className="step-section">
                  <h4>Official source</h4>
                  <a href={activeStep.official_source} target="_blank" rel="noreferrer" style={{ color: 'var(--primary)' }}>
                    {activeStep.official_source} →
                  </a>
                </div>
              )}

              {/* ── Ask Kunja ── */}
              <div className="step-section" style={{ borderTop: '2px solid var(--border)', paddingTop: '15px' }}>
                <h4>Ask Kunja about this step</h4>
                <form onSubmit={askKunja} style={{ marginBottom: '10px' }}>
                  <div style={{ display: 'flex', gap: '8px' }}>
                    <input
                      type="text"
                      placeholder="e.g. Do I need this if my products are made in Malawi?"
                      value={askQuestion}
                      onChange={(e) => setAskQuestion(e.target.value)}
                      style={{ flex: 1, padding: '10px', borderRadius: '6px', border: '1px solid var(--border)', fontSize: '0.95rem' }}
                    />
                    <button className="btn" type="submit" disabled={asking || !askQuestion.trim()}>
                      {asking ? 'Thinking...' : 'Ask'}
                    </button>
                  </div>
                </form>

                {askAnswer && (
                  <div className="ask-answer">
                    <strong style={{ color: 'var(--primary)' }}>Kunja says:</strong>
                    <p style={{ marginTop: '8px', whiteSpace: 'pre-wrap', lineHeight: 1.6 }}>
                      {askAnswer}
                    </p>
                  </div>
                )}
              </div>

              {/* ── Notes & status ── */}
              <div className="step-section">
                <h4>Your notes</h4>
                <textarea
                  value={stepNotes}
                  onChange={(e) => setStepNotes(e.target.value)}
                  placeholder="Add any notes about this step..."
                  rows={2}
                  style={{ width: '100%', padding: '10px', borderRadius: '6px', border: '1px solid var(--border)', fontSize: '0.95rem' }}
                />
              </div>

              <div className="drawer-actions">
                <button
                  className="btn-secondary"
                  onClick={() => updateStepStatus('in_progress')}
                  disabled={updatingStep || activeStep.status === 'in_progress'}
                >
                  Start this step
                </button>
                <button
                  className="btn"
                  onClick={() => updateStepStatus('completed')}
                  disabled={updatingStep || activeStep.status === 'completed'}
                >
                  ✓ Mark complete
                </button>
                <button
                  className="btn-secondary"
                  onClick={() => updateStepStatus('skipped')}
                  disabled={updatingStep || activeStep.status === 'skipped'}
                >
                  Skip
                </button>
              </div>

              {error && <div className="error-box" style={{ marginTop: '10px' }}>{error}</div>}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default JourneyView