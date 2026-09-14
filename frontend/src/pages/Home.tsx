import { useNavigate } from 'react-router-dom'

function Home() {
  const navigate = useNavigate()

  return (
    <div>
      <header>
        <h1>🇿🇲 Kunja 🇲🇼</h1>
        <p>Cross-border compliance for Malawi ↔ Zambia</p>
      </header>

      <div className="card">
        <h2>Welcome to Kunja</h2>
        <p>
          Kunja helps businesses establish themselves across the Malawi-Zambia border.
          Whether you're a Malawian expanding into Zambia, or a Zambian coming to Malawi,
          we make compliance simple.
        </p>
      </div>

      <div className="country-flags">
        <div className="country-card">
          <span>🇲🇼</span>
          <h3>Malawi</h3>
          <p>Business registration, tax, employment, immigration</p>
        </div>
        <div className="country-card">
          <span>↔️</span>
          <h3>Cross-Border</h3>
          <p>Work permits, SADC trade, double taxation</p>
        </div>
        <div className="country-card">
          <span>🇿🇲</span>
          <h3>Zambia</h3>
          <p>Business registration, tax, employment, immigration</p>
        </div>
      </div>

      <div className="card">
        <h2>Get Started</h2>
        <p>Choose your direction:</p>
        <div style={{ display: 'flex', gap: '10px', marginTop: '15px' }}>
          <button className="btn" onClick={() => navigate('/checklists/new')}>
            🇲🇼 I'm Malawian → Expanding to Zambia
          </button>
          <button className="btn" onClick={() => navigate('/checklists/new')}>
            🇿🇲 I'm Zambian → Expanding to Malawi
          </button>
        </div>
      </div>

      <div className="card">
        <h2>AI-Powered Analysis</h2>
        <p>
          Upload your business documents and our AI (powered by Ollama, running locally)
          will analyze them for compliance issues across both countries.
        </p>
        <p style={{ marginTop: '10px', color: '#666' }}>
          🔒 Your data stays on your machine - no external API calls
        </p>
      </div>
    </div>
  )
}

export default Home
