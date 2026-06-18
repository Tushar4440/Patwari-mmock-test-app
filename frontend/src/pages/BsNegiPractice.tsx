import React, { useState, useEffect, useCallback } from 'react';
import axios from 'axios';
import {
  BookOpen, Award, CheckCircle2, XCircle, ChevronLeft, ChevronRight,
  Play, ArrowLeft, Info, Clock, Zap
} from 'lucide-react';
import API_BASE_URL from '../apiConfig';
import './pages.css';

interface Question {
  id: string;
  unit: number;
  chapter: string;
  text_hi: string;
  text_en: string;
  options: string[];
  correct_answer: string;
  explanation_hi: string;
  explanation_en: string;
  attempted: boolean;
  correct: boolean;
}

interface UnitInfo {
  unit_number: number;
  title_hi: string;
  title_en: string;
  chapters: string[];
  question_count: number;
  attempted_count: number;
  correct_count: number;
}

type LanguageMode = 'bilingual' | 'hindi' | 'english';
type ScreenMode = 'dashboard' | 'practice' | 'mocktest' | 'testresult';

const BsNegiPractice: React.FC = () => {
  const userId = localStorage.getItem('uksssc_user_id') || '1';

  // State
  const [units, setUnits] = useState<UnitInfo[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [languageMode, setLanguageMode] = useState<LanguageMode>('bilingual');
  const [screenMode, setScreenMode] = useState<ScreenMode>('dashboard');

  // Selected practice details
  const [selectedUnit, setSelectedUnit] = useState<number | null>(null);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [currentQIndex, setCurrentQIndex] = useState<number>(0);

  // Study mode answer state
  const [selectedAnswer, setSelectedAnswer] = useState<string | null>(null);
  const [answeredMap, setAnsweredMap] = useState<Record<string, { selected: string; correct: boolean }>>({});

  // Mock Test state
  const [mockAnswers, setMockAnswers] = useState<Record<string, string>>({});
  const [testTimeLeft, setTestTimeLeft] = useState<number>(1200); // 20 minutes default
  const [testActive, setTestActive] = useState<boolean>(false);
  const [testResult, setTestResult] = useState<{ score: number; total: number } | null>(null);
  const [reviewMode, setReviewMode] = useState<boolean>(false);

  // Load Units Data
  const loadUnits = useCallback(() => {
    setLoading(true);
    axios.get(`${API_BASE_URL}/bs_negi/units?user_id=${userId}`)
      .then(res => {
        setUnits(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Failed to fetch BS Negi units", err);
        setLoading(false);
      });
  }, [userId]);

  useEffect(() => {
    loadUnits();
  }, [loadUnits]);

  // Mock test timer
  useEffect(() => {
    if (screenMode !== 'mocktest' || reviewMode || !testActive) return;

    const timer = setInterval(() => {
      setTestTimeLeft(prev => {
        if (prev <= 1) {
          clearInterval(timer);
          handleMockTestSubmit();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [screenMode, reviewMode, testActive]);

  // Initialize Practice / Study Mode
  const startPractice = (unitNum: number) => {
    setLoading(true);
    setSelectedUnit(unitNum);
    axios.get(`${API_BASE_URL}/bs_negi/questions?unit=${unitNum}&user_id=${userId}`)
      .then(res => {
        setQuestions(res.data);
        setCurrentQIndex(0);
        setSelectedAnswer(null);
        setAnsweredMap({});
        setScreenMode('practice');
        setLoading(false);
      })
      .catch(err => {
        console.error("Failed to fetch questions", err);
        setLoading(false);
      });
  };

  // Initialize Mock Test
  const startMockTest = (unitNum: number | null) => {
    setLoading(true);
    setSelectedUnit(unitNum);
    const url = unitNum
      ? `${API_BASE_URL}/bs_negi/questions?unit=${unitNum}&user_id=${userId}`
      : `${API_BASE_URL}/bs_negi/questions?user_id=${userId}`;

    axios.get(url)
      .then(res => {
        let testQs = res.data;
        // Shuffle and pick 20 questions (or all if less than 20)
        testQs = [...testQs].sort(() => Math.random() - 0.5);
        const limit = 20;
        setQuestions(testQs.slice(0, limit));
        setCurrentQIndex(0);
        setMockAnswers({});
        setTestTimeLeft(Math.min(testQs.length, limit) * 60); // 1 minute per question
        setTestActive(true);
        setReviewMode(false);
        setTestResult(null);
        setScreenMode('mocktest');
        setLoading(false);
      })
      .catch(err => {
        console.error("Failed to load questions for test", err);
        setLoading(false);
      });
  };

  // Initialize AI Practice
  const startAIPractice = () => {
    setLoading(true);
    const section = "full"; // Or allow user to select a section
    const numQuestionsPerSection = 3; // Generate a smaller set for quick practice

    axios.post(`${API_BASE_URL}/ai_practice_questions`, {
      section: section,
      num_questions_per_section: numQuestionsPerSection
    }).then(res => {
      setQuestions(res.data);
      setCurrentQIndex(0);
      setSelectedAnswer(null);
      setAnsweredMap({});
      setScreenMode('practice');
      setLoading(false);
    }).catch(err => {
      console.error("Failed to fetch AI practice questions", err);
      setLoading(false);
    });
  };

  // Option split helper to parse options like "हिन्दी / English"
  const getDisplayOption = (option: string) => {
    if (!option) return '';
    const parts = option.split(' / ');
    if (parts.length > 1) {
      if (languageMode === 'hindi') return parts[0].trim();
      if (languageMode === 'english') return parts[1].trim();
    }
    return option;
  };

  // Handle option selection in Study Mode
  const handleSelectOptionStudy = (question: Question, option: string) => {
    if (answeredMap[question.id] || selectedAnswer) return; // already answered

    const isCorrect = option === question.correct_answer;
    setSelectedAnswer(option);
    setAnsweredMap(prev => ({
      ...prev,
      [question.id]: { selected: option, correct: isCorrect }
    }));

    // Only post progress for B.S. Negi questions, not AI-generated ones
    if (question.id.startsWith('bs_negi_')) {
      axios.post(`${API_BASE_URL}/bs_negi/progress`, {
        user_id: parseInt(userId),
        question_id: question.id,
        is_correct: isCorrect
      }).catch(err => console.error("Failed to update progress", err));
    }
  };

  // Handle Mock Test Option Selection
  const handleSelectOptionMock = (questionId: string, option: string) => {
    if (reviewMode) return;
    setMockAnswers(prev => ({
      ...prev,
      [questionId]: option
    }));
  };

  // Submit Mock Test
  const handleMockTestSubmit = () => {
    setTestActive(false);
    let score = 0;
    const updates = questions.map(q => {
      const ans = mockAnswers[q.id] || "";
      const correct = ans === q.correct_answer;
      if (correct) score++;
      return {
        question_id: q.id,
        is_correct: correct
      };
    });

    setTestResult({
      score: score,
      total: questions.length
    });

    // Save all progress in batch
    axios.post(`${API_BASE_URL}/bs_negi/progress`, {
      user_id: parseInt(userId),
      updates: updates
    })
      .then(() => {
        setScreenMode('testresult');
        loadUnits(); // Refresh main dashboard progress
      })
      .catch(err => {
        console.error("Failed to save test progress in batch", err);
        setScreenMode('testresult');
      });
  };

  // Reset/Exit to Dashboard
  const exitToDashboard = () => {
    setSelectedUnit(null);
    setScreenMode('dashboard');
    loadUnits();
  };

  const formatTime = (seconds: number) => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  if (loading) {
    return (
      <div className="container" style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '60vh' }}>
        <div className="loading-spinner">Loading B.S. Negi MCQ Practice...</div>
      </div>
    );
  }

  // Dashboard view
  if (screenMode === 'dashboard') {
    return (
      <div className="container animate-fade-in">
        {/* Header & Title */}
        <div className="dashboard-header" style={{ marginBottom: '2.5rem' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.25rem' }}>
              <span className="section-badge" style={{ background: 'rgba(99, 102, 241, 0.15)', color: 'var(--accent-primary)', fontWeight: 600 }}>Standard Reference Study</span>
            </div>
            <h1 className="page-title">
              B.S. Negi <span className="gradient-text">MCQ Practice</span>
            </h1>
            <p className="page-subtitle">Practice question-by-question or take mock tests based on B.S. Negi's complete study book.</p>
          </div>

          <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
            {/* Language Selection tabs */}
            <div className="glass-panel" style={{ display: 'flex', gap: '0.25rem', padding: '0.25rem', borderRadius: 'var(--radius-md)', background: 'rgba(255,255,255,0.03)' }}>
              <button
                className={`btn ${languageMode === 'bilingual' ? 'btn-primary' : 'btn-outline'}`}
                style={{ padding: '0.4rem 0.8rem', fontSize: '0.8rem' }}
                onClick={() => setLanguageMode('bilingual')}
              >
                Bilingual
              </button>
              <button
                className={`btn ${languageMode === 'hindi' ? 'btn-primary' : 'btn-outline'}`}
                style={{ padding: '0.4rem 0.8rem', fontSize: '0.8rem' }}
                onClick={() => setLanguageMode('hindi')}
              >
                हिन्दी
              </button>
              <button
                className={`btn ${languageMode === 'english' ? 'btn-primary' : 'btn-outline'}`}
                style={{ padding: '0.4rem 0.8rem', fontSize: '0.8rem' }}
                onClick={() => setLanguageMode('english')}
              >
                English
              </button>
            </div>

            <button className="btn btn-primary" onClick={startAIPractice} style={{ background: 'linear-gradient(135deg, var(--accent-secondary), var(--accent-primary))', border: 'none', boxShadow: 'none' }}>
              <Zap size={16} /> AI Practice (Unlimited)
            </button>

            <button className="btn btn-primary" onClick={() => startMockTest(null)}>
              <Play size={16} /> Full Mock Test (20 Qs)
            </button>
          </div>
        </div>

        {/* Units Grid */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(340px, 1fr))', gap: '2rem', marginBottom: '4rem' }}>
          {units.map((unit) => {
            const progressPct = unit.question_count > 0
              ? Math.round((unit.attempted_count / unit.question_count) * 100)
              : 0;

            return (
              <div key={unit.unit_number} className="glass-panel" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between', padding: '1.75rem', position: 'relative', overflow: 'hidden' }}>
                {/* Accent glow on top */}
                <div style={{ position: 'absolute', top: 0, left: 0, right: 0, height: '4px', background: 'linear-gradient(90deg, var(--accent-primary), var(--accent-secondary))' }} />

                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.75rem' }}>
                    <span style={{ fontSize: '0.8rem', color: 'var(--accent-primary)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.1em' }}>
                      Unit {unit.unit_number}
                    </span>
                    <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                      {unit.question_count} Questions
                    </span>
                  </div>

                  <h3 style={{ fontSize: '1.25rem', marginBottom: '0.5rem', fontWeight: 700 }}>
                    {unit.title_hi}
                  </h3>
                  <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '1.5rem', minHeight: '2.5rem', lineHeight: '1.4' }}>
                    {unit.title_en}
                  </p>

                  {/* Chapters pill list */}
                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.35rem', marginBottom: '1.5rem' }}>
                    {unit.chapters.slice(0, 3).map((ch, idx) => (
                      <span key={idx} style={{ fontSize: '0.75rem', background: 'rgba(255,255,255,0.04)', color: 'var(--text-secondary)', padding: '0.2rem 0.5rem', borderRadius: '4px' }}>
                        {ch.split(' / ')[0]}
                      </span>
                    ))}
                    {unit.chapters.length > 3 && (
                      <span style={{ fontSize: '0.75rem', background: 'rgba(255,255,255,0.04)', color: 'var(--accent-primary)', padding: '0.2rem 0.5rem', borderRadius: '4px', fontWeight: 600 }}>
                        +{unit.chapters.length - 3} more
                      </span>
                    )}
                  </div>
                </div>

                <div>
                  {/* Progress gauge */}
                  <div style={{ marginBottom: '1.5rem' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', marginBottom: '0.35rem' }}>
                      <span style={{ color: 'var(--text-muted)' }}>Progress ({unit.attempted_count}/{unit.question_count})</span>
                      <span style={{ color: 'var(--text-primary)', fontWeight: 600 }}>{progressPct}%</span>
                    </div>
                    <div style={{ height: '6px', background: 'rgba(255,255,255,0.05)', borderRadius: '3px', overflow: 'hidden' }}>
                      <div style={{ width: `${progressPct}%`, height: '100%', background: 'linear-gradient(90deg, var(--accent-primary), var(--accent-secondary))', borderRadius: '3px', transition: 'width 0.3s ease' }} />
                    </div>
                  </div>

                  {/* Action buttons */}
                  <div style={{ display: 'flex', gap: '1rem' }}>
                    <button
                      className="btn btn-primary"
                      style={{ flex: 1, padding: '0.6rem 1rem', fontSize: '0.85rem' }}
                      onClick={() => startPractice(unit.unit_number)}
                    >
                      <BookOpen size={14} /> Practice
                    </button>
                    <button
                      className="btn btn-outline"
                      style={{ flex: 1, padding: '0.6rem 1rem', fontSize: '0.85rem' }}
                      onClick={() => startMockTest(unit.unit_number)}
                    >
                      <Award size={14} /> Mock Test
                    </button>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    );
  }

  // Practice/Study Mode
  if (screenMode === 'practice') {
    const currentQ = questions[currentQIndex];
    if (!currentQ) return <div className="container">No questions found.</div>;

    const currentQAnswerStatus = answeredMap[currentQ.id];
    const hasAlreadyAnswered = !!currentQAnswerStatus;

    return (
      <div className="container animate-fade-in" style={{ maxWidth: '850px' }}>
        {/* Practice Header */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem', borderBottom: '1px solid var(--glass-border)', paddingBottom: '1rem' }}>
          <div>
            <button className="btn btn-outline" style={{ padding: '0.4rem 0.8rem', fontSize: '0.8rem', display: 'flex', alignItems: 'center', gap: '0.35rem', marginBottom: '0.5rem' }} onClick={exitToDashboard}>
              <ArrowLeft size={14} /> Exit Practice
            </button>
            <h2 style={{ fontSize: '1.25rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              Unit {selectedUnit} Practice <span style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>({currentQIndex + 1} of {questions.length})</span>
            </h2>
            <p style={{ color: 'var(--accent-primary)', fontSize: '0.85rem', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '0.25rem' }}>
              <Info size={12} /> {currentQ.chapter.split(' / ')[0]}
            </p>
          </div>

          {/* Quick Lang Switch */}
          <div style={{ display: 'flex', gap: '0.2rem', padding: '0.2rem', background: 'rgba(255,255,255,0.03)', borderRadius: 'var(--radius-md)' }}>
            <button className={`btn ${languageMode === 'bilingual' ? 'btn-primary' : 'btn-outline'}`} style={{ padding: '0.3rem 0.6rem', fontSize: '0.75rem' }} onClick={() => setLanguageMode('bilingual')}>Bilingual</button>
            <button className={`btn ${languageMode === 'hindi' ? 'btn-primary' : 'btn-outline'}`} style={{ padding: '0.3rem 0.6rem', fontSize: '0.75rem' }} onClick={() => setLanguageMode('hindi')}>हिन्दी</button>
            <button className={`btn ${languageMode === 'english' ? 'btn-primary' : 'btn-outline'}`} style={{ padding: '0.3rem 0.6rem', fontSize: '0.75rem' }} onClick={() => setLanguageMode('english')}>Eng</button>
          </div>
        </div>

        {/* Question Panel */}
        <div className="glass-panel" style={{ marginBottom: '1.5rem', padding: '2.5rem' }}>
          {/* Question Text */}
          <div style={{ marginBottom: '2rem' }}>
            {/* Hindi Text */}
            {(languageMode === 'bilingual' || languageMode === 'hindi') && (
              <h3 style={{ fontSize: '1.3rem', fontWeight: 600, lineHeight: '1.5', color: 'var(--text-primary)', marginBottom: languageMode === 'bilingual' ? '0.75rem' : '0' }}>
                {currentQ.text_hi}
              </h3>
            )}
            {/* English Text */}
            {(languageMode === 'bilingual' || languageMode === 'english') && (
              <p style={{ fontSize: '1.15rem', color: languageMode === 'bilingual' ? 'var(--text-secondary)' : 'var(--text-primary)', lineHeight: '1.5', fontStyle: languageMode === 'bilingual' ? 'italic' : 'normal' }}>
                {currentQ.text_en}
              </p>
            )}
          </div>

          {/* Options Grid */}
          <div className="options-grid" style={{ gap: '0.75rem', marginBottom: '2rem' }}>
            {currentQ.options.map((opt, i) => {
              const displayOpt = getDisplayOption(opt);
              const isCorrectOpt = opt === currentQ.correct_answer;
              const isSelected = selectedAnswer === opt || (hasAlreadyAnswered && currentQAnswerStatus.selected === opt);

              let optionBg = 'var(--bg-elevated)';
              let optionBorder = 'var(--glass-border)';
              let optionColor = 'var(--text-primary)';

              if (hasAlreadyAnswered) {
                if (isCorrectOpt) {
                  // highlight green
                  optionBg = 'rgba(16, 185, 129, 0.08)';
                  optionBorder = '1px solid var(--accent-success)';
                  optionColor = 'var(--accent-success)';
                } else if (isSelected) {
                  // highlight red
                  optionBg = 'rgba(239, 68, 68, 0.08)';
                  optionBorder = '1px solid var(--accent-danger)';
                  optionColor = 'var(--accent-danger)';
                } else {
                  // fade out others
                  optionBg = 'rgba(255,255,255,0.01)';
                  optionBorder = '1px solid rgba(255,255,255,0.03)';
                  optionColor = 'var(--text-muted)';
                }
              }

              return (
                <button
                  key={i}
                  className="option-btn"
                  onClick={() => handleSelectOptionStudy(currentQ, opt)}
                  disabled={hasAlreadyAnswered}
                  style={{
                    background: optionBg,
                    border: optionBorder,
                    color: optionColor,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '1.1rem 1.5rem',
                    transition: 'all 0.2s ease',
                    borderRadius: 'var(--radius-md)',
                    cursor: hasAlreadyAnswered ? 'default' : 'pointer'
                  }}
                >
                  <span style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                    <span style={{ fontWeight: 700, opacity: 0.5 }}>{String.fromCharCode(65 + i)}.</span>
                    {displayOpt}
                  </span>

                  {hasAlreadyAnswered && isCorrectOpt && <CheckCircle2 size={18} style={{ color: 'var(--accent-success)' }} />}
                  {hasAlreadyAnswered && isSelected && !isCorrectOpt && <XCircle size={18} style={{ color: 'var(--accent-danger)' }} />}
                </button>
              );
            })}
          </div>

          {/* Explanation Box */}
          {hasAlreadyAnswered && (
            <div className="animate-fade-in" style={{ padding: '1.5rem', background: 'rgba(99, 102, 241, 0.03)', borderLeft: '4px solid var(--accent-primary)', borderRadius: '4px' }}>
              <h4 style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--accent-primary)', fontSize: '0.95rem', fontWeight: 700, marginBottom: '0.5rem' }}>
                <Info size={16} /> Explanation / व्याख्या:
              </h4>

              {/* Hindi Explanation */}
              {(languageMode === 'bilingual' || languageMode === 'hindi') && currentQ.explanation_hi && (
                <p style={{ fontSize: '0.95rem', color: 'var(--text-primary)', marginBottom: languageMode === 'bilingual' ? '0.5rem' : '0', lineHeight: '1.6' }}>
                  {currentQ.explanation_hi}
                </p>
              )}
              {/* English Explanation */}
              {(languageMode === 'bilingual' || languageMode === 'english') && currentQ.explanation_en && (
                <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', fontStyle: languageMode === 'bilingual' ? 'italic' : 'normal', lineHeight: '1.6' }}>
                  {currentQ.explanation_en}
                </p>
              )}
            </div>
          )}
        </div>

        {/* Practice Navigation */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '3rem' }}>
          <button
            className="btn btn-outline"
            onClick={() => {
              setCurrentQIndex(prev => Math.max(0, prev - 1));
              setSelectedAnswer(null);
            }}
            disabled={currentQIndex === 0}
          >
            <ChevronLeft size={16} /> Previous
          </button>

          {/* Question Dot Navigator */}
          <div style={{ display: 'flex', gap: '0.35rem', overflowX: 'auto', padding: '0.5rem 0', maxWidth: '60%' }}>
            {questions.map((q, idx) => {
              const status = answeredMap[q.id];
              let dotBg = 'rgba(255,255,255,0.05)';
              let dotBorder = '1px solid var(--glass-border)';

              if (idx === currentQIndex) {
                dotBorder = '2px solid var(--accent-primary)';
                dotBg = 'rgba(99, 102, 241, 0.1)';
              } else if (status) {
                dotBg = status.correct ? 'var(--accent-success)' : 'var(--accent-danger)';
                dotBorder = 'none';
              }

              return (
                <button
                  key={q.id}
                  onClick={() => {
                    setCurrentQIndex(idx);
                    setSelectedAnswer(null);
                  }}
                  style={{
                    width: '24px',
                    height: '24px',
                    borderRadius: '50%',
                    background: dotBg,
                    border: dotBorder,
                    color: status ? '#fff' : 'var(--text-muted)',
                    fontSize: '0.7rem',
                    fontWeight: 700,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    cursor: 'pointer',
                    flexShrink: 0
                  }}
                >
                  {idx + 1}
                </button>
              );
            })}
          </div>

          <button
            className="btn btn-primary"
            onClick={() => {
              setCurrentQIndex(prev => Math.min(questions.length - 1, prev + 1));
              setSelectedAnswer(null);
            }}
            disabled={currentQIndex === questions.length - 1}
          >
            Next <ChevronRight size={16} />
          </button>
        </div>
      </div>
    );
  }

  // Mock Test Mode
  if (screenMode === 'mocktest') {
    const currentQ = questions[currentQIndex];
    if (!currentQ) return <div className="container">Loading test questions...</div>;

    return (
      <div className="container animate-fade-in" style={{ maxWidth: '850px' }}>
        {/* Test Header */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem', borderBottom: '1px solid var(--glass-border)', paddingBottom: '1rem' }}>
          <div>
            <h2 style={{ fontSize: '1.25rem', marginBottom: '0.25rem' }}>
              {reviewMode ? 'Review Mode' : 'Mock Test Session'}
            </h2>
            <p className="text-muted" style={{ fontSize: '0.85rem' }}>
              {selectedUnit ? `Unit ${selectedUnit}` : 'Full Syllabus'} Mock Test • Question {currentQIndex + 1} of {questions.length}
            </p>
          </div>

          <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
            {!reviewMode && (
              <div className="timer" style={{ fontSize: '1.2rem', padding: '0.5rem 1rem', background: 'rgba(245,158,11,0.1)', borderRadius: 'var(--radius-md)', border: '1px solid rgba(245,158,11,0.2)' }}>
                <Clock size={16} style={{ marginRight: '0.5rem', display: 'inline' }} />
                {formatTime(testTimeLeft)}
              </div>
            )}

            {!reviewMode ? (
              <button className="btn btn-outline" style={{ padding: '0.5rem 1rem', background: 'rgba(239, 68, 68, 0.1)', color: 'var(--accent-danger)', border: '1px solid rgba(239, 68, 68, 0.2)' }} onClick={() => {
                if (window.confirm("Are you sure you want to end this test? Unsubmitted progress will be lost.")) {
                  exitToDashboard();
                }
              }}>
                Cancel Test
              </button>
            ) : (
              <button className="btn btn-primary" onClick={() => setScreenMode('testresult')}>
                Back to Results
              </button>
            )}
          </div>
        </div>

        {/* Question Panel */}
        <div className="glass-panel" style={{ marginBottom: '1.5rem', padding: '2.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
            <span className="section-badge">{currentQ.chapter.split(' / ')[0]}</span>
            {reviewMode && (
              <span style={{
                padding: '0.25rem 0.75rem',
                borderRadius: '1rem',
                fontSize: '0.8rem',
                fontWeight: 600,
                background: mockAnswers[currentQ.id] === currentQ.correct_answer ? 'rgba(16, 185, 129, 0.1)' : 'rgba(239, 68, 68, 0.1)',
                color: mockAnswers[currentQ.id] === currentQ.correct_answer ? 'var(--accent-success)' : 'var(--accent-danger)'
              }}>
                {mockAnswers[currentQ.id] === currentQ.correct_answer ? 'Correct' : (mockAnswers[currentQ.id] ? 'Incorrect' : 'Skipped')}
              </span>
            )}
          </div>

          <div style={{ marginBottom: '2rem' }}>
            {/* Hindi Question */}
            {(languageMode === 'bilingual' || languageMode === 'hindi') && (
              <h3 style={{ fontSize: '1.3rem', fontWeight: 600, lineHeight: '1.5', color: 'var(--text-primary)', marginBottom: languageMode === 'bilingual' ? '0.75rem' : '0' }}>
                {currentQ.text_hi}
              </h3>
            )}
            {/* English Question */}
            {(languageMode === 'bilingual' || languageMode === 'english') && (
              <p style={{ fontSize: '1.15rem', color: languageMode === 'bilingual' ? 'var(--text-secondary)' : 'var(--text-primary)', lineHeight: '1.5' }}>
                {currentQ.text_en}
              </p>
            )}
          </div>

          {/* Options Grid */}
          <div className="options-grid" style={{ gap: '0.75rem', marginBottom: '2rem' }}>
            {currentQ.options.map((opt, i) => {
              const displayOpt = getDisplayOption(opt);
              const isSelected = mockAnswers[currentQ.id] === opt;
              const isCorrectOpt = opt === currentQ.correct_answer;

              let btnClass = "option-btn";
              let borderStyle = {};
              let bgStyle = {};

              if (reviewMode) {
                if (isCorrectOpt) {
                  borderStyle = { border: '1px solid var(--accent-success)' };
                  bgStyle = { background: 'rgba(16, 185, 129, 0.08)', color: 'var(--accent-success)' };
                } else if (isSelected) {
                  borderStyle = { border: '1px solid var(--accent-danger)' };
                  bgStyle = { background: 'rgba(239, 68, 68, 0.08)', color: 'var(--accent-danger)' };
                } else {
                  bgStyle = { opacity: 0.5 };
                }
              } else if (isSelected) {
                btnClass += " selected";
                borderStyle = { border: '1px solid var(--accent-primary)' };
                bgStyle = { background: 'rgba(99, 102, 241, 0.1)', color: '#fff' };
              }

              return (
                <button
                  key={i}
                  className={btnClass}
                  style={{
                    textAlign: 'left',
                    padding: '1.1rem 1.5rem',
                    width: '100%',
                    borderRadius: 'var(--radius-md)',
                    display: 'flex',
                    alignItems: 'center',
                    cursor: reviewMode ? 'default' : 'pointer',
                    ...borderStyle,
                    ...bgStyle
                  }}
                  onClick={() => handleSelectOptionMock(currentQ.id, opt)}
                  disabled={reviewMode}
                >
                  <span style={{ fontWeight: 700, marginRight: '1rem', color: 'var(--text-muted)' }}>
                    {String.fromCharCode(65 + i)}.
                  </span>
                  {displayOpt}
                </button>
              );
            })}
          </div>

          {/* Explanation in Review Mode */}
          {reviewMode && (
            <div className="animate-fade-in" style={{ padding: '1.5rem', background: 'rgba(99, 102, 241, 0.03)', borderLeft: '4px solid var(--accent-primary)', borderRadius: '4px' }}>
              <h4 style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--accent-primary)', fontSize: '0.95rem', fontWeight: 700, marginBottom: '0.5rem' }}>
                <Info size={16} /> Explanation / व्याख्या:
              </h4>
              {(languageMode === 'bilingual' || languageMode === 'hindi') && currentQ.explanation_hi && (
                <p style={{ fontSize: '0.95rem', color: 'var(--text-primary)', marginBottom: '0.5rem', lineHeight: '1.6' }}>
                  {currentQ.explanation_hi}
                </p>
              )}
              {(languageMode === 'bilingual' || languageMode === 'english') && currentQ.explanation_en && (
                <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', fontStyle: 'italic', lineHeight: '1.6' }}>
                  {currentQ.explanation_en}
                </p>
              )}
            </div>
          )}
        </div>

        {/* Test Navigation Footer */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '3rem' }}>
          <button
            className="btn btn-outline"
            onClick={() => setCurrentQIndex(prev => Math.max(0, prev - 1))}
            disabled={currentQIndex === 0}
          >
            <ChevronLeft size={16} /> Previous
          </button>

          {/* Grid of Question Selectors */}
          <div style={{ display: 'flex', gap: '0.35rem', overflowX: 'auto', padding: '0.5rem 0', maxWidth: '60%' }}>
            {questions.map((q, idx) => {
              const hasAns = !!mockAnswers[q.id];
              let cellBg = 'rgba(255,255,255,0.03)';
              let border = '1px solid var(--glass-border)';

              if (idx === currentQIndex) {
                border = '2px solid var(--accent-primary)';
                cellBg = 'rgba(99, 102, 241, 0.1)';
              } else if (reviewMode) {
                const isCorrect = mockAnswers[q.id] === q.correct_answer;
                cellBg = isCorrect ? 'var(--accent-success)' : 'var(--accent-danger)';
                border = 'none';
              } else if (hasAns) {
                cellBg = 'rgba(99, 102, 241, 0.4)';
                border = 'none';
              }

              return (
                <button
                  key={q.id}
                  onClick={() => setCurrentQIndex(idx)}
                  style={{
                    width: '24px',
                    height: '24px',
                    borderRadius: '50%',
                    background: cellBg,
                    border: border,
                    color: hasAns || reviewMode ? '#fff' : 'var(--text-muted)',
                    fontSize: '0.7rem',
                    fontWeight: 700,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    cursor: 'pointer',
                    flexShrink: 0
                  }}
                >
                  {idx + 1}
                </button>
              );
            })}
          </div>

          {currentQIndex === questions.length - 1 && !reviewMode ? (
            <button className="btn btn-primary" onClick={handleMockTestSubmit} style={{ background: 'linear-gradient(135deg, var(--accent-success), #059669)', border: 'none', boxShadow: 'none' }}>
              Submit Mock Test
            </button>
          ) : (
            <button
              className="btn btn-primary"
              onClick={() => setCurrentQIndex(prev => Math.min(questions.length - 1, prev + 1))}
              disabled={currentQIndex === questions.length - 1}
            >
              Next <ChevronRight size={16} />
            </button>
          )}
        </div>
      </div>
    );
  }

  // Test Result view
  if (screenMode === 'testresult' && testResult) {
    const scorePct = testResult.total > 0 ? Math.round((testResult.score / testResult.total) * 100) : 0;

    return (
      <div className="container animate-fade-in" style={{ maxWidth: '750px', textAlign: 'center', padding: '4rem 1.5rem' }}>
        <div className="glass-panel" style={{ padding: '3.5rem 2.5rem' }}>
          <div style={{ display: 'inline-flex', background: 'rgba(16, 185, 129, 0.1)', color: 'var(--accent-success)', padding: '1.5rem', borderRadius: '50%', marginBottom: '1.5rem' }}>
            <Award size={48} />
          </div>

          <h1 className="page-title" style={{ fontSize: '2.25rem', marginBottom: '0.5rem' }}>Mock Test Submitted!</h1>
          <p className="page-subtitle" style={{ marginBottom: '2.5rem' }}>Review your B.S. Negi practice test performance breakdown.</p>

          <div className="stats-grid" style={{ marginBottom: '3rem', gridTemplateColumns: '1fr 1fr' }}>
            <div className="stat-card" style={{ background: 'var(--bg-elevated)', borderRadius: 'var(--radius-lg)', display: 'block', padding: '1.5rem' }}>
              <h3 style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', marginBottom: '0.5rem' }}>Final Score</h3>
              <p className="stat-value gradient-text" style={{ fontSize: '2.5rem' }}>{testResult.score} / {testResult.total}</p>
            </div>

            <div className="stat-card" style={{ background: 'var(--bg-elevated)', borderRadius: 'var(--radius-lg)', display: 'block', padding: '1.5rem' }}>
              <h3 style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', marginBottom: '0.5rem' }}>Accuracy Percentage</h3>
              <p className="stat-value" style={{ fontSize: '2.5rem' }}>{scorePct}%</p>
            </div>
          </div>

          {/* Custom recommendations */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', background: 'rgba(99,102,241,0.05)', border: '1px solid rgba(99,102,241,0.15)', borderRadius: 'var(--radius-md)', padding: '1.25rem', marginBottom: '2.5rem', textAlign: 'left' }}>
            <Info size={24} style={{ color: 'var(--accent-primary)', flexShrink: 0 }} />
            <div>
              <h4 style={{ fontSize: '0.95rem', fontWeight: 700, color: 'var(--text-primary)', marginBottom: '0.15rem' }}>
                {scorePct >= 80 ? 'Excellent Command!' : scorePct >= 50 ? 'Steady Progress!' : 'Needs Revision!'}
              </h4>
              <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', lineHeight: 1.4 }}>
                {scorePct >= 80
                  ? 'Fantastic work! You have shown a stellar understanding of this material. Try full syllabus tests next.'
                  : scorePct >= 50
                    ? 'Good effort. Go through the incorrect answers in Review Mode and re-read the chapter explanation notes.'
                    : 'We suggest returning to the study practice mode for this unit first. Learn chapter concepts before retaking timed mock tests.'}
              </p>
            </div>
          </div>

          <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center' }}>
            <button className="btn btn-outline" onClick={exitToDashboard} style={{ minWidth: '160px' }}>
              Back to Dashboard
            </button>

            <button className="btn btn-primary" onClick={() => {
              setReviewMode(true);
              setScreenMode('mocktest');
              setCurrentQIndex(0);
            }} style={{ minWidth: '160px' }}>
              Review Answers
            </button>
          </div>
        </div>
      </div>
    );
  }

  return null;
};

export default BsNegiPractice;
