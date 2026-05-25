import React, { useState, useEffect, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { Clock, CheckCircle, AlertCircle, ChevronRight, ChevronLeft } from 'lucide-react';
import API_BASE_URL from '../apiConfig';
import './pages.css';

interface Question {
  id: number;
  section: string;
  text: string;
  source?: string;
  options: string[];
}

interface TestData {
  id: number;
  title: string;
  questions: Question[];
}

interface ReviewItem {
  id: number;
  correct_answer: string;
  explanation: string;
}

interface TestResult {
  score: number;
  total: number;
  review_data: ReviewItem[];
}

const MockTestInterface: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  const [testData, setTestData] = useState<TestData | null>(null);
  const [loading, setLoading] = useState(true);
  const [currentQIndex, setCurrentQIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<number, string>>({});
  const [timeLeft, setTimeLeft] = useState(7200); // 2 hours default
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState<TestResult | null>(null);
  const [reviewMode, setReviewMode] = useState(false);

  const handleSubmit = useCallback(async () => {
    if (!testData) return;

    setSubmitting(true);
    const userId = localStorage.getItem('uksssc_user_id') || '1';
    try {
      const res = await axios.post(`${API_BASE_URL}/submit_test`, {
        test_id: parseInt(id!),
        user_id: parseInt(userId),
        answers: answers
      });

      setResult(res.data);
      setSubmitting(false);
    } catch (err) {
      console.error("Failed to submit test", err);
      setSubmitting(false);
      alert("Failed to submit test results.");
    }
  }, [id, testData, answers]);

  useEffect(() => {
    // Fetch test questions
    axios.get(`${API_BASE_URL}/tests/${id}`)
      .then(res => {
        setTestData(res.data);
        // Set time based on questions (e.g. 1 min per question)
        setTimeLeft(res.data.questions.length * 60);
        setLoading(false);
      })
      .catch(err => {
        console.error("Failed to load test", err);
        setLoading(false);
      });
  }, [id]);

  useEffect(() => {
    if (loading || result) return;

    const timer = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) {
          clearInterval(timer);
          handleSubmit();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [loading, result, handleSubmit]);

  const handleSelectOption = (qId: number, option: string) => {
    setAnswers(prev => ({
      ...prev,
      [qId]: option
    }));
  };

  const formatTime = (seconds: number) => {
    const h = Math.floor(seconds / 3600);
    const m = Math.floor((seconds % 3600) / 60);
    const s = seconds % 60;
    return `${h > 0 ? h + ':' : ''}${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  if (loading) return <div className="container"><div className="loading-spinner">Loading exam...</div></div>;
  if (!testData) return <div className="container"><h2>Test not found</h2></div>;

  if (result && !reviewMode) {
    return (
      <div className="container animate-fade-in" style={{ maxWidth: '800px' }}>
        <div className="glass-panel" style={{ textAlign: 'center', padding: '4rem 2rem' }}>
          <div style={{ display: 'inline-flex', background: 'rgba(16, 185, 129, 0.1)', color: 'var(--accent-success)', padding: '1rem', borderRadius: '50%', marginBottom: '1.5rem' }}>
            <CheckCircle size={48} />
          </div>
          <h1 className="page-title">Test Submitted!</h1>
          <p className="page-subtitle" style={{ marginBottom: '2rem' }}>Here is your performance breakdown.</p>

          <div className="stats-grid" style={{ marginBottom: '2rem' }}>
            <div className="stat-card" style={{ background: 'var(--bg-elevated)', borderRadius: 'var(--radius-lg)' }}>
              <div className="stat-info" style={{ textAlign: 'center', width: '100%' }}>
                <h3>Score</h3>
                <p className="stat-value gradient-text">{result.score} / {result.total}</p>
              </div>
            </div>
            <div className="stat-card" style={{ background: 'var(--bg-elevated)', borderRadius: 'var(--radius-lg)' }}>
              <div className="stat-info" style={{ textAlign: 'center', width: '100%' }}>
                <h3>Percentage</h3>
                <p className="stat-value">{((result.score / result.total) * 100).toFixed(1)}%</p>
              </div>
            </div>
          </div>

          <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center' }}>
            <button className="btn btn-outline" onClick={() => navigate('/')}>
              Return to Dashboard
            </button>
            <button className="btn btn-primary" onClick={() => { setReviewMode(true); setCurrentQIndex(0); }}>
              Review Answers
            </button>
          </div>
        </div>
      </div>
    );
  }

  const currentQ = testData.questions[currentQIndex];
  const isLastQuestion = currentQIndex === testData.questions.length - 1;

  let reviewDataForQ = null;
  if (reviewMode && result?.review_data) {
    reviewDataForQ = result.review_data.find((r) => r.id === currentQ.id);
  }

  return (
    <div className="container animate-fade-in" style={{ maxWidth: '800px' }}>
      <div className="test-header">
        <div>
          <h2 style={{ fontSize: '1.25rem', marginBottom: '0.25rem' }}>
            {reviewMode ? "Review Mode: " : ""}{testData.title}
          </h2>
          <p className="text-muted" style={{ fontSize: '0.9rem' }}>Question {currentQIndex + 1} of {testData.questions.length}</p>
        </div>
        {!reviewMode && (
          <div className="timer">
            <Clock size={24} />
            {formatTime(timeLeft)}
          </div>
        )}
      </div>

      <div className="glass-panel question-panel">
        <div className="question-meta">
          <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center' }}>
            <span className="section-badge">{currentQ.section}</span>
            {currentQ.source && (
              <span className="source-badge" style={{
                background: 'rgba(245, 158, 11, 0.1)',
                color: 'var(--accent-warning)',
                padding: '0.25rem 0.75rem',
                border: '1px solid rgba(245, 158, 11, 0.2)',
                borderRadius: '1rem',
                fontSize: '0.8rem',
                fontWeight: 600
              }}>
                Source: {currentQ.source}
              </span>
            )}
          </div>
          {reviewMode && reviewDataForQ && (
            <span style={{
              padding: '0.25rem 0.75rem',
              borderRadius: '1rem',
              fontSize: '0.875rem',
              background: answers[currentQ.id] === reviewDataForQ.correct_answer ? 'rgba(16, 185, 129, 0.1)' : 'rgba(239, 68, 68, 0.1)',
              color: answers[currentQ.id] === reviewDataForQ.correct_answer ? 'var(--accent-success)' : 'var(--accent-error)'
            }}>
              {answers[currentQ.id] === reviewDataForQ.correct_answer ? 'Correct' : (answers[currentQ.id] ? 'Incorrect' : 'Skipped')}
            </span>
          )}
        </div>

        <h3 className="question-text">{currentQ.text}</h3>

        <div className="options-grid">
          {currentQ.options.map((opt, i) => {
            let btnClass = "option-btn";

            if (reviewMode && reviewDataForQ) {
              if (opt === reviewDataForQ.correct_answer) {
                btnClass += " selected"; // Green highlight via CSS or inline
              } else if (opt === answers[currentQ.id]) {
                btnClass += " error"; // Red highlight
              }
            } else if (!reviewMode && answers[currentQ.id] === opt) {
              btnClass += " selected";
            }

            return (
              <button
                key={i}
                className={btnClass}
                onClick={() => !reviewMode && handleSelectOption(currentQ.id, opt)}
                style={reviewMode ? {
                  borderColor: opt === reviewDataForQ?.correct_answer ? 'var(--accent-success)' : (opt === answers[currentQ.id] ? 'var(--accent-error)' : ''),
                  background: opt === reviewDataForQ?.correct_answer ? 'rgba(16, 185, 129, 0.05)' : (opt === answers[currentQ.id] ? 'rgba(239, 68, 68, 0.05)' : '')
                } : {}}
              >
                <span style={{ fontWeight: 600, marginRight: '1rem', color: reviewMode && opt === reviewDataForQ?.correct_answer ? 'var(--accent-success)' : 'var(--text-muted)' }}>
                  {String.fromCharCode(65 + i)}.
                </span>
                {opt}
              </button>
            )
          })}
        </div>

        {reviewMode && reviewDataForQ && (
          <div className="explanation-box" style={{ marginTop: '2rem', padding: '1.5rem', background: 'rgba(59, 130, 246, 0.05)', borderLeft: '4px solid var(--accent-primary)', borderRadius: '0 var(--radius-md) var(--radius-md) 0' }}>
            <h4 style={{ color: 'var(--accent-primary)', marginBottom: '0.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <AlertCircle size={18} /> AI Explanation (विस्तृत व्याख्या)
            </h4> {/* The explanation might not always be AI-generated, especially for extracted questions. Consider renaming to "Explanation" or "Detailed Explanation". */}
            <p style={{ color: 'var(--text-secondary)', lineHeight: 1.6, fontSize: '0.95rem' }}>
              {reviewDataForQ.explanation}
            </p>
          </div>
        )}
      </div>

      <div className="test-footer">
        <button
          className="btn btn-outline"
          onClick={() => setCurrentQIndex(prev => Math.max(0, prev - 1))}
          disabled={currentQIndex === 0}
        >
          <ChevronLeft size={20} /> Previous
        </button>

        {isLastQuestion ? (
          reviewMode ? (
            <button className="btn btn-primary" onClick={() => navigate('/')}>
              Finish Review <CheckCircle size={20} />
            </button>
          ) : (
            <button
              className="btn btn-primary"
              onClick={handleSubmit}
              disabled={submitting}
            >
              {submitting ? 'Submitting...' : 'Submit Test'} <CheckCircle size={20} />
            </button>
          )
        ) : (
          <button
            className="btn btn-primary"
            onClick={() => setCurrentQIndex(prev => Math.min(testData.questions.length - 1, prev + 1))}
          >
            Next <ChevronRight size={20} />
          </button>
        )}
      </div>

      <div className="app-watermark centered">
        Tushar-Classes-2026
      </div>
    </div>
  );
};

export default MockTestInterface;
