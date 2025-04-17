# Insurance Claim Backend (Django)

This is the **backend API** for the e-commerce platform, built using **Django** and **Django REST Framework (DRF)**.

After you have successfully run the backend, you should be able to:
- ✅ Access all the API endpoints at [http://127.0.0.1:8000](http://127.0.0.1:8000)
- ✅ Access the frontend at [http://127.0.0.1:8000](http://127.0.0.1:8000)
## 🚀 Important Notice: Run The Backend Before Running The Frontend
The [**React frontend**](http://127.0.0.1:8000) **will not function properly** without the backend running.  
Before starting the frontend, make sure the **Django server** is up and running.

---

## 📌 1️⃣ Requirements

Ensure you have the following installed:

- **Python** (≥ 3.8)  
- **Django** (≥ 4.0)  
- **Django REST Framework** (DRF)  
- **django-cors-headers** (for CORS handling)  
- **PostgreSQL** (or SQLite for local development)  

## 📌 2️⃣ Development Setup:
```bash
pip install virtualenv
```
```bash
virtualenv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python manage.py migrate
```
```bash
python manage.py collectstatic --no-input
```
```bash
python manage.py createsuperuser
```
```bash
python manage.py runserver 0.0.0.0:8000
```
