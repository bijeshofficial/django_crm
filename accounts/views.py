from django.shortcuts import render
from accounts.models import Product

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request):
    return render(request, 'accounts/customer.html')