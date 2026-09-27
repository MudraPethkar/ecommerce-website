from django.core.management.base import BaseCommand
from store.models import Product

PRODUCTS = [
    ('Aurora Headphones', 'aurora-headphones', 'Wireless noise-cancelling headphones with a 30-hour battery.', '79.99', 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=700', 25),
    ('Minimal Backpack', 'minimal-backpack', 'A durable everyday backpack with a padded laptop sleeve.', '54.00', 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=700', 18),
    ('Desk Lamp', 'desk-lamp', 'Warm, adjustable LED light for your workspace.', '32.50', 'https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=700', 30),
    ('Everyday Sneakers', 'everyday-sneakers', 'Comfortable low-top sneakers for daily adventures.', '68.00', 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=700', 12),
]

class Command(BaseCommand):
    help = 'Create sample products'
    def handle(self, *args, **kwargs):
        for name, slug, description, price, image_url, stock in PRODUCTS:
            Product.objects.update_or_create(slug=slug, defaults=locals())
        self.stdout.write(self.style.SUCCESS('Sample products loaded.'))
