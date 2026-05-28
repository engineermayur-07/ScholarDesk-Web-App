<div align="center">

# 🎒 Students ToolKit

**An all-in-one CLI-based productivity suite for engineering students**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat&logo=sqlite&logoColor=white)](https://sqlite.org)
[![Gemini AI](https://img.shields.io/badge/Gemini-2.5%20Flash-4285F4?style=flat&logo=google&logoColor=white)](https://ai.google.dev)

*Your academic life, organised in one terminal.*

</div>

---

## 📖 About The Project

**Students ToolKit** is a feature-rich, terminal-based student management system built entirely in Python. Designed for engineering students, it brings together every productivity tool a student needs — from task scheduling and notes to an AI study buddy and expense tracking — all accessible from a single, secure login-protected interface.

Every piece of student data is stored locally in a **SQLite database**, ensuring privacy and offline access with no external accounts required (except for the optional AI chatbot feature).

---

## ✨ Features — 17 Tools in One App

### 🔐 Authentication
- **Student Registration** — sign up with name, email, age, class, and contact info
- **Login / Logout** — password-protected session management

### ✅ Task Management
- **Schedule Tasks** — add tasks with deadlines
- **View Tasks** — see all pending tasks in a list
- **Mark as Completed** — tick off finished tasks
- **View Completed / Incomplete Tasks** — filter by status
- **Delete Tasks** — remove tasks when no longer needed

### 📝 Notes
- **Add Notes** — write and save subject-wise notes
- **View Notes** — browse saved notes
- **Delete Notes** — remove old notes

### 🤖 Saathi AI — AI Study Buddy
- Powered by **Google Gemini 2.5 Flash** via the `google-genai` SDK
- Maintains full conversation context across the session
- Answers concept questions, gives study tips, recommends resources
- Friendly, encouraging, student-first system prompt

### ⏱️ Pomodoro Timer
- Classic 25/5 focus-break timer built into the terminal
- Helps students build productive study sessions

### 📊 Academic Calculators
- **SGPA Calculator** — enter credits and grade points per subject, get instant SGPA
- **Attendance Tracker** — track present vs total lectures per subject, see attendance percentage

### 💰 Expense Tracker
- **Add Expenses** — log daily spending with category and date
- **View Expenses** — review all recorded transactions

### 📚 Study Resources
Built-in curated links for documentation and free PDF notes (via CodeWithHarry) covering:

`Python` `C Programming` `C++` `Java` `JavaScript` `HTML` `CSS` `PHP` `DSA` `SQL` `MySQL` `MongoDB` `Django` `Flask` `SQLite` `Git`

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Database | SQLite 3 (via `sqlite3` standard library) |
| AI Chatbot | Google Gemini 2.5 Flash (`google-genai` SDK) |
| Architecture | Modular — features split across `features/` package |

---

## 📁 Project Structure

```
Students-ToolKit/
│
├── main.py                 # Entry point — login/register menu + main app loop
├── chatbot.py              # Saathi AI — Gemini 2.5 Flash chat session
├── database_setup.py       # SQLite schema initialisation (students, tasks, expenses)
├── resources.json          # Curated study resource links
├── student_toolkit.db      # SQLite database (auto-created on first run)
│
└── features/               # Feature modules
    ├── auth.py             # Registration, login, profile
    ├── tasks.py            # Task CRUD and status management
    ├── notes.py            # Notes CRUD
    ├── finance.py          # Expense tracker
    ├── tools.py            # SGPA calculator, attendance tracker, Pomodoro timer
    └── utility.py          # Resources viewer and shared helpers 
```

---

## 🗄️ Database Schema

```sql
-- Students table
students (email PK, name, password, age, class, contact_info)

-- Tasks table
tasks (id PK AUTOINCREMENT, student_email FK, task, completed, deadline)

-- Expenses table
expenses (id PK AUTOINCREMENT, student_email FK, amount, category, date)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- A Google Gemini API key (free at [aistudio.google.com](https://aistudio.google.com)) — required only for Saathi AI

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/engineermayur-07/Students-ToolKit.git
cd Students-ToolKit

# 2. Install dependencies
pip install google-genai

# 3. Set your Gemini API key as an environment variable
# Windows (PowerShell)
$env:GEMINI_API_KEY = "your_api_key_here"

# macOS / Linux
export GEMINI_API_KEY="your_api_key_here"

# 4. Run the toolkit
python main.py
```

---

## 🖥️ App Flow

```
python main.py
        │
        ├── 1. Register  → enter details → saved to SQLite
        ├── 2. Login     → authenticated session begins
        │       │
        │       ├── View Profile        ├── SGPA Calculator
        │       ├── Schedule Tasks      ├── Attendance Tracker
        │       ├── View Tasks          ├── Expenses Tracker
        │       ├── Mark Completed      ├── View Expenses
        │       ├── Delete Tasks        ├── Saathi AI (Gemini)
        │       ├── Add / View Notes    ├── Pomodoro Timer
        │       ├── Study Resources     └── Logout
        │
        └── 3. Exit
```

---

## 🔒 Security Notice

- Passwords are currently stored as plain text in the SQLite database. For a production version, replace with `bcrypt` or `hashlib` password hashing before sharing with others.
- The Gemini API key is read from an environment variable — never hardcode it in source files.

---

## 🤝 Contributing

Contributions are welcome! Ideas for improvement:
- Password hashing with `bcrypt`
- GUI frontend using `tkinter` or `streamlit`
- Export notes and tasks to PDF
- Timetable / schedule feature

To contribute:

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 👤 Developer

<table>
  <tr>
    <td align="center">
      <b>Mayur B. Gund</b><br>
      FY B.Tech Computer Science Engineering<br><br>
      <a href="https://github.com/engineermayur-07">github.com/engineermayur-07</a>
      <a href="https://linkedin.com/in/mgund1920">LinkedIn</a>
    </td>
  </tr>
</table>

---

 
---

<div align="center">
  <i>Built with ❤️ for students, by a student.</i>
</div>
