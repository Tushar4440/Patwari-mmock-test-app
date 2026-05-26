# UKSSSC VDO/Patwari AI Mock Test Platform

A full-stack, AI-powered mock test generation platform specifically designed for the **UKSSSC VDO/Patwari Exam (May 17, 2026)**. 

**Live Website:** [https://patwari-mmock-test-app.vercel.app/](https://patwari-mmock-test-app.vercel.app/)

This platform uses the cutting-edge **Google Gemini 2.5 Flash AI** to automatically generate an unlimited number of highly difficult, memory-based mock tests strictly based on the exam syllabus.

## 🌟 Key Features

*   **Unlimited AI Test Generation:** Click a button and the AI acts as an expert exam setter, instantly generating 20-question tests (or full-length 21-question mixed tests).
*   **Zero-Cost "Infinite" Questions:** Optimized to use Google Gemini's generous free tier. By requesting all questions in a single, combined AI prompt, the platform effortlessly avoids strict API rate limits while letting you generate up to 1,500 tests per day for free.
*   **Fully Hindi Localized:** The AI is strictly prompted to return all question text, options, correct answers, and detailed explanations entirely in the Devanagari script (Hindi), matching the exact medium of the actual exam.
*   **Interactive Testing Interface:** A modern, distraction-free environment with a real-time countdown timer, seamless navigation, and instant post-submission grading.
*   **Dynamic Analytics Dashboard:** Visual performance tracking (using Recharts) to analyze your lifetime scores and predict marks based on historical trends.
*   **Premium Glassmorphic UI:** A beautifully designed, modern dark-mode interface built with React, Vanilla CSS, and subtle micro-animations.

## 🏗️ Architecture Stack

This is a modern Full-Stack application split into two distinct environments:

### Frontend (React + TypeScript + Vite)
*   Located in the `/frontend` directory.
*   **Routing:** `react-router-dom` for Single Page Application navigation.
*   **Styling:** Custom Vanilla CSS Design System (`index.css`) featuring glassmorphism (`backdrop-filter`), CSS variables for consistent theming, and responsive flexbox/grid layouts.
*   **Visualization:** `recharts` for the dynamic Area Chart on the dashboard.
*   **Icons:** `lucide-react` for crisp, scalable vector icons.

### Backend (Python Flask + SQLite + SQLAlchemy)
*   Located in the `/backend` directory.
*   **Framework:** Flask serves a RESTful JSON API.
*   **Database:** SQLite integrated via SQLAlchemy ORM. The schema includes models for `User`, `MockTest`, `Question` (which stores the AI explanations), and `TestAttempt`.
*   **AI Integration:** Uses `google-generativeai` and the `gemini-2.5-flash` model. Prompts are carefully engineered to parse structured JSON output.
*   **Security:** Uses `python-dotenv` to securely load the API key from a local `.env` file, preventing accidental exposure of credentials.

## 🚀 How to Run Locally

### Prerequisites
1.  Node.js installed (for frontend).
2.  Python 3.10+ installed (for backend).
3.  A free API key from [Google AI Studio](https://aistudio.google.com/).

### 1. Setup the Backend
1.  Navigate into the backend folder:
    ```bash
    cd backend
    ```
2.  Activate the virtual environment (Windows):
    ```bash
    .\venv\Scripts\activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Create a `.env` file in the `backend` folder and add your key:
    ```env
    GEMINI_API_KEY=your_actual_api_key_here
    ```
5.  Start the Flask server:
    ```bash
    python app.py
    ```
    *The server will run on `http://127.0.0.1:5000`*

### 2. Setup the Frontend
1.  Open a *new* terminal window and navigate into the frontend folder:
    ```bash
    cd frontend
    ```
2.  Install NPM packages:
    ```bash
    npm install
    ```
3.  Start the Vite development server:
    ```bash
    npm run dev
    ```
    *The app will run on `http://localhost:5173`*

## 🔮 Future Roadmap (Currently in Progress)
*   **Test Review & Explanations:** Allowing users to review submitted tests to read the AI's detailed explanation for the correct answers.
*   **Advanced Analytics:** Radar charts mapping out section-by-section accuracy to identify weak points (e.g., strong in Hindi, weak in Uttarakhand GK).
*   **Dynamic Loading Screens:** Premium, engaging loading states while the AI formulates tests.
*   **User Profiles:** Fully functional user accounts to track long-term progress leading up to the May 2026 exam.
