# 🧠 Smart Resume Analyzer & Job Matcher

A Django-based web application that allows users to upload resumes, intelligently analyzes them using AI/NLP techniques, and recommends the most suitable job opportunities.

## 🚀 Features

- 📁 Upload resumes (PDF/DOCX)
- 🧠 Extract information using NLP (skills, experience, education)
- 🔍 Match extracted data with job listings
- 💼 Recommend relevant jobs based on profile
- 📝 Suggest improvements to resumes (optional AI module)
- 🔐 Admin panel for managing job listings and feedback

---

## 🛠 Tech Stack

| Layer         | Tools/Tech                                      |
|---------------|-------------------------------------------------|
| Backend       | Django, Python                                  |
| Frontend      | HTML, CSS, Bootstrap, JavaScript                |
| AI/NLP        | spaCy, scikit-learn, pandas, numpy              |
| Database      | SQLite (dev), PostgreSQL (prod)                 |
| File Parsing  | PyMuPDF (PDF), python-docx (DOCX)               |
| Deployment    | GitHub, Heroku/Vercel (future), GitHub Actions |

---

## 📂 Project Structure
smart_resume_matcher/
│
├── resumeapp/ # Main app for resume analysis
├── smartmatcher/ # Django project settings
├── media/ # Uploaded resumes
├── templates/ # HTML templates
├── static/ # Static files (CSS/JS/images)
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md

## ⚙️ Installation & Setup

1. **Clone the Repository**
git clone https://github.com/patilhrishikesh/smart_resume_matcher.git
cd smart_resume_matcher

Create & Activate Virtual Environment

python -m venv myenv
myenv\Scripts\activate   # On Windows

Run Migrations
python manage.py makemigrations
python manage.py migrate

Start Development Server
python manage.py runserver

🔮 Upcoming Features
AI-based resume score & suggestions
User authentication (login/signup)
Admin dashboard with analytics
Job scraping from online portals

🤝 Contributing
Contributions, issues and feature requests are welcome!
Feel free to fork this project and submit a pull request.
