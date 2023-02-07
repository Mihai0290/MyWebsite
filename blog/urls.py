from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('news/', views.news, name='news'),
]