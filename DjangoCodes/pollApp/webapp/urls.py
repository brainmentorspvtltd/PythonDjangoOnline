from django.urls import path, include
from . import views

app_name='pollApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.details, name='detail')
]