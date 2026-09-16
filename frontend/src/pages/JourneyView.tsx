import { useState, useEffect, useCallback } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { api, Journey, JourneyStep } from '../lib/api'

const STATUS_ICONS: Record<string, string> = {
  completed: '✓',
  in_progress: '●',
  needs_verification: '⚠',
  not_started: '○',
  blocked: '🔒',
  skipped: '–',
}

const STATUS_LABELS: Record<string, string> = {
  completed: 'Complete',
  in_progress: 'In progress',
  needs_verification: 'Needs verification',
  not_started: 'Not started',
  blocked: 'Blocked',
  skipped: 'Skipped',
}

export default function JourneyView() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [journey, setJourney] = useState<Journey | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  // Active phase (for timeline navigation)
  const [activePhase, setActivePhase] = useState<number>(0)

  // Step detail drawer
  const [activeStep, setActiveStep] = useState<JourneyStep | null>(null)
  const [activeStepPhaseName, setActiveStepPhaseName] = useState('')
  const [updatingStep, setUpdatingStep] = useState(false)
  const [stepNotes, setStepNotes] = useState('')

  // Ask Kunja
  const [askQuestion, setAskQuestion] = useState('')
  const [askAnswer, setAskAnswer] = useState('')
  const [asking, setAsking] = useState(false)

  const loadJourney = useCallback(() => {
    api<Journey>(`/api/v1/journeys/${id}`)
      .then((j) => {
        setJourney(j)
        // Auto-select the current phase (first incomplete phase)
        const incomplete = j.phases.findIndex((p) =>
          p.steps.some((s) => s.status !== 'completed' && s.status !== 'skipped')
        )
        setActivePhase(incomplete >= 0 ? incomplete : 0)
      })
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }, [id])

  useEffect(() => { loadJourney() }, [loadJourney])

  const openStep = (step: JourneyStep, phaseName: string) => {
    setActiveStep(step)
    setActiveStepPhaseName(phaseName)
    setStepNotes(step.user_notes || '')
    setAskQuestion('')
    setAskAnswer('')
  }

  const closeStep = () => setActiveStep(null)

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
    setAskAnswer('')
    try {
      const res = await api<{ answer: string }>(`/api/v1/journeys/${journey.id}/ask`, {
        method: 'POST',
        body: JSON.stringify({ step_id: activeStep?.id ?? null, question: askQuestion }),
      })
      setAskAnswer(res.answer)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Ask failed')
    } finally {
      setAsking(false)
    }
  }

  if (loading) return <div className="card text-center">Loading journey...</div>
  if (error && !journey) return <div className="card error-box">{error}</div>
  if (!journey) return null

  const pct = journey.progress.percentage
  const currentPhase = journey.phases[activePhase]

  // Completion check
  const allComplete = journey.phases.every((p) =>
    p.steps.every((s) => s.status === 'completed' || s.status === 'skipped')
  )

  if (allComplete) {
    return (
      <div className="completion-screen">
        <div className="completion-icon">🎉</div>
        <h1>You're ready for market!</h1>
        <p>
          Your market-entry journey from{' '}
          {journey.origin_country === 'malawi' ? 'Malawi' : 'Zambia'} to{' '}
          {journey.target_country === 'zambia' ? 'Zambia' : 'Malawi'} is complete.
        </p>
        <div className="completion-checklist">
          <div className="completion-checklist-item">
            <span className="completion-check">✓</span>
            All required steps completed
          </div>
          <div className="completion-checklist-item">
            <span className="completion-check">✓</span>
            Outstanding issues: 0
          </div>
        </div>
        <div className="completion-actions">
          <button className="btn btn-lg" onClick={() => navigate('/dashboard')}>
            Back to Dashboard
          </button>
          <button className="btn-secondary btn-lg" onClick={() => navigate('/journeys/new')}>
            Start another journey
          </button>
        </div>
      </div>
    )
  }

  return (
    <div>
      {/* Journey header */}
      <div className="flex-between mb-2">
        <div>
          <h1 style={{ fontSize: '1.3rem', fontWeight: 700, marginBottom: '4px' }}>
            {journey.origin_country === 'malawi' ? '🇲🇼' : '🇿🇲'}{' '}
            {journey.company_name}
          </h1>
          <p className="text-sm text-muted">
            {journey.origin_country === 'malawi' ? 'Malawi' : 'Zambia'} →{' '}
            {journey.target_country === 'zambia' ? 'Zambia' : 'Malawi'} ·{' '}
            {journey.industry.replace(/_/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase())} ·{' '}
            {journey.business_model_label}
          </p>
        </div>
        <button className="btn-secondary" onClick={() => navigate('/journeys/new')}>
          + New Journey
        </button>
      </div>

      {/* Progress overview */}
      <div className="card">
        <div className="flex-between mb-1">
          <h2 style={{ fontSize: '1rem' }}>Your Market Entry Progress</h2>
          <span style={{ fontSize: '1.6rem', fontWeight: 700, color: 'var(--primary)' }}>
            {pct}%
          </span>
        </div>
        <div className="progress-bar progress-bar-lg">
          <div
            className="progress-fill"
            style={{
              width: `${pct}%`,
              background: pct >= 80 ? 'var(--completed)' : 'var(--primary)',
            }}
          />
        </div>
        <p className="text-sm text-muted mt-1">
          {journey.progress.completed_steps} completed ·{' '}
          {journey.progress.in_progress_steps} in progress ·{' '}
          {journey.progress.total_steps - journey.progress.completed_steps - journey.progress.in_progress_steps} pending
        </p>
      </div>

      {/* Next Steps */}
      {journey.progress.next_step_id && (
        <div className="card">
          <h2 style={{ marginBottom: '14px' }}>Your next steps</h2>
          <div className="next-steps-list">
            {journey.phases
              .flatMap((phase) =>
                phase.steps
                  .filter((s) => s.status === 'not_started' || s.status === 'in_progress')
                  .slice(0, 3)
                  .map((s) => ({ ...s, phaseName: phase.name }))
              )
              .map((step, i) => (
                <button
                  key={step.id}
                  className="next-step-card"
                  onClick={() => openStep(step, step.phaseName)}
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

      {/* Phase timeline */}
      <div className="card">
        <h2 style={{ marginBottom: '18px' }}>Market Entry Roadmap</h2>
        <div className="phase-timeline">
          {journey.phases.map((phase, i) => {
            const completedSteps = phase.steps.filter((s) => s.status === 'completed' || s.status === 'skipped').length
            const isComplete = completedSteps === phase.steps.length
            const isCurrent = i === activePhase
            const isPast = i < activePhase || isComplete

            return (
              <div key={phase.id} className="phase-timeline-item">
                <div
                  className={`phase-timeline-node ${isComplete ? 'completed' : isCurrent ? 'current active' : ''}`}
                  onClick={() => setActivePhase(i)}
                >
                  <div className="phase-timeline-circle">
                    {isComplete ? '' : i + 1}
                  </div>
                  <span className="phase-timeline-label">{phase.name}</span>
                </div>
                {i < journey.phases.length - 1 && (
                  <div className={`phase-timeline-connector ${isPast && isComplete ? 'completed' : ''}`} />
                )}
              </div>
            )
          })}
        </div>
      </div>

      {/* Active phase steps */}
      {currentPhase && (
        <div className="card">
          <div className="flex-between mb-1">
            <div>
              <h2 style={{ fontSize: '1.05rem', marginBottom: '2px' }}>
                {currentPhase.name}
              </h2>
              <p className="text-sm text-muted">{currentPhase.description}</p>
            </div>
            <span className="text-sm text-muted">
              {currentPhase.steps.filter((s) => s.status === 'completed').length}/{currentPhase.steps.length}
            </span>
          </div>

          <div className="progress-bar-sm" style={{ marginBottom: '18px' }}>
            <div
              className="progress-fill"
              style={{
                width: `${currentPhase.steps.length > 0 ? (currentPhase.steps.filter((s) => s.status === 'completed').length / currentPhase.steps.length) * 100 : 0}%`,
                background: 'var(--primary)',
              }}
            />
          </div>

          <div>
            {currentPhase.steps.map((step) => (
              <button
                key={step.id}
                className={`step-card ${step.status === 'blocked' ? 'blocked' : ''}`}
                onClick={() => {
                  if (step.status !== 'blocked') openStep(step, currentPhase.name)
                }}
              >
                <div className={`step-status ${step.status}`}>
                  {STATUS_ICONS[step.status] || '○'}
                </div>
                <div className="step-card-body">
                  <div className="step-card-title">{step.title}</div>
                  <div className="step-card-subtitle">
                    {STATUS_LABELS[step.status]}
                    {step.status === 'blocked' && ' · Requires previous step'}
                  </div>
                </div>
                <span className="step-card-arrow">→</span>
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Step detail drawer */}
      {activeStep && (
        <div className="drawer-overlay" onClick={closeStep}>
          <div className="drawer" onClick={(e) => e.stopPropagation()}>
            <div className="drawer-header">
              <div>
                <h3>{activeStep.title}</h3>
                <span className="text-sm text-muted">{activeStepPhaseName}</span>
                <div style={{ marginTop: '8px' }}>
                  <span className={`status-pill ${activeStep.status}`}>
                    {STATUS_LABELS[activeStep.status] || activeStep.status}
                  </span>
                </div>
              </div>
              <button className="drawer-close" onClick={closeStep}>×</button>
            </div>

            <div className="drawer-body">
              {error && <div className="error-box mb-2">{error}</div>}

              {activeStep.description && (
                <div className="step-section">
                  <h4>What is this?</h4>
                  <p>{activeStep.description}</p>
                </div>
              )}

              {activeStep.why_needed && (
                <div className="step-section">
                  <h4>Why do I need it?</h4>
                  <p>{activeStep.why_needed}</p>
                </div>
              )}

              {activeStep.authority && (
                <div className="step-section">
                  <h4>Who handles it?</h4>
                  <p><strong>{activeStep.authority}</strong></p>
                </div>
              )}

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

              {activeStep.instructions && (
                <div className="step-section">
                  <h4>How do I complete it?</h4>
                  <div
                    style={{ whiteSpace: 'pre-wrap', lineHeight: 1.7, fontSize: '0.92rem' }}
                    dangerouslySetInnerHTML={{
                      __html: activeStep.instructions
                        .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
                        .replace(/\n/g, '<br/>'),
                    }}
                  />
                </div>
              )}

              <div style={{ display: 'flex', gap: '20px', flexWrap: 'wrap' }}>
                {activeStep.estimated_cost && (
                  <div className="step-section" style={{ flex: 1, minWidth: '160px' }}>
                    <h4>Estimated cost</h4>
                    <p>{activeStep.estimated_cost}</p>
                  </div>
                )}
                {activeStep.estimated_timeline && (
                  <div className="step-section" style={{ flex: 1, minWidth: '160px' }}>
                    <h4>Estimated timeline</h4>
                    <p>{activeStep.estimated_timeline}</p>
                  </div>
                )}
              </div>

              {activeStep.official_source && (
                <div className="step-section">
                  <h4>Official source</h4>
                  <a href={activeStep.official_source} target="_blank" rel="noreferrer" style={{ color: 'var(--primary)' }}>
                    {activeStep.official_source} →
                  </a>
                </div>
              )}

              {/* Ask Kunja */}
              <div className="step-section">
                <div className="ask-section">
                  <h4>💬 Ask Kunja about this step</h4>
                  <form onSubmit={askKunja} className="ask-form">
                    <input
                      type="text"
                      placeholder="e.g. Do I need this if my products are made in Malawi?"
                      value={askQuestion}
                      onChange={(e) => setAskQuestion(e.target.value)}
                    />
                    <button className="btn" type="submit" disabled={asking || !askQuestion.trim()}>
                      {asking ? <span className="spinner" /> : 'Ask'}
                    </button>
                  </form>

                  {askAnswer && (
                    <div className="ask-answer">
                      <div className="ask-label">💬 Kunja</div>
                      <p style={{ whiteSpace: 'pre-wrap', lineHeight: 1.65 }}>{askAnswer}</p>
                    </div>
                  )}
                </div>
              </div>

              {/* Notes */}
              <div className="step-section">
                <h4>Your notes</h4>
                <textarea
                  value={stepNotes}
                  onChange={(e) => setStepNotes(e.target.value)}
                  placeholder="Add any notes about this step..."
                  rows={2}
                  style={{ width: '100%', padding: '10px', borderRadius: 'var(--radius-sm)', border: '1.5px solid var(--border)', fontSize: '0.9rem', fontFamily: 'var(--font)' }}
                />
              </div>
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
          </div>
        </div>
      )}
    </div>
  )
}
