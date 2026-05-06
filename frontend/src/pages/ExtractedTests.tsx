import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { BookMarked, Star, Play, RefreshCw, ShieldCheck, Calendar, FileText, Loader2, ListOrdered } from 'lucide-react';
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
  const [searchQuery, setSearchQuery] = useState('');
  const [loading, setLoading] = useState(true);
  const [seeding, setSeeding] = useState(false);
  const [excludeAttempted, setExcludeAttempted] = useState(false);
  const [numQuestions, setNumQuestions] = useState(100); // New state for number of questions
  const [balanceTopics, setBalanceTopics] = useState(true); // New state for balancing topics
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
        user_id: 1,
        num_questions: numQuestions, // Send numQuestions
        balance_topics: balanceTopics // Send balanceTopics
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

  const filteredTests = (selectedTopic === 'All Topics'
    ? tests
    : tests.filter(t => t.title.toLowerCase().includes(selectedTopic.toLowerCase())))
    .filter(t =>
      t.title.toLowerCase().includes(searchQuery.toLowerCase())
    );

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

        {/* Search Bar */}
        <div style={{ width: '100%', maxWidth: '500px', margin: '1.5rem 0' }}>
          <input
            type="text"
            className="form-control"
            placeholder="Search within your generated tests..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{ background: 'var(--bg-elevated)', border: '1px solid var(--border-subtle)' }}
          />
        </div>

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

        {/* ── Test Generation Options ── */}
        <div className="glass-panel" style={{ marginTop: '1.5rem', padding: '1.5rem', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <h3 className="section-title" style={{ margin: '0', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <ListOrdered size={20} className="gradient-text" /> Generate New Test
          </h3>
          <div style={{ display: 'flex', gap: '1rem', alignItems: 'center', flexWrap: 'wrap' }}>
            <div className="input-group" style={{ flex: '1 1 150px', margin: 0 }}>
              <label className="input-label" htmlFor="numQuestions">Number of Questions</label>
              <input
                id="numQuestions"
                type="number"
                className="select-field"
                value={numQuestions}
                onChange={(e) => setNumQuestions(Math.max(1, parseInt(e.target.value) || 1))}
                min="1"
                max="200" // Set a reasonable max
                style={{ width: '100%' }}
              />
            </div>
            <label className="exclude-toggle" style={{ flex: '1 1 200px', margin: 0 }}>
              <input
                type="checkbox"
                checked={excludeAttempted}
                onChange={(e) => setExcludeAttempted(e.target.checked)}
              />
              <span>Exclude Attempted Questions</span>
            </label>
            {selectedTopic === 'All Topics' && (
              <label className="exclude-toggle" style={{ flex: '1 1 200px', margin: 0 }}>
                <input
                  type="checkbox"
                  checked={balanceTopics}
                  onChange={(e) => setBalanceTopics(e.target.checked)}
                />
                <span>Balance Topics (Full Mock)</span>
              </label>
            )}
          </div>
          <button
            className="btn btn-primary"
            onClick={handleSeedTest}
            disabled={seeding}
            id="btn-generate-topic-test"
            style={{ padding: '0.9rem 2rem', fontSize: '1rem', marginTop: '1rem' }}
          >
            {seeding ? (
              <><Loader2 size={18} className="spin-icon" /> Generating...</>
            ) : (
              <><RefreshCw size={18} /> Generate New {selectedTopic === 'All Topics' ? 'Full Mock' : selectedTopic} Test</>
            )}
          </button>
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
          <p style={{ color: 'var(--text-secondary)', marginBottom: '2rem', maxWidth: '400px', textAlign: 'center' }}>Click the button below to generate a new {numQuestions}-question test set for <strong>{selectedTopic}</strong>.</p>
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
        </>
      )}
    </div>
  );
};

export default ExtractedTests;
