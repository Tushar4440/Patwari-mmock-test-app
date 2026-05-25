import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import {
  XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
  AreaChart, Area, Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis
} from 'recharts';
import { TrendingUp, Target, Award, Clock, BookMarked, ShieldCheck } from 'lucide-react';
import API_BASE_URL from '../apiConfig';
import './pages.css';

interface HistoryItem {
  attempt_id: number;
  test_id: number;
  score: number;
  total: number;
  percentage: number;
  date: string;
}

interface SectionAccuracyItem {
  section: string;
  accuracy: number;
  fullMark: number;
}

interface AnalyticsData {
  history: HistoryItem[];
  predicted_score: number;
  section_accuracy: SectionAccuracyItem[];
}

const Dashboard: React.FC = () => {
  const [analytics, setAnalytics] = useState<AnalyticsData | null>(null);
  const [loading, setLoading] = useState(true);
  const [username, setUsername] = useState<string | null>(null);

  useEffect(() => {
    const userId = localStorage.getItem('uksssc_user_id') || '1';

    axios.get(`${API_BASE_URL}/analytics/${userId}`)
      .then(res => {
        setAnalytics(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Failed to fetch analytics", err);
        setLoading(false);
      });

    const loadUsername = () => {
      const savedName = localStorage.getItem('uksssc_username');
      setUsername(savedName);
    };

    loadUsername();
    window.addEventListener('storage', loadUsername);
    return () => window.removeEventListener('storage', loadUsername);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('uksssc_username');
    localStorage.removeItem('uksssc_user_id');
    setUsername(null);
    window.dispatchEvent(new Event('storage'));
  };

  if (loading) {
    return <div className="container"><div className="loading-spinner">Loading your progress...</div></div>;
  }

  const historyData = analytics?.history || [];
  const predictedScore = analytics?.predicted_score || 0;
  const sectionAccuracy = analytics?.section_accuracy || [];

  return (
    <div className="container animate-fade-in">
      <div className="dashboard-header">
        <div>
          <h1 className="page-title">
            Welcome back, <span className="gradient-text">{username}</span>
          </h1>
          <p className="page-subtitle">Track your UKSSSC VDO/Patwari exam preparation journey.</p>
        </div>
        <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
          <button
            onClick={handleLogout}
            className="btn"
            style={{ background: 'rgba(239, 68, 68, 0.1)', border: '1px solid rgba(239, 68, 68, 0.2)', color: 'var(--accent-error)', padding: '0.6rem 1.2rem', borderRadius: 'var(--radius-md)', fontSize: '0.9rem', fontWeight: 500, cursor: 'pointer' }}
          >
            Logout
          </button>
          <Link to="/generate" className="btn btn-primary">
            Take New Mock Test
          </Link>
        </div>
      </div>

      <div className="stats-grid">
        <div className="glass-panel stat-card">
          <div className="stat-icon" style={{ background: 'rgba(99, 102, 241, 0.1)', color: 'var(--accent-primary)' }}>
            <Target size={24} />
          </div>
          <div className="stat-info">
            <h3>Predicted Score</h3>
            <p className="stat-value">{predictedScore}%</p>
          </div>
        </div>
        <div className="glass-panel stat-card">
          <div className="stat-icon" style={{ background: 'rgba(16, 185, 129, 0.1)', color: 'var(--accent-success)' }}>
            <Award size={24} />
          </div>
          <div className="stat-info">
            <h3>Tests Completed</h3>
            <p className="stat-value">{historyData.length}</p>
          </div>
        </div>
        <div className="glass-panel stat-card">
          <div className="stat-icon" style={{ background: 'rgba(245, 158, 11, 0.1)', color: 'var(--accent-warning)' }}>
            <TrendingUp size={24} />
          </div>
          <div className="stat-info">
            <h3>Recent Score</h3>
            <p className="stat-value">{historyData.length > 0 ? `${historyData[historyData.length - 1].percentage.toFixed(1)}%` : 'N/A'}</p>
          </div>
        </div>
      </div>

      {/* ── Extracted Tests Promo Banner ── */}
      <div className="extracted-promo-card">
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
          <div style={{ background: 'rgba(245,158,11,0.15)', color: '#f59e0b', padding: '0.75rem', borderRadius: 'var(--radius-lg)', display: 'flex' }}>
            <BookMarked size={28} />
          </div>
          <div className="extracted-promo-text">
            <h3>🎯 Extracted Mock Tests — UK GK Only</h3>
            <p>Practice with real questions sourced from previous UKSSSC exams. <ShieldCheck size={13} style={{ verticalAlign: 'middle', color: 'var(--accent-success)' }} /> No AI content — 100% authentic.</p>
          </div>
        </div>
        <Link to="/extracted" className="btn" style={{ background: 'linear-gradient(135deg, #f59e0b, #ea580c)', color: '#fff', border: 'none', whiteSpace: 'nowrap' }}>
          View Extracted Tests
        </Link>
      </div>

      <div className="charts-container">
        <div className="glass-panel chart-panel">
          <h2 className="section-title">Performance Trend</h2>
          {historyData.length > 0 ? (
            <div className="chart-wrapper">
              <ResponsiveContainer width="100%" height={300}>
                <AreaChart data={historyData}>
                  <defs>
                    <linearGradient id="colorScore" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="var(--accent-primary)" stopOpacity={0.8} />
                      <stop offset="95%" stopColor="var(--accent-primary)" stopOpacity={0} />
                    </linearGradient>
                  </defs>
                  <CartesianGrid strokeDasharray="3 3" stroke="var(--border-color)" vertical={false} />
                  <XAxis dataKey="date" stroke="var(--text-muted)" />
                  <YAxis stroke="var(--text-muted)" />
                  <Tooltip
                    contentStyle={{ backgroundColor: 'var(--bg-elevated)', borderColor: 'var(--border-color)', borderRadius: '8px' }}
                    itemStyle={{ color: 'var(--text-primary)' }}
                  />
                  <Area type="monotone" dataKey="percentage" stroke="var(--accent-primary)" fillOpacity={1} fill="url(#colorScore)" />
                </AreaChart>
              </ResponsiveContainer>
            </div>
          ) : (
            <div className="empty-state">
              <Clock size={48} className="empty-icon" />
              <p>Take your first mock test to see your performance trend.</p>
            </div>
          )}
        </div>

        <div className="glass-panel chart-panel">
          <h2 className="section-title">Subject Mastery (Accuracy)</h2>
          {sectionAccuracy.length > 0 ? (
            <div className="chart-wrapper">
              <ResponsiveContainer width="100%" height={300}>
                <RadarChart cx="50%" cy="50%" outerRadius="70%" data={sectionAccuracy}>
                  <PolarGrid stroke="var(--border-color)" />
                  <PolarAngleAxis dataKey="section" stroke="var(--text-muted)" tick={{ fill: 'var(--text-muted)', fontSize: 12 }} />
                  <PolarRadiusAxis angle={30} domain={[0, 100]} stroke="var(--text-muted)" />
                  <Radar name="Accuracy" dataKey="accuracy" stroke="var(--accent-primary)" fill="var(--accent-primary)" fillOpacity={0.5} />
                  <Tooltip
                    contentStyle={{ backgroundColor: 'var(--bg-elevated)', borderColor: 'var(--border-color)', borderRadius: '8px' }}
                    itemStyle={{ color: 'var(--accent-primary)', fontWeight: 'bold' }}
                  />
                </RadarChart>
              </ResponsiveContainer>
            </div>
          ) : (
            <div className="empty-state">
              <Award size={48} className="empty-icon" />
              <p>Complete tests to see your strong and weak sections.</p>
            </div>
          )}
        </div>
      </div>

      <div className="app-watermark">
        Tushar-Classes-2026
      </div>
    </div>
  );
};

export default Dashboard;
