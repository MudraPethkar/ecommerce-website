from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CheckoutForm, RegisterForm
from .models import Category, Order, OrderItem, Product


def cart_data(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    items = []
    total = Decimal('0.00')
    for product in products:
        quantity = min(int(cart[str(product.id)]), product.stock)
        subtotal = product.price * quantity
        items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
        total += subtotal
    return items, total


def home(request):
    category_slug = request.GET.get('category')
    categories = Category.objects.all()
    
    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)
    else:
        products = Product.objects.all()
    
    return render(request, 'store/home.html', {'products': products, 'categories': categories, 'selected_category': category_slug})


def product_detail(request, slug):
    return render(request, 'store/product_detail.html', {'product': get_object_or_404(Product, slug=slug)})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    key = str(product.id)
    cart[key] = min(int(cart.get(key, 0)) + 1, product.stock)
    request.session['cart'] = cart
    messages.success(request, f'{product.name} added to your cart.')
    return redirect(request.POST.get('next') or 'cart')


def update_cart(request, product_id):
    cart = request.session.get('cart', {})
    quantity = max(0, int(request.POST.get('quantity', 0)))
    product = get_object_or_404(Product, id=product_id)
    if quantity:
        cart[str(product.id)] = min(quantity, product.stock)
    else:
        cart.pop(str(product.id), None)
    request.session['cart'] = cart
    return redirect('cart')


def cart(request):
    items, total = cart_data(request)
    return render(request, 'store/cart.html', {'items': items, 'total': total})


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')
    return render(request, 'store/register.html', {'form': form})


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect(request.GET.get('next', 'home'))
    return render(request, 'store/login.html', {'form': form})


@login_required
def checkout(request):
    items, total = cart_data(request)
    if not items:
        return redirect('cart')
    form = CheckoutForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        with transaction.atomic():
            order = Order.objects.create(user=request.user, total=total, shipping_address=form.cleaned_data['shipping_address'])
            for item in items:
                product = Product.objects.select_for_update().get(id=item['product'].id)
                if item['quantity'] > product.stock:
                    messages.error(request, f'{product.name} is out of stock.')
                    return redirect('cart')
                OrderItem.objects.create(order=order, product=product, quantity=item['quantity'], price=product.price)
                product.stock -= item['quantity']
                product.save(update_fields=['stock'])
        request.session['cart'] = {}
        return redirect('order_success', order_id=order.id)
    return render(request, 'store/checkout.html', {'form': form, 'items': items, 'total': total})


@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'store/order_success.html', {'order': order})


@login_required
def orders(request):
    return render(request, 'store/orders.html', {'orders': request.user.orders.prefetch_related('items')})
