import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { User, Lock, Mail, ArrowRight, LogIn, GraduationCap, Phone } from 'lucide-react';
import './pages.css';

const Auth: React.FC = () => {
    const [isLogin, setIsLogin] = useState(true);
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [phone, setPhone] = useState('');
    const [name, setName] = useState('');
    const [targetExam, setTargetExam] = useState('UKSSSC VDO/Patwari');
    const navigate = useNavigate();

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        // Simulate authentication logic
        const storedUsers = JSON.parse(localStorage.getItem('uksssc_registered_users') || '{}');

        if (!isLogin && password !== confirmPassword) {
            alert("Passwords do not match!");
            return;
        }

        if (!isLogin) {
            if (storedUsers[email]) {
                alert("User already exists with this email!");
                return;
            }

            // Create new user record
            const newUserId = Math.floor(Math.random() * 10000) + 2; // Generate random ID > 1
            const newUser = {
                id: newUserId,
                name: name || 'New User',
                email,
                password, // In real apps, never store plain text passwords
                phone,
                targetExam
            };

            storedUsers[email] = newUser;
            localStorage.setItem('uksssc_registered_users', JSON.stringify(storedUsers));

            // Log them in immediately
            localStorage.setItem('uksssc_username', newUser.name);
            localStorage.setItem('uksssc_user_id', newUser.id.toString());
            localStorage.setItem('uksssc_target_exam', targetExam);
            localStorage.setItem('uksssc_phone', phone);
        } else {
            const user = storedUsers[email];

            if (user && user.password === password) {
                localStorage.setItem('uksssc_username', user.name);
                localStorage.setItem('uksssc_user_id', user.id.toString());
                localStorage.setItem('uksssc_target_exam', user.targetExam || 'UKSSSC VDO/Patwari');
                localStorage.setItem('uksssc_phone', user.phone || '');
            } else {
                alert("Invalid email or password!");
                return;
            }
        }

        // Dispatch storage event so other components (Dashboard, Profile) detect the change
        window.dispatchEvent(new Event('storage'));

        // Navigate to dashboard
        navigate('/');
    };

    return (
        <div className="container animate-fade-in" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '80vh' }}>
            <div className="glass-panel" style={{ width: '100%', maxWidth: '450px', padding: '2.5rem', position: 'relative' }}>

                <div style={{ textAlign: 'center', marginBottom: '1.5rem' }}>
                    <h2 style={{ fontSize: '0.9rem', color: 'var(--accent-primary)', textTransform: 'uppercase', letterSpacing: '0.25em', fontWeight: 800 }}>Tushar Classes</h2>
                    <div style={{ width: '40px', height: '2px', background: 'var(--accent-primary)', margin: '0.5rem auto 0' }}></div>
                </div>

                <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                    <h1 className="page-title" style={{ fontSize: '2rem' }}>
                        {isLogin ? 'Welcome ' : 'Join '}
                        <span className="gradient-text">{isLogin ? 'Back' : 'Us'}</span>
                    </h1>
                    <p className="page-subtitle">
                        {isLogin ? 'Enter your credentials to continue' : 'Create an account to track your journey'}
                    </p>
                </div>

                <form onSubmit={handleSubmit}>
                    {!isLogin && (
                        <div className="input-group">
                            <label className="input-label">Full Name</label>
                            <div style={{ position: 'relative' }}>
                                <User size={18} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
                                <input
                                    type="text"
                                    className="select-field"
                                    placeholder="John Doe"
                                    value={name}
                                    onChange={(e) => setName(e.target.value)}
                                    style={{ paddingLeft: '2.5rem', width: '100%', background: 'var(--bg-elevated)', border: '1px solid var(--border-color)', color: 'var(--text-primary)', borderRadius: 'var(--radius-md)' }}
                                    required
                                />
                            </div>
                        </div>
                    )}

                    <div className="input-group">
                        <label className="input-label">Email Address</label>
                        <div style={{ position: 'relative' }}>
                            <Mail size={18} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
                            <input
                                type="email"
                                className="select-field"
                                placeholder="name@example.com"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                style={{ paddingLeft: '2.5rem', width: '100%', background: 'var(--bg-elevated)', border: '1px solid var(--border-color)', color: 'var(--text-primary)', borderRadius: 'var(--radius-md)' }}
                                required
                            />
                        </div>
                    </div>

                    {!isLogin && (
                        <div className="input-group">
                            <label className="input-label">Phone Number</label>
                            <div style={{ position: 'relative' }}>
                                <Phone size={18} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
                                <input
                                    type="tel"
                                    className="select-field"
                                    placeholder="+91 00000 00000"
                                    value={phone}
                                    onChange={(e) => setPhone(e.target.value)}
                                    style={{ paddingLeft: '2.5rem', width: '100%', background: 'var(--bg-elevated)', border: '1px solid var(--border-color)', color: 'var(--text-primary)', borderRadius: 'var(--radius-md)' }}
                                    required
                                />
                            </div>
                        </div>
                    )}

                    <div className="input-group">
                        <label className="input-label">Password</label>
                        <div style={{ position: 'relative', marginBottom: !isLogin ? '1rem' : '0' }}>
                            <Lock size={18} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
                            <input
                                type="password"
                                className="select-field"
                                placeholder="••••••••"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                style={{ paddingLeft: '2.5rem', width: '100%', background: 'var(--bg-elevated)', border: '1px solid var(--border-color)', color: 'var(--text-primary)', borderRadius: 'var(--radius-md)' }}
                                required
                            />
                        </div>
                    </div>

                    {!isLogin && (
                        <>
                            <div className="input-group">
                                <label className="input-label">Confirm Password</label>
                                <div style={{ position: 'relative' }}>
                                    <Lock size={18} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
                                    <input
                                        type="password"
                                        className="select-field"
                                        placeholder="••••••••"
                                        value={confirmPassword}
                                        onChange={(e) => setConfirmPassword(e.target.value)}
                                        style={{ paddingLeft: '2.5rem', width: '100%', background: 'var(--bg-elevated)', border: '1px solid var(--border-color)', color: 'var(--text-primary)', borderRadius: 'var(--radius-md)' }}
                                        required
                                    />
                                </div>
                            </div>

                            <div className="input-group">
                                <label htmlFor="auth-target-exam" className="input-label">Target Exam</label>
                                <div style={{ position: 'relative' }}>
                                    <GraduationCap size={18} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
                                    <select
                                        id="auth-target-exam"
                                        title="Target Exam"
                                        className="select-field"
                                        value={targetExam}
                                        onChange={(e) => setTargetExam(e.target.value)}
                                        style={{ paddingLeft: '2.5rem', width: '100%', background: 'var(--bg-elevated)', border: '1px solid var(--border-color)', color: 'var(--text-primary)', borderRadius: 'var(--radius-md)' }}
                                    >
                                        <option value="UKSSSC VDO/Patwari">UKSSSC VDO/Patwari</option>
                                        <option value="UKPSC Group C">UKPSC Group C</option>
                                        <option value="Other State Exams">Other State Exams</option>
                                    </select>
                                </div>
                            </div>
                        </>
                    )}

                    <button type="submit" className="btn btn-primary" style={{ width: '100%', marginTop: '1rem', padding: '0.8rem' }}>
                        {isLogin ? (
                            <span style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}>
                                Login <LogIn size={18} />
                            </span>
                        ) : (
                            <span style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}>
                                Create Account <ArrowRight size={18} />
                            </span>
                        )}
                    </button>
                </form>

                <div style={{ marginTop: '2rem', textAlign: 'center', fontSize: '0.9rem', color: 'var(--text-muted)' }}>
                    {isLogin ? "Don't have an account?" : "Already have an account?"}
                    <button
                        style={{ background: 'none', border: 'none', fontWeight: 600, marginLeft: '0.5rem', cursor: 'pointer', padding: 0, font: 'inherit' }}
                        onClick={() => setIsLogin(!isLogin)}
                    >
                        <span className="gradient-text">{isLogin ? 'Register Here' : 'Log In'}</span>
                    </button>
                </div>
            </div>

            <div className="app-watermark">
                Tushar-Classes-2026
            </div>
        </div>
    );
};

export default Auth;