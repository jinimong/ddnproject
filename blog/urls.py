from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    re_path(r'^post/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    re_path(r'^post/(?P<id>\d+)/publish/$', views.post_publish, name='post_publish'),
    re_path(r'^post/(?P<id>\d+)/remove/$', views.post_remove, name='post_remove'),
    re_path(r'^post/(?P<id>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^comment/(?P<id>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    re_path(r'^comment/(?P<id>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
