from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views

register_converter(FourDigitYearConverter, 'yyyy')

app_name = 'shop'

urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year),
    path('', views.item_list, name='item_list'),
    path('test_jinja/', views.item_list_test_jinja, name='item_list_test_jinja'),    
]
