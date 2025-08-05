from django.shortcuts import render

from product.models import ProductImage, Product

def index(request):
    products = Product.objects.all()[0:5]

    context = {
        'featured_products': products,
    }
    return render(request, 'home.html', context)