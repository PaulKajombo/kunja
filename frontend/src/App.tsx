import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { AuthProvider } from './hooks/useAuth'
import ErrorBoundary from './components/ErrorBoundary'
import Layout from './components/Layout'
import RequireAuth from './components/RequireAuth'
import Landing from './pages/Landing'
import Login from './pages/Login'
import Register from './pages/Register'
import Dashboard from './pages/Dashboard'
import JourneyNew from './pages/JourneyNew'
import JourneyView from './pages/JourneyView'
import Documents from './pages/Documents'
import Assistant from './pages/Assistant'

function App() {
  return (
    <AuthProvider>
      <ErrorBoundary>
        <Router>
          <Routes>
            <Route path="/" element={<Landing />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route element={<RequireAuth />}>
              <Route element={<Layout />}>
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/journeys/new" element={<JourneyNew />} />
                <Route path="/journeys/:id" element={<JourneyView />} />
                <Route path="/documents" element={<Documents />} />
                <Route path="/assistant" element={<Assistant />} />
              </Route>
            </Route>
          </Routes>
        </Router>
      </ErrorBoundary>
    </AuthProvider>
  )
}

export default App