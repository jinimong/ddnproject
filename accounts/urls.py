from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('login/url/', views.RequestLoginViaUrlView.as_view(), name='request_login_via_url'),
    path('login/<uidb64>/<token>/', views.login_via_url, name='login_via_url'),
    path('password_change/', views.MyPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.MyPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
