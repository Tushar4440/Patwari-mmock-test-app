import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Zap, BookMarked, BarChart3, User as UserIcon, Calendar, ArrowRight, Star } from 'lucide-react';
import './pages.css';

const Home: React.FC = () => {
    const [username, setUsername] = useState('');
    const [targetExam, setTargetExam] = useState('');

    useEffect(() => {
        setUsername(localStorage.getItem('uksssc_username') || 'Aspirant');
        setTargetExam(localStorage.getItem('uksssc_target_exam') || 'UKSSSC VDO/Patwari');
    }, []);

    const handleLogout = () => {
        localStorage.removeItem('uksssc_username');
        localStorage.removeItem('uksssc_user_id');
        window.dispatchEvent(new Event('storage'));
    };

    return (
        <div className="container animate-fade-in">
            <div className="dashboard-header" style={{ marginBottom: '3rem' }}>
                <div>
                    <h1 className="page-title">नमस्ते, <span className="gradient-text">{username}</span></h1>
                    <p className="page-subtitle">Your personalized preparation hub for {targetExam}.</p>
                </div>
                <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
                    <div className="glass-panel" style={{ padding: '0.75rem 1.5rem', display: 'flex', alignItems: 'center', gap: '0.75rem', border: '1px solid var(--accent-primary-op)' }}>
                        <Calendar size={18} className="gradient-text" />
                        <span style={{ fontSize: '0.9rem', fontWeight: 600 }}>Exam Date: May 17, 2026</span>
                    </div>
                    <button
                        onClick={handleLogout}
                        className="btn"
                        style={{ background: 'rgba(239, 68, 68, 0.1)', border: '1px solid rgba(239, 68, 68, 0.2)', color: 'var(--accent-error)', padding: '0.6rem 1.2rem', borderRadius: 'var(--radius-md)', fontSize: '0.9rem', fontWeight: 500, cursor: 'pointer' }}
                    >
                        Logout
                    </button>
                </div>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '2rem', marginBottom: '3rem' }}>
                {/* Primary Action Card */}
                <div className="glass-panel" style={{ padding: '2rem', background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(168, 85, 247, 0.1))', border: '1px solid rgba(99, 102, 241, 0.2)', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
                    <div>
                        <h2 style={{ fontSize: '1.5rem', marginBottom: '1rem' }}>Ready for a <span className="gradient-text">New Challenge?</span></h2>
                        <p style={{ color: 'var(--text-muted)', lineHeight: '1.6', marginBottom: '2rem' }}>
                            Generate a fresh AI mock test tailored to your syllabus and difficulty level.
                        </p>
                    </div>
                    <Link to="/generate" className="btn btn-primary" style={{ width: 'fit-content', padding: '0.8rem 2rem' }}>
                        Generate Mock Test <Zap size={18} style={{ marginLeft: '0.5rem' }} />
                    </Link>
                </div>

                {/* Secondary Feature Card */}
                <div className="glass-panel" style={{ padding: '2rem', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
                    <div>
                        <h2 style={{ fontSize: '1.5rem', marginBottom: '1rem' }}>Verified <span className="gradient-text">Question Bank</span></h2>
                        <p style={{ color: 'var(--text-muted)', lineHeight: '1.6', marginBottom: '2rem' }}>
                            Practice with 100% authentic questions extracted from previous UKSSSC exams.
                        </p>
                    </div>
                    <Link to="/extracted" className="btn btn-outline" style={{ width: 'fit-content' }}>
                        Browse Bank <BookMarked size={18} style={{ marginLeft: '0.5rem' }} />
                    </Link>
                </div>
            </div>

            <h2 className="section-title" style={{ marginBottom: '1.5rem' }}>Quick <span className="gradient-text">Access</span></h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1.5rem' }}>
                <Link to="/dashboard" className="glass-panel stat-card" style={{ textDecoration: 'none', transition: 'transform 0.2s' }}>
                    <div className="stat-icon" style={{ background: 'rgba(16, 185, 129, 0.1)', color: 'var(--accent-success)' }}>
                        <BarChart3 size={24} />
                    </div>
                    <div className="stat-info">
                        <h3 style={{ fontSize: '1.1rem' }}>Analytics</h3>
                        <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Detailed performance tracking</p>
                    </div>
                    <ArrowRight size={16} style={{ marginLeft: 'auto', color: 'var(--text-muted)' }} />
                </Link>

                <Link to="/profile" className="glass-panel stat-card" style={{ textDecoration: 'none', transition: 'transform 0.2s' }}>
                    <div className="stat-icon" style={{ background: 'rgba(245, 158, 11, 0.1)', color: 'var(--accent-warning)' }}>
                        <UserIcon size={24} />
                    </div>
                    <div className="stat-info">
                        <h3 style={{ fontSize: '1.1rem' }}>Settings</h3>
                        <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Manage your exam preferences</p>
                    </div>
                    <ArrowRight size={16} style={{ marginLeft: 'auto', color: 'var(--text-muted)' }} />
                </Link>
            </div>

            <div className="glass-panel" style={{ marginTop: '3rem', padding: '1.5rem', textAlign: 'center', background: 'rgba(255, 255, 255, 0.02)' }}>
                <p style={{ fontSize: '0.9rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}>
                    <Star size={14} className="text-amber" />
                    Tip: Try subject-specific tests if you're struggling with Uttarakhand GK.
                </p>
            </div>
        </div>
    );
};

export default Home;