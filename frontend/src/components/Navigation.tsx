import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { BookOpen, BarChart2, PlusCircle, User, BookMarked } from 'lucide-react';

const Navigation: React.FC = () => {
  const location = useLocation();

  return (
    <nav className="navbar">
      <div className="container nav-container">
        <Link to="/" className="nav-brand">
          <BookOpen className="gradient-text" />
          <span>UKSSSC <span className="gradient-text">Mock Prep</span></span>
        </Link>
        <div className="nav-links">
          <Link to="/" className={`nav-link ${location.pathname === '/' ? 'active' : ''}`}>
            <BarChart2 size={18} /> Dashboard
          </Link>
          <Link to="/generate" className={`nav-link ${location.pathname === '/generate' ? 'active' : ''}`}>
            <PlusCircle size={18} /> New Test
          </Link>
          <Link
            to="/extracted"
            className={`nav-link nav-link-extracted ${location.pathname === '/extracted' ? 'active' : ''}`}
          >
            <BookMarked size={18} /> Extracted Tests
          </Link>
          <Link to="/profile" className={`nav-link ${location.pathname === '/profile' ? 'active' : ''}`}>
            <User size={18} /> Profile
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;
