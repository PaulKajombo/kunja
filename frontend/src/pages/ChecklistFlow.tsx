import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { api, Checklist, Question } from '../lib/api'

function ChecklistFlow() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [checklist, setChecklist] = useState<Checklist | null>(null)
  const [questions, setQuestions] = useState<Record<string, any>>({})
  const [answers, setAnswers] = useState<Record<string, string>>({})
  const [currentCategory, setCurrentCategory] = useState('')
  const [loading, setLoading] = useState(true)
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    loadAll()
  }, [id])

  const loadAll = async () => {
    setLoading(true)
    try {
      const cl = await api<Checklist>(`/api/v1/checklists/${id}`)
      setChecklist(cl)
      const qs = await api<Record<string, any>>(`/api/v1/checklists/questions/${cl.target_country.toLowerCase()}`)
      setQuestions(qs)
      const cats = Object.keys(qs)
      if (cats.length > 0) setCurrentCategory(cats[0])
    } catch (e: any) {
      setError(e.message)
    } finally {
      setLoading(false)
    }
  }

  const categories = Object.keys(questions)

  const catQuestions = (cat: string): Question[] =>
    questions[cat]?.questions || []

  const catAnswered = (cat: string) => {
    const qs = catQuestions(cat)
    return qs.filter((q) => answers[q.id]).length
  }

  const handleAnswer = (questionId: string, value: string) => {
    setAnswers((prev) => ({ ...prev, [questionId]: value }))
  }

  const allAnswered = () => {
    const total = categories.reduce((acc, cat) => acc + catQuestions(cat).length, 0)
    return Object.keys(answers).length >= total
  }

  const handleSubmit = async () => {
    setSubmitting(true)
    setError('')
    try {
      await api<any>(`/api/v1/checklists/${id}/submit`, {
        method: 'POST',
        body: JSON.stringify({ answers }),
      })
      navigate(`/checklists/${id}/results`)
    } catch (e: any) {
      setError(e.message)
      setSubmitting(false)
    }
  }

  if (loading) return <div className="card">Loading checklist...</div>
  if (error && !checklist) return <div className="card error-box">{error}</div>

  return (
    <div>
      <a href="/" style={{ color: 'var(--primary)', textDecoration: 'none' }}>← Back home</a>
      <header>
        <h1>Compliance Check: {checklist?.target_country}</h1>
        <p>
          {checklist?.company_name} • {checklist?.origin_country} → {checklist?.target_country} • {checklist?.business_type}
        </p>
      </header>

      <div style={{ display: 'flex', gap: '20px', marginBottom: '20px' }}>
        {/* Category sidebar */}
        <div style={{ minWidth: '220px' }}>
          {categories.map((cat) => {
            const data = questions[cat]
            const total = data.questions.length
            const done = catAnswered(cat)
            return (
              <button
                key={cat}
                onClick={() => setCurrentCategory(cat)}
                className={`cat-btn ${currentCategory === cat ? 'active' : ''}`}
              >
                <div style={{ fontWeight: 600 }}>{data.name}</div>
                <small>{done}/{total} answered</small>
              </button>
            )
          })}
        </div>

        {/* Questions */}
        <div style={{ flex: 1 }}>
          {currentCategory && questions[currentCategory] && (
            <div className="card">
              <h2>{questions[currentCategory].name}</h2>
              <p style={{ color: '#666', marginBottom: '15px' }}>
                {questions[currentCategory].regulation}
              </p>

              {catQuestions(currentCategory).map((q, i) => (
                <div key={q.id} className="question-block">
                  <p style={{ fontWeight: 500 }}>
                    {i + 1}. {q.question}
                    {q.critical && <span className="critical-badge">Important</span>}
                  </p>
                  <div className="yes-no">
                    <button
                      type="button"
                      className={answers[q.id] === 'yes' ? 'yes-btn selected' : 'yes-btn'}
                      onClick={() => handleAnswer(q.id, 'yes')}
                    >
                      ✓ Yes
                    </button>
                    <button
                      type="button"
                      className={answers[q.id] === 'no' ? 'no-btn selected' : 'no-btn'}
                      onClick={() => handleAnswer(q.id, 'no')}
                    >
                      ✗ No
                    </button>
                  </div>
                  {answers[q.id] === 'no' && (
                    <small style={{ color: 'var(--secondary)' }}>
                      {q.requirement}
                    </small>
                  )}
                </div>
              ))}

              <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '20px' }}>
                <button
                  className="btn-secondary"
                  onClick={() => {
                    const idx = categories.indexOf(currentCategory)
                    if (idx > 0) setCurrentCategory(categories[idx - 1])
                  }}
                  disabled={categories.indexOf(currentCategory) === 0}
                >
                  ← Previous
                </button>

                {categories.indexOf(currentCategory) < categories.length - 1 ? (
                  <button
                    className="btn"
                    onClick={() => setCurrentCategory(categories[categories.indexOf(currentCategory) + 1])}
                  >
                    Next Section →
                  </button>
                ) : (
                  <button
                    className="btn"
                    onClick={handleSubmit}
                    disabled={!allAnswered() || submitting}
                  >
                    {submitting ? 'Submitting...' : 'Submit & Get Score'}
                  </button>
                )}
              </div>
            </div>
          )}

          {!allAnswered() && (
            <p style={{ color: '#666', marginTop: '10px' }}>
              Answer all questions to get your compliance score
            </p>
          )}
          {error && <div className="error-box">{error}</div>}
        </div>
      </div>
    </div>
  )
}

export default ChecklistFlow