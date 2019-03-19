from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('mobiles/',views.mobiles, name='mobiles'),
    path('search/',views.search, name='search'),
    path('register/',views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('about/',views.about, name='about')
]