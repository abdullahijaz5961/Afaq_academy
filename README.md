# Afaq Academy — Website

Django-based website for Afaq Academy, Rahim Yar Khan. Pages: Home, About, Admissions 2026–27, Contact.

## Local Development

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Deploy on Render (Free)

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Settings:
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn afaq_academy.wsgi:application`
   - **Environment:** Python 3
5. Add Environment Variables:
   - `SECRET_KEY` → generate a random string
   - `DEBUG` → `False`
   - `ALLOWED_HOSTS` → `your-app-name.onrender.com`
6. Click **Deploy**

## GitHub Codespaces

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Then open the forwarded port in the browser.

## Project Structure

```
afaq_academy/
├── afaq_academy/       # Django settings & wsgi
├── afaq_app/           # Views & URLs
├── templates/          # HTML templates (home, about, admissions, contact)
├── static/             # CSS, JS
├── requirements.txt    # Python dependencies
├── render.yaml         # Render config
├── build.sh            # Render build script
└── Procfile            # Gunicorn start
```
