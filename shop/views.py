from django.shortcuts import render
from math import ceil
from .models import Product, Contact



def index(request):
    # products = Product.objects.all()

    # num = len(products)
    # num_slide = num//4 + ceil(num/4 - num//4)

    # all_products = [
    #     [products, range(1, num_slide), num_slide ],
    #     [products, range(1, num_slide), num_slide],

    # ]

    all_products = []
    products_category = Product.objects.values('category', 'id')
    categories = {item["category"] for item in products_category }
    for cat in categories:
        products = Product.objects.filter(category=cat)
        num = len(products)
        num_slide = num//4 + ceil(num/4 - num//4)
        all_products.append([products, range(1, num_slide), num_slide])

    context = {
        "all_products":all_products,
        
    }


    return render(request, 'shop/shop_index.html', context)



def about(request):     
    return render(request, 'shop/shop_about.html')



def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        instance = Contact(name=name, email=email, phone=phone, subject=subject, message=message )
        instance.save()
    return render(request, 'shop/shop_contact.html')



def search(request):
    return render(request, 'shop/shop_search.html')



def productview(request, p_id):
    product = Product.objects.filter(id=p_id)
    context = {
        'product':product[0]
    }
    return render(request, 'shop/shop_productview.html', context)



def tracker(request):
    return render(request, 'shop/shop_tracker.html')



def checkout(request):
    return render(request, 'shop/shop_checkout.html')