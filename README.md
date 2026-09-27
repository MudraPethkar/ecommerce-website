# Northstar Store

A basic ecommerce website built with Django, SQLite, HTML, CSS, and JavaScript.

## Features
- Product catalog and product detail pages
- Session-based shopping cart with quantity updates
- User registration, login, and logout
- Checkout and order processing with stock validation
- Order history
- Django admin for managing products and orders

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_products
python manage.py createsuperuser
python manage.py runserver
```

Visit http://127.0.0.1:8000/ and use `/admin/` to manage the catalog. For production, move `SECRET_KEY` to an environment variable, set `DEBUG=False`, configure `ALLOWED_HOSTS`, and use a production database.
