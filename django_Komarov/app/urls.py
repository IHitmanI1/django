"""
Адресация приложения,
для каждой страницы - свой адрес
"""
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('simple/', views.simple, name='simple'),
    path('map/', views.map, name='map'),
    path('my_form/', views.myform, name='my_form'),
    path('product/', views.product, name='product'),
    path('game/', views.game, name='game'),
    path('new_product/', views.new_product, name='new_product'),
]

