import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { User, Calendar, Save, CheckCircle, LogOut } from 'lucide-react';
import API_BASE_URL from '../apiConfig';
import './pages.css';

interface HistoryItem {
  total: number;
  percentage: number;
}

interface AnalyticsData {
  history: HistoryItem[];
}

const Profile: React.FC = () => {
  const [analytics, setAnalytics] = useState<AnalyticsData | null>(null);
  const [name, setName] = useState(() => localStorage.getItem('uksssc_username') || 'Aspirant');
  const [saved, setSaved] = useState(false);
  const [targetExam, setTargetExam] = useState(() => localStorage.getItem('uksssc_target_exam') || 'UKSSSC VDO/Patwari');
  const [phone, setPhone] = useState(() => localStorage.getItem('uksssc_phone') || '');
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

    const handleStorageChange = () => {
      const savedName = localStorage.getItem('uksssc_username');
      if (savedName) setName(savedName);
      const savedExam = localStorage.getItem('uksssc_target_exam');
      if (savedExam) setTargetExam(savedExam);
      const savedPhone = localStorage.getItem('uksssc_phone');
      if (savedPhone) setPhone(savedPhone);
    };

    window.addEventListener('storage', handleStorageChange);
    return () => window.removeEventListener('storage', handleStorageChange);
  }, []);

  const handleSave = () => {
    localStorage.setItem('uksssc_username', name);
    localStorage.setItem('uksssc_phone', phone);
    localStorage.setItem('uksssc_target_exam', targetExam);
    setSaved(true);
    setTimeout(() => setSaved(false), 3000);
    // Dispatch event so other components update
    window.dispatchEvent(new Event('storage'));
  };

  const handleLogout = () => {
    localStorage.removeItem('uksssc_username');
    localStorage.removeItem('uksssc_user_id');
    localStorage.removeItem('uksssc_phone');
    localStorage.removeItem('uksssc_target_exam');
    window.dispatchEvent(new Event('storage'));
    navigate('/');
  };

  const historyData = analytics?.history || [];
  const totalTests = historyData.length;
  const totalQuestions = historyData.reduce((acc: number, curr: HistoryItem) => acc + curr.total, 0);
  const avgScore = totalTests > 0
    ? (historyData.reduce((acc: number, curr: HistoryItem) => acc + curr.percentage, 0) / totalTests).toFixed(1)
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
          <label className="input-label" htmlFor="profile-name">Display Name</label>
          <input
            id="profile-name"
            type="text"
            className="select-field"
            value={name}
            onChange={(e) => setName(e.target.value)}
            title="Display Name"
            placeholder="Enter your display name"
            style={{ width: '100%', background: 'var(--bg-elevated)', border: '1px solid var(--border-color)', color: 'var(--text-primary)', padding: '0.75rem', borderRadius: 'var(--radius-md)' }}
          />
        </div>

        <div className="input-group" style={{ marginTop: '1.5rem' }}>
          <label className="input-label" htmlFor="profile-phone">Phone Number</label>
          <input
            id="profile-phone"
            type="tel"
            className="select-field"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
            title="Phone Number"
            placeholder="Enter your phone number"
            style={{ width: '100%', background: 'var(--bg-elevated)', border: '1px solid var(--border-color)', color: 'var(--text-primary)', padding: '0.75rem', borderRadius: 'var(--radius-md)' }}
          />
        </div>

        <div className="input-group" style={{ marginTop: '1.5rem' }}>
          <label className="input-label" htmlFor="profile-target-exam">Target Exam</label>
          <select
            id="profile-target-exam"
            className="select-field"
            value={targetExam}
            onChange={(e) => setTargetExam(e.target.value)}
            title="Target Exam"
            style={{ width: '100%', background: 'var(--bg-elevated)', border: '1px solid var(--border-color)', color: 'var(--text-primary)', padding: '0.75rem', borderRadius: 'var(--radius-md)' }}
          >
            <option value="UKSSSC VDO/Patwari">UKSSSC VDO/Patwari</option>
            <option value="UKPSC Group C">UKPSC Group C</option>
            <option value="Other State Exams">Other State Exams</option>
          </select>
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

        <button
          className="btn"
          onClick={handleLogout}
          style={{ marginTop: '1.5rem', marginLeft: '1rem', background: 'rgba(239, 68, 68, 0.1)', color: 'var(--accent-error)', border: '1px solid rgba(239, 68, 68, 0.2)' }}
        >
          <LogOut size={18} style={{ marginRight: '0.5rem' }} /> Logout
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
