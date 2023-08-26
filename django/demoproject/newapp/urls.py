from django.urls import path, re_path
from . import views

app_name = 'newapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('redirect/', views.myview, name='redirect')
]
