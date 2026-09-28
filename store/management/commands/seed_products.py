from django.core.management.base import BaseCommand
from store.models import Category, Product

CATEGORIES = [
    ('Electronics', 'electronics'),
    ('Beauty', 'beauty'),
    ('Clothes', 'clothes'),
    ('Home Decor', 'home-decor'),
    ('Essentials', 'essentials'),
]

PRODUCTS = [
    # Electronics
    ('Aurora Headphones', 'aurora-headphones', 'Wireless noise-cancelling headphones with a 30-hour battery.', '79.99', 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=700', 25, 'electronics'),
    ('Minimal Backpack', 'minimal-backpack', 'A durable everyday backpack with a padded laptop sleeve.', '54.00', 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=700', 18, 'electronics'),
    ('Desk Lamp', 'desk-lamp', 'Warm, adjustable LED light for your workspace.', '32.50', 'https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=700', 30, 'electronics'),
    
    # Beauty
    ('Organic Face Cream', 'organic-face-cream', 'Hydrating face cream with natural ingredients for all skin types.', '45.00', 'https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=700', 20, 'beauty'),
    ('Luxury Perfume', 'luxury-perfume', 'Premium eau de parfum with exotic floral notes.', '89.99', 'https://images.unsplash.com/photo-1588405748507-c0db3814b519?w=700', 15, 'beauty'),
    ('Hair Care Set', 'hair-care-set', 'Complete shampoo, conditioner, and mask for healthy hair.', '52.00', 'https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=700', 22, 'beauty'),
    ('Makeup Brush Collection', 'makeup-brush-collection', 'Professional 10-piece makeup brush set with soft bristles.', '38.50', 'https://images.unsplash.com/photo-1596462502278-bc52fe00baea?w=700', 16, 'beauty'),
    
    # Clothes
    ('Everyday Sneakers', 'everyday-sneakers', 'Comfortable low-top sneakers for daily adventures.', '68.00', 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=700', 12, 'clothes'),
    ('Casual T-Shirt', 'casual-t-shirt', 'Premium cotton t-shirt perfect for any occasion.', '25.00', 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=700', 35, 'clothes'),
    ('Classic Denim Jeans', 'classic-denim-jeans', 'Timeless denim jeans with perfect fit and comfort.', '65.00', 'https://images.unsplash.com/photo-1582418702059-53c50b63c69f?w=700', 28, 'clothes'),
    ('Wool Cardigan', 'wool-cardigan', 'Warm and cozy wool cardigan for chilly days.', '95.00', 'https://images.unsplash.com/photo-1551028719-00167b16ebc5?w=700', 14, 'clothes'),
    
    # Home Decor
    ('Decorative Throw Pillow', 'decorative-throw-pillow', 'Soft throw pillow with modern geometric patterns.', '35.00', 'https://images.unsplash.com/photo-1582517934482-ba2058bcad35?w=700', 19, 'home-decor'),
    ('Wooden Wall Shelves', 'wooden-wall-shelves', 'Set of 3 floating wooden shelves for your home.', '72.00', 'https://images.unsplash.com/photo-1595502707802-41f6f9d1e14d?w=700', 10, 'home-decor'),
    ('Ceramic Vase Set', 'ceramic-vase-set', 'Handcrafted ceramic vases in earthy tones.', '58.00', 'https://images.unsplash.com/photo-1578500494198-246f612d03b3?w=700', 17, 'home-decor'),
    ('Modern Wall Clock', 'modern-wall-clock', 'Minimalist wall clock with silent movement.', '42.00', 'https://images.unsplash.com/photo-1578500494198-246f612d03b3?w=700', 23, 'home-decor'),
    
    # Essentials
    ('Stainless Steel Water Bottle', 'stainless-steel-water-bottle', 'Keeps beverages hot or cold for 24 hours.', '29.99', 'https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=700', 40, 'essentials'),
    ('Bamboo Cutting Board', 'bamboo-cutting-board', 'Large durable cutting board for kitchen use.', '22.50', 'https://images.unsplash.com/photo-1577720643272-265f434885ee?w=700', 26, 'essentials'),
    ('Kitchen Knife Set', 'kitchen-knife-set', 'Professional 5-piece kitchen knife set.', '67.00', 'https://images.unsplash.com/photo-1593618998160-e34014e67546?w=700', 13, 'essentials'),
    ('Organic Tea Collection', 'organic-tea-collection', 'Assortment of 12 premium organic teas.', '36.00', 'https://images.unsplash.com/photo-1597318972365-7b1e3f8e6e5b?w=700', 31, 'essentials'),
]

class Command(BaseCommand):
    help = 'Create sample categories and products'
    
    def handle(self, *args, **kwargs):
        # Create categories
        for name, slug in CATEGORIES:
            Category.objects.get_or_create(slug=slug, defaults={'name': name})
        
        # Create products
        for name, slug, description, price, image_url, stock, category_slug in PRODUCTS:
            category = Category.objects.get(slug=category_slug)
            Product.objects.update_or_create(
                slug=slug,
                defaults={
                    'name': name,
                    'description': description,
                    'price': price,
                    'image_url': image_url,
                    'stock': stock,
                    'category': category
                }
            )
        
        self.stdout.write(self.style.SUCCESS('Sample categories and products loaded.'))
