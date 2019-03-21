from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    # path('validate/', views.validateEmail, name='validate')
    path('validate/', views.validateId, name='validate')
]
