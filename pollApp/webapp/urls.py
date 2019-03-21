from django.urls import path, include
from . import views

app_name='pollApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.details, name='detail'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]