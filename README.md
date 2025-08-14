# URL Shortener — FastAPI
A simple and clean URL Shortener web app built with FastAPI and Tailwind CSS, with a REST API backend and SQLite database.
Accepts a long URL, generates a short code, and redirects users to the original link.

📂 Features

Shorten long URLs into easy-to-share links

Redirect short URLs to their original destination

Tracks click counts for each short link

REST API with Swagger docs (/docs)

Clean, responsive UI built with Tailwind CSS

Dockerized for one-command local start

Public deployment on Render

🚀 Live - https://url-shortener-fastapi-ipec.onrender.com

🛠 Tech Stack

Backend: FastAPI, Python

Frontend: HTML, Tailwind CSS, Jinja2 Templates

Database: SQLite

Deployment: Render

Containerization: Docker, Docker Compose

Quickstart:
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
UI: http://127.0.0.1:8000  
Docs: http://127.0.0.1:8000/docs

Docker:
```bash
docker compose up --build
```
📄 API Endpoints
Shorten URL

POST /shorten/

{
  "original_url": "https://fastapi.tiangolo.com/"
}

Redirect

GET /{short_code} → redirects to original URL

List URLs

GET /shorten/

👨‍💻 Author

Indran Satheesan
Python Developer 
GitHub: indruzz768
