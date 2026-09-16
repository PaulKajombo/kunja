import { NavLink, Outlet, useNavigate } from 'react-router-dom'
import { useAuth } from '../hooks/useAuth'

const NAV_ITEMS = [
  { to: '/dashboard', icon: '📊', label: 'Dashboard' },
  { to: '/journeys/new', icon: '🗺️', label: 'Start Journey' },
  { to: '/documents', icon: '📄', label: 'Documents' },
  { to: '/assistant', icon: '💬', label: 'AI Assistant' },
]

export default function Layout() {
  const { user, logout } = useAuth()
  const navigate = useNavigate()

  const handleLogout = () => {
    logout()
    navigate('/login')
  }

  return (
    <div className="app-shell">
      {/* Desktop sidebar */}
      <aside className="app-sidebar">
        <div className="sidebar-brand">
          <h1>Kunja</h1>
          <p>Market Entry Guide</p>
        </div>
        <nav className="sidebar-nav">
          {NAV_ITEMS.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}
            >
              <span className="nav-icon">{item.icon}</span>
              {item.label}
            </NavLink>
          ))}
        </nav>
        <div className="sidebar-user">
          <div className="sidebar-user-initial">
            {(user?.full_name ?? 'U').charAt(0).toUpperCase()}
          </div>
          <div className="sidebar-user-meta">
            <div className="sidebar-user-name">{user?.full_name ?? 'Signed in'}</div>
            <div className="sidebar-user-country">{user?.country ?? 'Kunja user'}</div>
          </div>
          <button className="sidebar-logout" onClick={handleLogout} title="Sign out">
            Logout
          </button>
        </div>
        <div className="sidebar-footer">
          Kunja &copy; 2026
        </div>
      </aside>

      {/* Mobile header */}
      <header className="mobile-header">
        <h1>Kunja</h1>
        <NavLink to="/journeys/new" className="btn" style={{ fontSize: '0.8rem', padding: '6px 14px' }}>
          + New
        </NavLink>
      </header>

      {/* Mobile bottom nav */}
      <nav className="mobile-bottom-nav">
        <div className="mobile-nav-items">
          {NAV_ITEMS.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className={({ isActive }) => `mobile-nav-item ${isActive ? 'active' : ''}`}
            >
              <span className="nav-icon">{item.icon}</span>
              {item.label}
            </NavLink>
          ))}
        </div>
      </nav>

      {/* Main content */}
      <main className="app-main">
        <Outlet />
      </main>
    </div>
  )
}
