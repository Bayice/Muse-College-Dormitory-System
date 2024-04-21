import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './Login';
import StudentDashboard from './StudentDashboard';
import MentorDashboard from './MentorDashboard';
import ManagerDashboard from './ManagerDashboard';
import SupervisorDashboard from './SupervisorDashboard';
import ResultsPage from './ResultsPage';
import SelectionPage from './SelectionPage';
import SelectionOutput from './SelectionOutput';
import Dom_select from './Dom_select';
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/student" element={<StudentDashboard />} />
        <Route path="/mentor" element={<MentorDashboard />} />
        <Route path="/manager" element={<ManagerDashboard />} />
        <Route path="/supervisor" element={<SupervisorDashboard />} />
        <Route path="/results" element={<ResultsPage />} />
        <Route path="/selection" element={<SelectionPage />} /> 
        <Route path="/selection-output" element={<SelectionOutput />} />
        <Route path="/Dom_select" element={<Dom_select />} />
      </Routes>
    </Router>
  );
}

export default App;
