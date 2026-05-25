import React from 'react';
import { Link } from 'react-router-dom';
import { ShieldCheck, Zap, BookMarked, Target, Clock, GraduationCap, ChevronRight } from 'lucide-react';
import './pages.css';

const Landing: React.FC = () => {
    return (
        <div className="container animate-fade-in" style={{ padding: '4rem 1rem' }}>
            <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
                <h2 style={{ fontSize: '1.25rem', color: 'var(--accent-primary)', textTransform: 'uppercase', letterSpacing: '0.4em', fontWeight: 900 }}>Tushar Classes</h2>
                <div style={{ width: '60px', height: '4px', background: 'var(--accent-primary)', margin: '0.75rem auto 0', borderRadius: '2px' }}></div>
            </div>

            <div style={{ textAlign: 'center', marginBottom: '4rem' }}>
                <div className="extracted-hero-badge" style={{ margin: '0 auto' }}>
                    <ShieldCheck size={16} />
                    <span>Authorized Prep Platform for UKSSSC 2026</span>
                </div>
                <h1 className="page-title" style={{ fontSize: '3.5rem', marginTop: '1.5rem' }}>
                    Master the <span className="gradient-text">VDO/Patwari</span> Exam
                </h1>
                <p className="page-subtitle" style={{ maxWidth: '700px', margin: '1rem auto', fontSize: '1.1rem' }}>
                    The most advanced AI-powered mock test platform specifically designed for the Uttarakhand
                    Subordinate Service Selection Commission (UKSSSC) aspirants.
                </p>
                <Link to="/login" className="btn btn-primary" style={{ padding: '1rem 2.5rem', fontSize: '1.1rem', marginTop: '2rem' }}>
                    Login to Start Mock Test <ChevronRight size={20} />
                </Link>
            </div>

            <div className="stats-grid" style={{ marginBottom: '4rem' }}>
                <div className="glass-panel stat-card" style={{ flexDirection: 'column', alignItems: 'flex-start', gap: '1rem' }}>
                    <div style={{ background: 'rgba(99, 102, 241, 0.1)', color: 'var(--accent-primary)', padding: '0.8rem', borderRadius: '12px' }}>
                        <Zap size={24} />
                    </div>
                    <h3 style={{ color: 'var(--text-primary)', margin: 0 }}>AI-Generated Tests</h3>
                    <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', lineHeight: '1.5' }}>
                        Unlimited dynamic mock tests based on the latest 2026 syllabus and difficulty trends.
                    </p>
                </div>
                <div className="glass-panel stat-card" style={{ flexDirection: 'column', alignItems: 'flex-start', gap: '1rem' }}>
                    <div style={{ background: 'rgba(16, 185, 129, 0.1)', color: 'var(--accent-success)', padding: '0.8rem', borderRadius: '12px' }}>
                        <BookMarked size={24} />
                    </div>
                    <h3 style={{ color: 'var(--text-primary)', margin: 0 }}>100% Hindi Devanagari</h3>
                    <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', lineHeight: '1.5' }}>
                        All questions and detailed explanations are provided in the official exam medium.
                    </p>
                </div>
                <div className="glass-panel stat-card" style={{ flexDirection: 'column', alignItems: 'flex-start', gap: '1rem' }}>
                    <div style={{ background: 'rgba(245, 158, 11, 0.1)', color: 'var(--accent-warning)', padding: '0.8rem', borderRadius: '12px' }}>
                        <Target size={24} />
                    </div>
                    <h3 style={{ color: 'var(--text-primary)', margin: 0 }}>Verified UK GK</h3>
                    <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', lineHeight: '1.5' }}>
                        Authentic Uttarakhand-specific questions curated from previous years' official papers.
                    </p>
                </div>
            </div>

            <div className="glass-panel" style={{ padding: '3rem' }}>
                <div style={{ textAlign: 'center', marginBottom: '2.5rem' }}>
                    <h2 className="section-title" style={{ fontSize: '1.8rem' }}>Exam <span className="gradient-text">Pattern & Details</span></h2>
                    <p className="text-muted">Target Date: May 17, 2026 (Expected)</p>
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '2rem' }}>
                    <div style={{ textAlign: 'center' }}>
                        <Clock size={32} style={{ color: 'var(--accent-primary)', marginBottom: '1rem' }} />
                        <h4 style={{ color: 'var(--text-primary)', marginBottom: '0.5rem' }}>120 Minutes</h4>
                        <p className="text-muted" style={{ fontSize: '0.85rem' }}>Full-length duration to build time-management skills.</p>
                    </div>
                    <div style={{ textAlign: 'center' }}>
                        <GraduationCap size={32} style={{ color: 'var(--accent-success)', marginBottom: '1rem' }} />
                        <h4 style={{ color: 'var(--text-primary)', marginBottom: '0.5rem' }}>100 Questions</h4>
                        <p className="text-muted" style={{ fontSize: '0.85rem' }}>Structured according to UKSSSC VDO/Patwari weightage.</p>
                    </div>
                    <div style={{ textAlign: 'center' }}>
                        <ShieldCheck size={32} style={{ color: 'var(--accent-warning)', marginBottom: '1rem' }} />
                        <h4 style={{ color: 'var(--text-primary)', marginBottom: '0.5rem' }}>Negative Marking</h4>
                        <p className="text-muted" style={{ fontSize: '0.85rem' }}>0.25 penalty simulated to ensure accuracy during practice.</p>
                    </div>
                </div>

                <div style={{ marginTop: '3rem', padding: '1.5rem', background: 'rgba(255,255,255,0.03)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-color)' }}>
                    <h4 style={{ color: 'var(--text-primary)', marginBottom: '1rem', textAlign: 'center' }}>Subject Distribution</h4>
                    <div style={{ display: 'flex', justifyContent: 'space-around', flexWrap: 'wrap', gap: '1rem' }}>
                        <div className="section-badge" style={{ padding: '0.6rem 1.2rem' }}>General Hindi (20 Qs)</div>
                        <div className="section-badge" style={{ padding: '0.6rem 1.2rem' }}>General Knowledge (40 Qs)</div>
                        <div className="section-badge" style={{ padding: '0.6rem 1.2rem' }}>Uttarakhand GK (40 Qs)</div>
                    </div>
                </div>
            </div>

            <div style={{ marginTop: '4rem', textAlign: 'center' }}>
                <p style={{ color: 'var(--text-muted)', marginBottom: '1.5rem' }}>Ready to analyze your current preparation level?</p>
                <Link to="/login" className="btn btn-outline" style={{ padding: '0.8rem 2rem' }}>
                    Create Account to Track Scores
                </Link>
            </div>

            <div className="app-watermark">
                Tushar-Classes-2026
            </div>
        </div>
    );
};

export default Landing;