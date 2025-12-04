Backend for *shortcat*, s simple URL shortening service built with Django and Django REST Framework.

## Implementation
* CORS handled with `django-cors-headers`
* Docs generated in various formats with `drf-yasg`
* API models exposed and validated correctly
* Authentication and authorization with `dj-rest-auth` and `django-allauth`

## Setup
1. Clone the repository and navigate to the backend directory:
```bash
git clone https://github.com/shortcat-ssd/backend && cd backend
```

2. Create and activate a virtual environment:

Linux/Mac:
```bash
python -m venv .venv && source .venv/bin/activate
```

Windows:
```bash
python -m venv .venv && .venv\Scripts\activate
```

3. Install poetry and dependencies:
```bash
pip install poetry && poetry install
```

4. Set up environment variables:
Create a `.env` file in the root directory and add the necessary environment variables. You xan refer to `.env.example` for guidance.

5. Apply database migrations:
```bash
python manage.py migrate
```

6. Generate static files:
```bash
python manage.py collectstatic
```

7. (Optional) Create a superuser for admin access:
```bash
python manage.py createsuperuser
```

8. Run the development server:
```bash
python manage.py runserver
```