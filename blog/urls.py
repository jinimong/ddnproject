from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    re_path(r'^post/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),
]
