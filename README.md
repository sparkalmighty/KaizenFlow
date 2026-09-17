# KaizenFlow — One-Kaizen Gym System

HTML frontend + Python (Flask) backend.

## Project structure

```
KaizenFlow/
├── frontend/
│   ├── index.html      # Landing page
│   ├── login.html      # Log in
│   └── register.html   # Create account
├── backend/
│   ├── app.py          # Flask server (serves the pages)
│   ├── config.py
│   ├── requirements.txt
│   ├── models/         # (next) database models
│   ├── routes/         # (next) API routes
│   ├── services/       # (next) business logic
│   └── utils/
├── .env.example
└── .gitignore
```

## How to run and test page connections

### Option A — Flask (recommended)

```powershell
cd C:\Users\Meia\KaizenFlow\backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open in your browser:

- Landing: http://127.0.0.1:5000/
- Login: http://127.0.0.1:5000/login
- Register: http://127.0.0.1:5000/register

### Option B — Open HTML files directly

Double-click `frontend\index.html`, or right-click → Open with browser.

### What to click to verify links

1. **Landing** → **Log In** → should open login page  
2. **Landing** → **Join Now** → should open register page  
3. On **login** or **register**, click the **One-Kaizen Fitness** logo → should return to landing  
4. Login → **Create account** → register page  
5. Register → **Log in** → login page  

Forms do not save data yet — auth/database comes next.

## Database for later (online hosting)

Use **PostgreSQL** (managed): Neon, Supabase, Railway, or Render.  
Local prototype can use SQLite; do not use SQLite in production.
