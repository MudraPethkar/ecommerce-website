# Northstar Store

A modern ecommerce website built with Django, SQLite, HTML, CSS, and JavaScript.

**Live Demo:** http://localhost:8001/

## Features
- **Product Catalog**: Browse products across Electronics, Clothes, Home Decor, and Essentials
- **Category Filtering**: Left sidebar navigation with category filtering
- **Product Images**: High-quality Unsplash images for all products
- **Website Logo**: Custom SVG logo in header
- **Responsive Design**: Mobile-friendly sidebar navigation
- **Shopping Cart**: Session-based shopping cart with quantity updates
- **User Accounts**: Registration, login, and logout functionality
- **Checkout**: Order processing with stock validation
- **Order History**: View past orders
- **Admin Panel**: Django admin for managing products, categories, and orders

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

Visit http://localhost:8001/ to view the website and use `/admin/` to manage the catalog.

## Database
The database is pre-seeded with 15 products across 4 categories:
- **Electronics**: Headphones, Backpack, Desk Lamp
- **Clothes**: Sneakers, T-Shirt, Denim Jeans, Wool Cardigan
- **Home Decor**: Throw Pillow, Wall Shelves, Ceramic Vase, Wall Clock
- **Essentials**: Water Bottle, Cutting Board, Knife Set, Tea Collection
