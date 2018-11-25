from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views

register_converter(FourDigitYearConverter, 'yyyy')

app_name = 'shop'

urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year, name='archives_year'),
    path('', views.item_list, name='item_list'),
    path('item/new/', views.item_new, name='item_new'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),
    path('item/<int:id>/edit', views.item_edit, name='item_edit'),
    path('item/<int:id>/remove/', views.item_remove, name='item_remove'),
]
