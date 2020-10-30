
from django.urls import path
from .views import (
    index, 
    about,
    contact,
    search,
    productview,
    tracker,
    checkout,

)

urlpatterns = [
    path('', index, name='home-shop'),
    path('about', about, name='about-shop'),
    path('contact', contact, name='contact-shop'),
    path('search', search, name='search-shop'),
    path('product-view', productview, name='search-shop'),
    path('tracker', tracker, name='tracking-status-shop'),
    path('checkout', checkout, name='checkout-shop'),
]
