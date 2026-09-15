import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { api, JourneyOptions, Journey } from '../lib/api'

function NewJourney() {
  const navigate = useNavigate()

  const [options, setOptions] = useState<JourneyOptions | null>(null)
  const [origin, setOrigin] = useState('malawi')
  const [target, setTarget] = useState('zambia')
  const [companyName, setCompanyName] = useState('')
  const [industry, setIndustry] = useState('general')
  const [businessModel, setBusinessModel] = useState('distributor')
  const [businessDescription, setBusinessDescription] = useState('')

  const [loading, setLoading] = useState(true)
  const [creating, setCreating] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    api<JourneyOptions>('/api/v1/journeys/options')
      .then((data) => {
        setOptions(data)
        if (data.business_models.length > 0) {
          setBusinessModel(data.business_models[0].key)
        }
      })
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }, [])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!companyName.trim()) {
      setError('Please enter your company name')
      return
    }
    setCreating(true)
    setError('')
    try {
      const journey = await api<Journey>('/api/v1/journeys', {
        method: 'POST',
        body: JSON.stringify({
          company_name: companyName.trim(),
          origin_country: origin,
          target_country: target,
          industry,
          business_model: businessModel,
          business_description: businessDescription.trim() || null,
        }),
      })
      navigate(`/journeys/${journey.id}`)
    } catch (err: any) {
      setError(err.message)
      setCreating(false)
    }
  }

  if (loading) return <div className="card">Loading...</div>

  const modelInfo = options?.business_models.find((m) => m.key === businessModel)

  return (
    <div>
      <a href="/" className="breadcrumb">← Back home</a>
      <header>
        <h1>Plan Your Market Entry</h1>
        <p>Tell us about your business and we'll map your complete journey</p>
      </header>

      <form className="card" onSubmit={handleSubmit}>
        {error && <div className="error-box" style={{ marginBottom: '15px' }}>{error}</div>}

        <div className="form-group">
          <label>Origin country (where your business is based)</label>
          <select value={origin} onChange={(e) => { setOrigin(e.target.value); setTarget(e.target.value === 'malawi' ? 'zambia' : 'malawi') }}>
            {options?.countries.map((c) => (
              <option key={c.key} value={c.key}>{c.flag} {c.name}</option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label>Target country (where you want to expand)</label>
          <select value={target} onChange={(e) => { setTarget(e.target.value); setOrigin(e.target.value === 'malawi' ? 'zambia' : 'malawi') }}>
            {options?.countries.map((c) => (
              <option key={c.key} value={c.key}>{c.flag} {c.name}</option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label>Company name</label>
          <input
            type="text"
            placeholder="e.g. Mango Trading Ltd"
            value={companyName}
            onChange={(e) => setCompanyName(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label>Industry</label>
          <select value={industry} onChange={(e) => setIndustry(e.target.value)}>
            {options?.industries.map((ind) => (
              <option key={ind} value={ind}>
                {ind.replace(/_/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase())}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label>How do you want to enter {options?.countries.find((c) => c.key === target)?.name}?</label>
          <select value={businessModel} onChange={(e) => setBusinessModel(e.target.value)}>
            {options?.business_models.map((m) => (
              <option key={m.key} value={m.key}>{m.label}</option>
            ))}
          </select>
          {modelInfo && (
            <small style={{ color: '#666', display: 'block', marginTop: '5px' }}>
              {modelInfo.description}
            </small>
          )}
        </div>

        <div className="form-group">
          <label>Briefly describe what your business does (optional)</label>
          <textarea
            placeholder="e.g. We manufacture maize flour and want to export through a Lusaka distributor"
            value={businessDescription}
            onChange={(e) => setBusinessDescription(e.target.value)}
            rows={3}
            style={{ width: '100%', padding: '10px', borderRadius: '6px', border: '1px solid var(--border)', fontSize: '1rem' }}
          />
        </div>

        <button className="btn" type="submit" disabled={creating}>
          {creating ? 'Mapping your journey...' : 'Map My Journey →'}
        </button>
      </form>
    </div>
  )
}

export default NewJourney