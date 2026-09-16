import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { api, JourneyOptions, Journey } from '../lib/api'

interface WizardData {
  origin: string
  target: string
  companyName: string
  industry: string
  businessModel: string
  businessDescription: string
  productDescription: string
}

const STEPS = ['Business Details', 'Target Market', 'Product & Activity', 'Review']

export default function JourneyNew() {
  const navigate = useNavigate()
  const [step, setStep] = useState(0)
  const [options, setOptions] = useState<JourneyOptions | null>(null)
  const [loading, setLoading] = useState(true)
  const [creating, setCreating] = useState(false)
  const [error, setError] = useState('')

  const [data, setData] = useState<WizardData>({
    origin: 'malawi',
    target: 'zambia',
    companyName: '',
    industry: 'general',
    businessModel: 'distributor',
    businessDescription: '',
    productDescription: '',
  })

  useEffect(() => {
    api<JourneyOptions>('/api/v1/journeys/options')
      .then((d) => {
        setOptions(d)
        if (d.business_models.length > 0) {
          setData((prev) => ({ ...prev, businessModel: d.business_models[0].key }))
        }
      })
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }, [])

  const update = (patch: Partial<WizardData>) => setData((prev) => ({ ...prev, ...patch }))

  const next = () => {
    setError('')
    if (step === 0 && !data.companyName.trim()) {
      setError('Please enter your company name')
      return
    }
    if (step < 3) setStep(step + 1)
  }

  const back = () => { setError(''); if (step > 0) setStep(step - 1) }

  const createJourney = async () => {
    setCreating(true)
    setError('')
    try {
      const journey = await api<Journey>('/api/v1/journeys', {
        method: 'POST',
        body: JSON.stringify({
          company_name: data.companyName.trim(),
          origin_country: data.origin,
          target_country: data.target,
          industry: data.industry,
          business_model: data.businessModel,
          business_description: (data.productDescription || data.businessDescription).trim() || null,
        }),
      })
      navigate(`/journeys/${journey.id}`)
    } catch (err: any) {
      setError(err.message)
      setCreating(false)
    }
  }

  if (loading) {
    return <div className="card text-center">Loading options...</div>
  }

  const modelInfo = options?.business_models.find((m) => m.key === data.businessModel)
  const originCountry = options?.countries.find((c) => c.key === data.origin)
  const targetCountry = options?.countries.find((c) => c.key === data.target)

  return (
    <div className="wizard-container">
      <h1 style={{ textAlign: 'center', marginBottom: '32px', fontSize: '1.5rem', fontWeight: 700 }}>
        Plan Your Market Entry
      </h1>

      {/* Step indicator */}
      <div className="wizard-steps-indicator">
        {STEPS.map((label, i) => (
          <div key={label} style={{ display: 'flex', alignItems: 'center' }}>
            <div className={`wizard-step-dot ${i === step ? 'active' : i < step ? 'completed' : ''}`}>
              <div className="wizard-step-circle" />
              <span className="wizard-step-label">{label}</span>
            </div>
            {i < STEPS.length - 1 && (
              <div className={`wizard-connector ${i < step ? 'completed' : ''}`} />
            )}
          </div>
        ))}
      </div>

      {error && <div className="error-box mb-2">{error}</div>}

      {/* Step 0: Business Details */}
      {step === 0 && (
        <div className="wizard-card">
          <h2>Business Details</h2>
          <p className="wizard-subtitle">Where are you based and what do you do?</p>

          <div className="form-group">
            <label>Company name</label>
            <input
              type="text"
              placeholder="e.g. Mango Fresh Ltd"
              value={data.companyName}
              onChange={(e) => update({ companyName: e.target.value })}
            />
          </div>

          <div className="form-group">
            <label>Where are you based?</label>
            <div className="country-cards">
              {options?.countries.map((c) => (
                <button
                  key={c.key}
                  className={`country-card-select ${data.origin === c.key ? 'selected' : ''}`}
                  onClick={() => {
                    update({ origin: c.key, target: c.key === 'malawi' ? 'zambia' : 'malawi' })
                  }}
                >
                  <span className="country-flag">{c.flag}</span>
                  <span className="country-name">{c.name}</span>
                </button>
              ))}
            </div>
          </div>

          <div className="form-group">
            <label>Industry</label>
            <select value={data.industry} onChange={(e) => update({ industry: e.target.value })}>
              {options?.industries.map((ind) => (
                <option key={ind} value={ind}>
                  {ind.replace(/_/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase())}
                </option>
              ))}
            </select>
          </div>

          <div className="wizard-actions">
            <div />
            <button className="btn btn-lg" onClick={next}>
              Next →
            </button>
          </div>
        </div>
      )}

      {/* Step 1: Target Market */}
      {step === 1 && (
        <div className="wizard-card">
          <h2>Target Market</h2>
          <p className="wizard-subtitle">Where do you want to expand?</p>

          <div className="country-cards">
            {options?.countries
              .filter((c) => c.key !== data.origin)
              .map((c) => (
                <button
                  key={c.key}
                  className={`country-card-select ${data.target === c.key ? 'selected' : ''}`}
                  onClick={() => update({ target: c.key })}
                >
                  <span className="country-flag">{c.flag}</span>
                  <span className="country-name">{c.name}</span>
                </button>
              ))}
          </div>

          <div className="wizard-actions">
            <button className="btn-secondary" onClick={back}>← Back</button>
            <button className="btn btn-lg" onClick={next}>Next →</button>
          </div>
        </div>
      )}

      {/* Step 2: Product & Activity */}
      {step === 2 && (
        <div className="wizard-card">
          <h2>Product & Activity</h2>
          <p className="wizard-subtitle">What do you sell and how do you want to enter?</p>

          <div className="form-group">
            <label>What do you sell or provide?</label>
            <input
              type="text"
              placeholder="e.g. Packaged Peanut Butter"
              value={data.productDescription}
              onChange={(e) => update({ productDescription: e.target.value })}
            />
          </div>

          <div className="form-group">
            <label>How do you want to enter {targetCountry?.name || 'the target market'}?</label>
            <div className="option-cards">
              {options?.business_models.map((m) => (
                <button
                  key={m.key}
                  className={`option-card ${data.businessModel === m.key ? 'selected' : ''}`}
                  onClick={() => update({ businessModel: m.key })}
                >
                  <div className="option-card-radio" />
                  <div className="option-card-body">
                    <h4>{m.label}</h4>
                    <p>{m.description}</p>
                  </div>
                </button>
              ))}
            </div>
          </div>

          <div className="wizard-actions">
            <button className="btn-secondary" onClick={back}>← Back</button>
            <button className="btn btn-lg" onClick={next}>Next →</button>
          </div>
        </div>
      )}

      {/* Step 3: Review */}
      {step === 3 && (
        <div className="wizard-card">
          <h2>Your Market Journey</h2>
          <p className="wizard-subtitle">Review your details before we map your roadmap.</p>

          <div className="review-grid">
            <div className="review-row">
              <span className="review-label">From</span>
              <span className="review-value">
                {originCountry?.flag} {originCountry?.name}
              </span>
            </div>
            <div className="review-row">
              <span className="review-label">To</span>
              <span className="review-value">
                {targetCountry?.flag} {targetCountry?.name}
              </span>
            </div>
            <div className="review-row">
              <span className="review-label">Company</span>
              <span className="review-value">{data.companyName}</span>
            </div>
            <div className="review-row">
              <span className="review-label">Industry</span>
              <span className="review-value">
                {data.industry.replace(/_/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase())}
              </span>
            </div>
            {data.productDescription && (
              <div className="review-row">
                <span className="review-label">Product</span>
                <span className="review-value">{data.productDescription}</span>
              </div>
            )}
            <div className="review-row">
              <span className="review-label">Market Entry Model</span>
              <span className="review-value">{modelInfo?.label || data.businessModel}</span>
            </div>
          </div>

          <div className="wizard-actions">
            <button className="btn-secondary" onClick={back}>← Back</button>
            <button className="btn btn-xl" onClick={createJourney} disabled={creating}>
              {creating ? (
                <><span className="spinner" /> Creating your journey...</>
              ) : (
                'Create my journey →'
              )}
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
