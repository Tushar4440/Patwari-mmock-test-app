import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { Settings, Zap } from 'lucide-react';
import API_BASE_URL from '../apiConfig';
import './pages.css';

const TestGenerator: React.FC = () => {
  const navigate = useNavigate();
  const [section, setSection] = useState('full');
  const [generating, setGenerating] = useState(false);
  const [loadingTextIndex, setLoadingTextIndex] = useState(0);

  const loadingTexts = [
    "Analyzing UKSSSC Syllabus...",
    "Formulating highly difficult questions...",
    "Translating questions to Hindi...",
    "Writing detailed explanations...",
    "Finalizing mock test..."
  ];

  useEffect(() => {
    let interval: any;
    if (generating) {
      interval = setInterval(() => {
        setLoadingTextIndex((prev) => (prev + 1) % loadingTexts.length);
      }, 2500);
    } else {
      setLoadingTextIndex(0);
    }
    return () => clearInterval(interval);
  }, [generating]);

  const handleGenerate = async () => {
    setGenerating(true);
    try {
      const payload = {
        syllabus_text: 'UKSSSC VDO/Patwari Syllabus 2026', // Hardcoded predefined syllabus
        section: section,
        title: `Mock Test - ${section === 'full' ? 'Full Length' : section}`
      };

      const res = await axios.post(`${API_BASE_URL}/generate_test`, payload);

      setGenerating(false);
      navigate(`/test/${res.data.test_id}`);
    } catch (err) {
      console.error('Error generating test', err);
      setGenerating(false);
      alert('Failed to generate test. Make sure backend is running.');
    }
  };

  return (
    <div className="container animate-fade-in">
      <div className="dashboard-header">
        <div>
          <h1 className="page-title">Generate <span className="gradient-text">Mock Test</span></h1>
          <p className="page-subtitle">Configure your mock test settings to begin your practice.</p>
        </div>
      </div>

      <div className="glass-panel" style={{ maxWidth: '600px', margin: '0 auto' }}>
        <h2 className="section-title" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <Settings className="gradient-text" /> Test Configuration
        </h2>

        <div className="input-group" style={{ marginTop: '2rem' }}>
          <label className="input-label">Select Subject/Section</label>
          <div style={{ position: 'relative' }}>
            <select
              className="select-field"
              value={section}
              onChange={(e) => setSection(e.target.value)}
            >
              <option value="full">Full Length Mock Test (All Sections)</option>
              <option value="General Hindi">General Hindi</option>
              <option value="General Knowledge">General Knowledge</option>
              <option value="Uttarakhand GK">Uttarakhand GK</option>
            </select>
          </div>
        </div>

        <div className="input-group">
          <label className="input-label">Difficulty Level</label>
          <select className="select-field" disabled>
            <option>Hard (Memory Based)</option>
          </select>
          <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginTop: '0.5rem' }}>
            * UKSSSC exams are typically high difficulty
          </p>
        </div>

        {generating ? (
          <div style={{ textAlign: 'center', padding: '2rem 0', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1rem', background: 'rgba(99, 102, 241, 0.05)', borderRadius: 'var(--radius-md)', marginTop: '2rem', border: '1px solid rgba(99, 102, 241, 0.2)' }}>
            <style>{`
              @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
            `}</style>
            <div style={{ width: '40px', height: '40px', border: '3px solid rgba(99, 102, 241, 0.2)', borderTopColor: 'var(--accent-primary)', borderRadius: '50%', animation: 'spin 1s linear infinite' }}></div>
            <div>
              <p style={{ color: 'var(--accent-primary)', fontWeight: 600, fontSize: '1.1rem' }}>
                {loadingTexts[loadingTextIndex]}
              </p>
              <p style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginTop: '0.5rem' }}>This takes about 10-15 seconds...</p>
            </div>
          </div>
        ) : (
          <button
            className="btn btn-primary"
            style={{ width: '100%', marginTop: '1rem', padding: '1rem' }}
            onClick={handleGenerate}
          >
            <span style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}>
              <Zap size={20} /> Generate AI Mock Test
            </span>
          </button>
        )}
      </div>

      <div style={{ position: 'fixed', top: '20%', right: '10%', opacity: 0.07, pointerEvents: 'none', zIndex: 9999, userSelect: 'none', fontSize: '3rem', fontWeight: 900, color: 'var(--text-primary)', whiteSpace: 'nowrap', transform: 'rotate(15deg)', fontStyle: 'italic' }}>
        © 2026 MadeByTusharTewari copyright
      </div>
    </div>
  );
};

export default TestGenerator;
