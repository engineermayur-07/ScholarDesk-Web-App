<div align="center">

# 🎓 ScholarDesk — Academic Command Center

**A unified, full-stack web application engineered to streamline student academic life.**

[![Live Website](https://img.shields.io/badge/🌐%20Live%20Website-scholardesk.pythonanywhere.com-38bdf8?style=for-the-badge)](https://scholardesk.pythonanywhere.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.3-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Deployed on PythonAnywhere](https://img.shields.io/badge/Deployed%20on-PythonAnywhere-306998?style=for-the-badge)](https://www.pythonanywhere.com/)

</div>

---

## 📌 Overview

**ScholarDesk** is a student-centric productivity web application built with Python and Flask. It provides a centralized digital workspace where students can manage their academic notes, track deadlines, monitor attendance, calculate SGPA, log expenses, and interact with an AI-powered study assistant — all from a single, clean dashboard interface.

> Built by students, for students — from Sanjivani College of Engineering, Kopargaon.

---

## ✨ Features

### 📝 Notes Engine
Create, organize, and archive lecture notes and study materials within a structured personal cloud notebook. View, add, and purge entries with ease.

### 📅 Task Manager
Schedule and track assignments, project deadlines, and exam milestones. Stay ahead of your academic calendar with a deadline-oriented task management system.

### 📊 Academic Tools
A suite of built-in academic calculators including:
- **SGPA Calculator** — Compute semester GPA from course credits and grade points instantly.
- **Attendance Auditor** — Monitor lecture presence and stay above minimum threshold requirements.
- **Pomodoro Timer** — Study in structured focus intervals to maximize productivity.

### 💳 Expense Tracker
Log, categorize, and audit student expenses. Maintain budget awareness across an entire academic term with a personal finance ledger.

### 🤖 Saathi AI Assistant
An integrated AI-powered chatbot built with **Google Gemini (google-genai)**. Saathi acts as an intelligent study companion — capable of answering curriculum queries, summarizing topics, and providing context-aware academic guidance.

### 🔐 Secure Authentication
Full user authentication system with registration, login, session management, and password reset via contact number verification. Sessions are secured against back-navigation exploits with cache-control headers.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.10+, Flask 3.1.3 |
| **Database** | SQLite (`student_toolkit.db`) |
| **AI / Chatbot** | Google Generative AI (`google-genai 2.6.0`) |
| **Frontend** | HTML5, CSS3 (custom stylesheet), Vanilla JavaScript |
| **Deployment** | PythonAnywhere |
| **Data Validation** | Pydantic 2.13.3 |
| **HTTP Client** | Requests 2.33.0 |

---

## 📁 Project Structure

```
ScholarDesk-Web-App/
│
├── web_app.py              # Main Flask application — routes & UI rendering
├── chatbot.py              # Saathi AI chatbot logic (Google Gemini integration)
├── database_setup.py       # SQLite database initialization and schema setup
├── resources.json          # Static resource data
├── student_toolkit.db      # SQLite database file
├── requirements.txt        # Python dependencies
│
├── features/               # Modular feature blueprints
│   ├── auth.py             # Registration, login, logout, password reset
│   ├── notes.py            # Notes CRUD operations
│   ├── tasks.py            # Task scheduling and management
│   ├── tools.py            # SGPA calculator, attendance auditor, Pomodoro timer
│   └── finance.py          # Expense tracking and ledger management
│
└── static/
    └── style.css           # Global application stylesheet
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- A Google Gemini API key (for the Saathi AI chatbot)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/engineermayur-07/ScholarDesk-Web-App.git
cd ScholarDesk-Web-App
```

**2. Create and activate a virtual environment** *(recommended)*
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure your Gemini API key**

Set your Google Gemini API key as an environment variable or configure it within `chatbot.py`:
```bash
export GEMINI_API_KEY="your_api_key_here"
```

**5. Initialize the database**
```bash
python database_setup.py
```

**6. Run the application**
```bash
python web_app.py
```

The application will be accessible at `http://127.0.0.1:5000`.

---

## 🌐 Live Deployment

The application is live and accessible at:

**[https://www.engineermayur07.pythonanywhere.com](https://www.scholardesk.pythonanywhere.com)**

---

## 📸 Application Pages

| Route | Page |
|---|---|
| `/` | Landing Page |
| `/register` | New User Registration |
| `/login` | Secure Login |
| `/dashboard` | Main Workspace Dashboard |
| `/notes` | Notes Engine Hub |
| `/tasks` | Task Manager |
| `/tools` | Academic Tools (SGPA, Attendance, Pomodoro) |
| `/finance` | Expense Tracker Ledger |
| `/chatbot` | Saathi AI Assistant |
| `/profile` | Student Profile |
| `/reset_password` | Password Recovery |

---

## 👨‍💻 Developers

This project was designed and developed by:

| Developer | Role | Institution |
|---|---|---|
| **Mayur B. Gund** | Developer  | FY B.Tech CSE, Sanjivani College of Engineering |
| **Arjun B. Kadam** | Developer | FY B.Tech CSE, Sanjivani College of Engineering |

---

## 📬 Contact

**Mayur B. Gund**

[![Email](https://img.shields.io/badge/Email-mgund1920%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:mgund1920@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-mgund1920-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/mgund1920)

---

## 📄 License

This project is open-source and available for academic and educational purposes.

---

<div align="center">

Made with dedication at **Sanjivani College of Engineering, Kopargaon** 🎓

</div>
