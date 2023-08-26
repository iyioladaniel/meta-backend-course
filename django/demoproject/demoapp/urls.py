from django.urls import path, re_path
from . import views

app_name = 'demoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home),
    path('getuser/<name>/<int:age>/<id>', views.pathview, name='pathview'),
    path("getuser/", views.queryview, name='queryview'),
    path('showform/', views.showform, name='showform'),
    path('getform/', views.getform, name='getform'),
    path('dishes/<str:dish>', views.menuitems, name='dishes'), #dish=pasta
    path('drinks/<str:drink_name>', views.drinks, name='drink_name'),
    re_path(r'^menu_item/([0-9]{2})/$', views.display_menu_item), #what I used originally, but it still worked sha.
    re_path(r'^menu_item/(?P<menu_id>[0-9]{2})/$', views.display_menu_item),
    path('login/', views.login, name='login'),
]
