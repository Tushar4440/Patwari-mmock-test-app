import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import Dashboard from './pages/Dashboard';
import TestGenerator from './pages/TestGenerator';
import MockTestInterface from './pages/MockTestInterface';
import Profile from './pages/Profile';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app-container">
        <Navigation />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/generate" element={<TestGenerator />} />
            <Route path="/test/:id" element={<MockTestInterface />} />
            <Route path="/profile" element={<Profile />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
