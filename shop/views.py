from django.shortcuts import render, HttpResponse




def index(request):
    return render(request, 'shop/shop_index.html')



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