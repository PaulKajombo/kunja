import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import NewChecklist from './pages/NewChecklist'
import ChecklistFlow from './pages/ChecklistFlow'
import Results from './pages/Results'
import NewJourney from './pages/NewJourney'
import JourneyView from './pages/JourneyView'

function App() {
  return (
    <Router>
      <div className="app-container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/checklists/new" element={<NewChecklist />} />
          <Route path="/checklists/:id" element={<ChecklistFlow />} />
          <Route path="/checklists/:id/results" element={<Results />} />
          <Route path="/journeys/new" element={<NewJourney />} />
          <Route path="/journeys/:id" element={<JourneyView />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
