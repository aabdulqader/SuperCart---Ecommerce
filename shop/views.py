from django.shortcuts import render
from .models import Product
from math import ceil



def index(request):
    products = Product.objects.all()

    num = len(products)
    num_slide = num//4 + ceil(num/4 - num//4)

    all_products = [
        [products, range(1, num_slide), num_slide ],
        [products, range(1, num_slide), num_slide],

    ]
    context = {
        "all_products":all_products,
        
    }
    return render(request, 'shop/shop_index.html', context)



def about(request):
    return render(request, 'shop/shop_about.html')



def contact(request):
    return render(request, 'shop/shop_contact.html')



def search(request):
    return render(request, 'shop/shop_search.html')



def productview(request):
    return render(request, 'shop/shop_productview.html')



def tracker(request):
    return render(request, 'shop/shop_tracker.html')



def checkout(request):
    return render(request, 'shop/shop_checkout.html')