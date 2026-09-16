import { useNavigate } from 'react-router-dom'

export default function Landing() {
  const navigate = useNavigate()

  return (
    <div className="landing-page">
      {/* Hero */}
      <section className="landing-hero">
        <nav className="landing-nav" style={{ position: 'absolute', top: 0, left: 0, right: 0 }}>
          <div className="landing-nav-brand" style={{ color: 'white' }}>Kunja</div>
          <div style={{ display: 'flex', gap: 8 }}>
            <button
              className="btn-ghost"
              style={{ color: 'white' }}
              onClick={() => navigate('/register')}
            >
              Create account
            </button>
            <button
              className="btn-ghost"
              style={{ color: 'white' }}
              onClick={() => navigate('/login')}
            >
              Sign in
            </button>
          </div>
        </nav>

        <div className="landing-hero-content">
          <div className="landing-hero-flags">
            <span>🇲🇼</span>
            <span style={{ fontSize: '1.8rem', opacity: 0.5, alignSelf: 'center' }}>→</span>
            <span>🇿🇲</span>
          </div>

          <h1>Expand across Africa with clarity</h1>

          <p>
            Kunja guides businesses through every registration, trade requirement,
            document, and compliance step needed to enter new African markets.
            One clear path from where you are to where you want to be.
          </p>

          <div className="landing-cta-group">
            <button
              className="landing-cta-primary"
              onClick={() => navigate('/journeys/new')}
            >
              Start your market journey
            </button>
            <button
              className="landing-cta-secondary"
              onClick={() => navigate('/dashboard')}
            >
              Explore markets
            </button>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="landing-sections">
        <h2 className="landing-section-title">How Kunja works</h2>
        <p className="landing-section-subtitle">
          Tell us where you want to go. We map every step.
        </p>

        <div className="landing-features-grid">
          <div className="landing-feature">
            <div className="landing-feature-icon">🗺️</div>
            <h3>Tell us your plan</h3>
            <p>
              Your origin country, industry, and how you want to enter
              the target market. Takes less than two minutes.
            </p>
          </div>

          <div className="landing-feature">
            <div className="landing-feature-icon">📍</div>
            <h3>We map the path</h3>
            <p>
              Every step from home-country readiness through trade
              compliance to target-country operations, in the right order.
            </p>
          </div>

          <div className="landing-feature">
            <div className="landing-feature-icon">✅</div>
            <h3>Follow the roadmap</h3>
            <p>
              Track progress, mark steps complete, see what's next.
              Know exactly where you stand at every moment.
            </p>
          </div>

          <div className="landing-feature">
            <div className="landing-feature-icon">💬</div>
            <h3>Ask Kunja anything</h3>
            <p>
              AI-powered answers grounded in your actual journey context,
              relevant regulations, and authoritative sources.
            </p>
          </div>
        </div>
      </section>

      {/* Countries */}
      <section className="landing-sections" style={{ paddingTop: 0 }}>
        <h2 className="landing-section-title">Cross-border market entry</h2>
        <p className="landing-section-subtitle">
          Currently supporting the Malawi–Zambia corridor, with more markets coming soon.
        </p>

        <div style={{ display: 'flex', gap: '24px', justifyContent: 'center', flexWrap: 'wrap' }}>
          <div className="landing-feature" style={{ flex: '1 1 200px', maxWidth: '300px', textAlign: 'center' }}>
            <div style={{ fontSize: '3rem', marginBottom: '8px' }}>🇲🇼</div>
            <h3>From Malawi</h3>
            <p>Company readiness, export permits, SADC trade compliance</p>
          </div>
          <div className="landing-feature" style={{ flex: '1 1 200px', maxWidth: '300px', textAlign: 'center' }}>
            <div style={{ fontSize: '3rem', marginBottom: '8px' }}>↔️</div>
            <h3>Cross-Border</h3>
            <p>Certificates of origin, customs clearance, product standards</p>
          </div>
          <div className="landing-feature" style={{ flex: '1 1 200px', maxWidth: '300px', textAlign: 'center' }}>
            <div style={{ fontSize: '3rem', marginBottom: '8px' }}>🇿🇲</div>
            <h3>Into Zambia</h3>
            <p>PACRA registration, ZRA tax, business permits, operations</p>
          </div>
        </div>
      </section>

      <footer className="landing-footer">
        Kunja &mdash; Your guide to entering African markets
      </footer>
    </div>
  )
}
