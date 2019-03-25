from django.urls import path, include
from . import views
appname = 'app'
urlpatterns = [
    path('', views.index, name='index')
]
