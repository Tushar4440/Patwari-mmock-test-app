import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { User, Calendar, Save, CheckCircle, LogOut } from 'lucide-react';
import API_BASE_URL from '../apiConfig';
import './pages.css';

const Profile: React.FC = () => {
  const [analytics, setAnalytics] = useState<any>(null);
  const [name, setName] = useState('Aspirant');
  const [saved, setSaved] = useState(false);
  const [targetExam, setTargetExam] = useState('UKSSSC VDO/Patwari');
  const navigate = useNavigate();

  useEffect(() => {
    const userId = localStorage.getItem('uksssc_user_id') || '1';

    axios.get(`${API_BASE_URL}/analytics/${userId}`)
      .then(res => {
        setAnalytics(res.data);
      })
      .catch(err => {
        console.error("Failed to fetch analytics", err);
      });

    const savedName = localStorage.getItem('uksssc_username');
    if (savedName) setName(savedName);
    const savedExam = localStorage.getItem('uksssc_target_exam');
    if (savedExam) setTargetExam(savedExam);
  }, []);

  const handleSave = () => {
    localStorage.setItem('uksssc_username', name);
    setSaved(true);
    setTimeout(() => setSaved(false), 3000);
    // Dispatch event so other components update
    window.dispatchEvent(new Event('storage'));
  };

  const handleLogout = () => {
    localStorage.removeItem('uksssc_username');
    localStorage.removeItem('uksssc_user_id');
    window.dispatchEvent(new Event('storage'));
    navigate('/');
  };

  const historyData = analytics?.history || [];
  const totalTests = historyData.length;
  const totalQuestions = historyData.reduce((acc: number, curr: any) => acc + curr.total, 0);
  const avgScore = totalTests > 0
    ? (historyData.reduce((acc: number, curr: any) => acc + curr.percentage, 0) / totalTests).toFixed(1)
    : 0;

  return (
    <div className="container animate-fade-in" style={{ maxWidth: '800px' }}>
      <div className="dashboard-header">
        <div>
          <h1 className="page-title">User <span className="gradient-text">Profile</span></h1>
          <p className="page-subtitle">Manage your settings and view lifetime statistics.</p>
        </div>
      </div>

      <div className="glass-panel" style={{ marginBottom: '2rem' }}>
        <h2 className="section-title" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <User className="gradient-text" /> Personal Details
        </h2>

        <div className="input-group" style={{ marginTop: '1.5rem' }}>
          <label className="input-label">Display Name</label>
          <input
            type="text"
            className="select-field"
            value={name}
            onChange={(e) => setName(e.target.value)}
            style={{ width: '100%', background: 'var(--bg-elevated)', border: '1px solid var(--border-color)', color: 'var(--text-primary)', padding: '0.75rem', borderRadius: 'var(--radius-md)' }}
          />
        </div>

        <div className="input-group" style={{ marginTop: '1.5rem' }}>
          <label className="input-label">Target Exam Date</label>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', background: 'var(--bg-elevated)', padding: '0.75rem', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-color)', color: 'var(--text-muted)' }}>
            <Calendar size={18} />
            May 17, 2026 (UKSSSC VDO/Patwari)
          </div>
        </div>

        <button
          className="btn btn-primary"
          onClick={handleSave}
          style={{ marginTop: '1.5rem' }}
        >
          {saved ? <><CheckCircle size={18} /> Saved!</> : <><Save size={18} /> Save Changes</>}
        </button>
      </div>

      <div className="glass-panel">
        <h2 className="section-title">Lifetime Statistics</h2>

        <div className="stats-grid" style={{ marginTop: '1.5rem' }}>
          <div className="stat-card" style={{ background: 'var(--bg-elevated)' }}>
            <div className="stat-info" style={{ textAlign: 'center', width: '100%' }}>
              <h3>Total Tests Taken</h3>
              <p className="stat-value">{totalTests}</p>
            </div>
          </div>
          <div className="stat-card" style={{ background: 'var(--bg-elevated)' }}>
            <div className="stat-info" style={{ textAlign: 'center', width: '100%' }}>
              <h3>Questions Attempted</h3>
              <p className="stat-value">{totalQuestions}</p>
            </div>
          </div>
          <div className="stat-card" style={{ background: 'var(--bg-elevated)' }}>
            <div className="stat-info" style={{ textAlign: 'center', width: '100%' }}>
              <h3>Average Score</h3>
              <p className="stat-value">{avgScore}%</p>
            </div>
          </div>
        </div>
      </div>

      <div style={{ position: 'fixed', bottom: '5%', left: '2%', opacity: 0.07, pointerEvents: 'none', zIndex: 9999, userSelect: 'none', fontSize: '3.5rem', fontWeight: 900, color: 'var(--text-primary)', whiteSpace: 'nowrap', transform: 'rotate(-15deg)', fontStyle: 'italic' }}>
        © 2026 MadeByTusharTewari
      </div>
    </div>
  );
};

export default Profile;
