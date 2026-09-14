import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { api, Country } from '../lib/api'

function NewChecklist() {
  const navigate = useNavigate()
  const [countries, setCountries] = useState<Country[]>([])
  const [origin, setOrigin] = useState('Malawi')
  const [target, setTarget] = useState('Zambia')
  const [businessType, setBusinessType] = useState('llc')
  const [industry, setIndustry] = useState('')
  const [companyName, setCompanyName] = useState('')
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [submitting, setSubmitting] = useState(false)

  useEffect(() => {
    api<{ countries: Country[] }>('/api/v1/checklists/countries')
      .then((data) => setCountries(data.countries))
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }, [])

  const handleOriginChange = (value: string) => {
    setOrigin(value)
    if (value === target) {
      setTarget(value === 'Malawi' ? 'Zambia' : 'Malawi')
    }
  }

  const handleTargetChange = (value: string) => {
    setTarget(value)
    if (value === origin) {
      setOrigin(value === 'Malawi' ? 'Zambia' : 'Malawi')
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setSubmitting(true)
    setError('')
    try {
      const checklist = await api<{ id: number }>('/api/v1/checklists', {
        method: 'POST',
        body: JSON.stringify({
          origin_country: origin,
          target_country: target,
          business_type: businessType,
          industry,
          company_name: companyName,
        }),
      })
      navigate(`/checklists/${checklist.id}`)
    } catch (e: any) {
      setError(e.message)
    } finally {
      setSubmitting(false)
    }
  }

  if (loading) return <div className="card">Loading...</div>

  return (
    <div>
      <a href="/" style={{ color: 'var(--primary)', textDecoration: 'none' }}>← Back home</a>
      <header>
        <h1>New Compliance Checklist</h1>
        <p>Tell us about your cross-border business plans</p>
      </header>

      <div className="card">
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>I am based in (origin country)</label>
            <select value={origin} onChange={(e) => handleOriginChange(e.target.value)}>
              {countries.map((c) => (
                <option key={c.code} value={c.name}>{c.flag} {c.name}</option>
              ))}
            </select>
          </div>

          <div className="form-group">
            <label>I want to expand to (target country)</label>
            <select value={target} onChange={(e) => handleTargetChange(e.target.value)}>
              {countries.map((c) => (
                <option key={c.code} value={c.name}>{c.flag} {c.name}</option>
              ))}
            </select>
          </div>

          <div className="form-group">
            <label>Company name</label>
            <input
              type="text"
              value={companyName}
              onChange={(e) => setCompanyName(e.target.value)}
              placeholder="e.g. Mango Trading Ltd"
              required
            />
          </div>

          <div className="form-group">
            <label>Business type</label>
            <select value={businessType} onChange={(e) => setBusinessType(e.target.value)}>
              <option value="llc">Limited Liability Company (Ltd)</option>
              <option value="sole_proprietor">Sole Proprietor</option>
              <option value="partnership">Partnership</option>
              <option value="branch">Branch Office</option>
            </select>
          </div>

          <div className="form-group">
            <label>Industry</label>
            <input
              type="text"
              value={industry}
              onChange={(e) => setIndustry(e.target.value)}
              placeholder="e.g. Agriculture, Retail, Tech..."
              required
            />
          </div>

          {error && <div className="error-box">{error}</div>}

          <button type="submit" className="btn" disabled={submitting}>
            {submitting ? 'Creating...' : 'Start Checklist'}
          </button>
        </form>
      </div>

      {target && (
        <div className="card">
          <h2>What you'll be checked against</h2>
          <p>Your compliance with <strong>{target}</strong> regulations:</p>
          {countries
            .filter((c) => c.name === target)
            .map((c) => (
              <ul key={c.code}>
                {c.categories.map((cat) => (
                  <li key={cat.key}>
                    <strong>{cat.name}</strong> ({cat.question_count} questions)
                    <br />
                    <small>{cat.regulation}</small>
                  </li>
                ))}
              </ul>
            ))}
        </div>
      )}
    </div>
  )
}

export default NewChecklist