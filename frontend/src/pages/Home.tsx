import { useNavigate } from 'react-router-dom'

function Home() {
  const navigate = useNavigate()

  return (
    <div>
      <header>
        <h1>🇿🇲 Kunja 🇲🇼</h1>
        <p>Your guide to entering African markets</p>
      </header>

      <div className="card">
        <h2>Plan → Prepare → Comply → Enter → Operate</h2>
        <p>
          Kunja maps your complete market-entry journey. Whether you're a Malawian
          expanding into Zambia, or a Zambian coming to Malawi, we show you exactly
          what to do, in what order, and help at every step.
        </p>
      </div>

      <div className="card" style={{ textAlign: 'center' }}>
        <h2>Begin Your Journey</h2>
        <p style={{ marginBottom: '15px' }}>
          Tell us about your business and get a step-by-step roadmap.
        </p>
        <button className="btn" onClick={() => navigate('/journeys/new')} style={{ fontSize: '1.1rem', padding: '12px 30px' }}>
          🗺️ Map My Market Entry →
        </button>
      </div>

      <div className="country-flags">
        <div className="country-card">
          <span>🇲🇼</span>
          <h3>From Malawi</h3>
          <p>Company readiness, export permits, SADC trade</p>
        </div>
        <div className="country-card">
          <span>↔️</span>
          <h3>Cross-Border</h3>
          <p>Certificates of origin, customs, product standards</p>
        </div>
        <div className="country-card">
          <span>🇿🇲</span>
          <h3>Into Zambia</h3>
          <p>PACRA registration, ZRA tax, permits, operations</p>
        </div>
      </div>

      <div className="card">
        <h2>How It Works</h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '15px', marginTop: '15px' }}>
          <div>
            <h3 style={{ color: 'var(--primary)' }}>1. Tell us your plan</h3>
            <p style={{ color: '#666' }}>Your country, industry, and how you want to enter the market</p>
          </div>
          <div>
            <h3 style={{ color: 'var(--primary)' }}>2. We map the path</h3>
            <p style={{ color: '#666' }}>Every step from preparation to ongoing compliance, in order</p>
          </div>
          <div>
            <h3 style={{ color: 'var(--primary)' }}>3. Follow the roadmap</h3>
            <p style={{ color: '#666' }}>Track progress, mark steps complete, see what's next</p>
          </div>
          <div>
            <h3 style={{ color: 'var(--primary)' }}>4. Ask Kunja anything</h3>
            <p style={{ color: '#666' }}>AI guidance on any step, using your actual journey context</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Home
