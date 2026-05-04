import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { BookMarked, Star, Play, RefreshCw, ShieldCheck, Calendar, FileText, Loader2 } from 'lucide-react';
import API_BASE_URL from '../apiConfig';
import './pages.css';

interface ExtractedTest {
  id: number;
  title: string;
  created_at: string;
  question_count: number;
  is_extracted: boolean;
}

const ExtractedTests: React.FC = () => {
  const navigate = useNavigate();
  const [tests, setTests] = useState<ExtractedTest[]>([]);
  const [subTopics, setSubTopics] = useState<string[]>([]);
  const [selectedTopic, setSelectedTopic] = useState<string>('All Topics');
  const [loading, setLoading] = useState(true);
  const [seeding, setSeeding] = useState(false);
  const [excludeAttempted, setExcludeAttempted] = useState(false);
  const [progress, setProgress] = useState<any>(null);

  const fetchSubTopics = () => {
    axios.get(`${API_BASE_URL}/extracted_subtopics`)
      .then(res => setSubTopics(['All Topics', ...res.data]))
      .catch(err => console.error("Failed to fetch sub-topics:", err));
  };

  const fetchTests = () => {
    setLoading(true);
    axios.get(`${API_BASE_URL}/extracted_tests`)
      .then(res => {
        let data = res.data;
        if (data && !Array.isArray(data)) {
          if (Array.isArray(data.value)) data = data.value;
          else if (Array.isArray(data.tests)) data = data.tests;
          else data = [];
        }
        setTests(Array.isArray(data) ? data : []);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Failed to fetch extracted tests:", err);
        setTests([]);
        setLoading(false);
      });
  };

  const fetchProgress = () => {
    axios.get(`${API_BASE_URL}/user_progress/1`)
      .then(res => setProgress(res.data))
      .catch(err => console.error("Failed to fetch progress:", err));
  };

  useEffect(() => {
    fetchTests();
    fetchSubTopics();
    fetchProgress();
  }, []);

  const handleSeedTest = async () => {
    setSeeding(true);
    try {
      const payload = {
        sub_topic: selectedTopic === 'All Topics' ? null : selectedTopic,
        exclude_attempted: excludeAttempted,
        user_id: 1
      };
      await axios.post(`${API_BASE_URL}/seed_extracted_test`, payload);
      fetchTests();
      fetchProgress();
    } catch (err: any) {
      const errorMsg = err.response?.data?.error || 'Failed to create extracted test.';
      alert(errorMsg);
    } finally {
      setSeeding(false);
    }
  };

  const filteredTests = selectedTopic === 'All Topics' 
    ? tests 
    : tests.filter(t => t.title.includes(selectedTopic) || t.is_extracted); // Fallback: show all if title search isn't perfect, or we can improve the title matching

  return (
    <div className="container animate-fade-in">
      {/* ── Hero Header ── */}
      <div className="extracted-hero">
        <div className="extracted-hero-badge">
          <ShieldCheck size={16} />
          <span>100% Authentic • No AI Generated Content</span>
        </div>
        <h1 className="page-title" style={{ marginTop: '1rem' }}>
          <span className="gradient-text">Extracted</span> Mock Tests
        </h1>
        <p className="page-subtitle" style={{ maxWidth: '600px' }}>
          Real questions from UKSSSC previous exams, categorized by sub-topics. 
          Practice exactly what you need with verified exam material.
        </p>

        {/* Topic Selector */}
        <div className="topic-selector-container">
           {subTopics.map(topic => (
             <button 
               key={topic} 
               className={`topic-chip ${selectedTopic === topic ? 'active' : ''}`}
               onClick={() => setSelectedTopic(topic)}
             >
               {topic}
             </button>
           ))}
        </div>

        {/* ── Progress Bar ── */}
        {progress && (
          <div className="extracted-progress-container glass-panel">
            <div className="progress-header">
              <div className="progress-info">
                <Star size={16} className="text-amber" />
                <span>Bank Progress: <strong>{progress.attempted_count} / {progress.total_bank}</strong> Questions</span>
              </div>
              <span className="progress-percent">{progress.overall_progress}%</span>
            </div>
            <div className="progress-bar-bg">
              <div 
                className="progress-bar-fill" 
                style={{ width: `${progress.overall_progress}%` }}
              ></div>
            </div>
            <div className="progress-footer">
              <label className="exclude-toggle">
                <input 
                  type="checkbox" 
                  checked={excludeAttempted}
                  onChange={(e) => setExcludeAttempted(e.target.checked)}
                />
                <span>Exclude Attempted Questions</span>
              </label>
            </div>
          </div>
        )}
      </div>

      {/* ── Divider ── */}
      <div className="extracted-divider">
        <span>{selectedTopic} Test Sets</span>
      </div>

      {/* ── Test List ── */}
      {loading ? (
        <div className="empty-state">
          <Loader2 size={40} className="empty-icon spin-icon" />
          <p>Loading extracted tests...</p>
        </div>
      ) : filteredTests.length === 0 ? (
        <div className="glass-panel extracted-empty">
          <BookMarked size={56} className="empty-icon" style={{ color: 'var(--accent-secondary)', opacity: 0.6 }} />
          <h2 style={{ marginBottom: '0.5rem' }}>No {selectedTopic} Tests Yet</h2>
          <p style={{ color: 'var(--text-secondary)', marginBottom: '2rem', maxWidth: '400px', textAlign: 'center' }}>
            Click the button below to generate a new 30-question test set for <strong>{selectedTopic}</strong>.
          </p>
          <button
            className="btn btn-primary"
            onClick={handleSeedTest}
            disabled={seeding}
            id="btn-generate-topic-test"
            style={{ padding: '0.9rem 2rem', fontSize: '1rem' }}
          >
            {seeding ? (
              <><Loader2 size={18} className="spin-icon" /> Generating...</>
            ) : (
              <><RefreshCw size={18} /> Generate {selectedTopic} Test</>
            )}
          </button>
        </div>
      ) : (
        <>
          <div className="extracted-tests-grid">
            {Array.isArray(filteredTests) && filteredTests.map((test, idx) => (
              <div key={test.id} className="glass-panel extracted-test-card">
                <div className="extracted-card-top">
                  <div className="extracted-set-badge">Set {filteredTests.length - idx}</div>
                  <div className="extracted-verified-badge">
                    <ShieldCheck size={13} /> Verified
                  </div>
                </div>

                <h3 className="extracted-card-title">{test.title}</h3>

                <div className="extracted-card-meta">
                  <span><FileText size={14} /> {test.question_count} Questions</span>
                  <span><Calendar size={14} /> {test.created_at}</span>
                </div>

                <div className="extracted-card-tags">
                  <span className="section-badge">Uttarakhand GK</span>
                  <span className="extracted-source-tag">Official Sources</span>
                </div>

                <button
                  className="btn btn-primary extracted-start-btn"
                  id={`btn-start-extracted-${test.id}`}
                  onClick={() => navigate(`/test/${test.id}`)}
                >
                  <Play size={16} /> Start Test
                </button>
              </div>
            ))}
          </div>

          {/* Add more test */}
          <div className="extracted-add-more">
            <button
              className="btn btn-outline"
              onClick={handleSeedTest}
              disabled={seeding}
              id="btn-add-topic-set"
            >
              {seeding ? (
                <><Loader2 size={16} className="spin-icon" /> Generating {selectedTopic} Set...</>
              ) : (
                <><RefreshCw size={16} /> Generate New {selectedTopic} Set</>
              )}
            </button>
          </div>
        </>
      )}
    </div>
  );
};

export default ExtractedTests;
