import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Landing from './pages/Landing'
import Dashboard from './pages/Dashboard'
import JourneyNew from './pages/JourneyNew'
import JourneyView from './pages/JourneyView'
import Documents from './pages/Documents'
import Assistant from './pages/Assistant'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route element={<Layout />}>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/journeys/new" element={<JourneyNew />} />
          <Route path="/journeys/:id" element={<JourneyView />} />
          <Route path="/documents" element={<Documents />} />
          <Route path="/assistant" element={<Assistant />} />
        </Route>
      </Routes>
    </Router>
  )
}

export default App
