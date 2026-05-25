import { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Navigation from './components/Navigation';
import Dashboard from './pages/Dashboard';
import TestGenerator from './pages/TestGenerator';
import MockTestInterface from './pages/MockTestInterface';
import Profile from './pages/Profile';
import ExtractedTests from './pages/ExtractedTests';
import Auth from './pages/Auth';
import Landing from './pages/Landing';
import Home from './pages/Home';
import './App.css';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem('uksssc_user_id'));

  useEffect(() => {
    const checkAuth = () => {
      setIsAuthenticated(!!localStorage.getItem('uksssc_user_id'));
    };

    window.addEventListener('storage', checkAuth);
    return () => window.removeEventListener('storage', checkAuth);
  }, []);

  return (
    <Router>
      {!isAuthenticated ? (
        <Routes>
          {/* Unauthenticated users see the Landing page or Login */}
          <Route path="/" element={<Landing />} />
          <Route path="/login" element={<Auth />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      ) : (
        <div className="app-container">
          <Navigation />
          <main className="main-content">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/generate" element={<TestGenerator />} />
              <Route path="/test/:id" element={<MockTestInterface />} />
              <Route path="/profile" element={<Profile />} />
              <Route path="/extracted" element={<ExtractedTests />} />
              <Route path="/login" element={<Auth />} />
              {/* Catch-all for logged in users */}
              <Route path="*" element={<Navigate to="/" replace />} />
            </Routes>
          </main>
        </div>
      )}
    </Router>
  );
}

export default App;
