from django.urls import path, re_path
from . import views

app_name = 'littlelemon'
urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
]
