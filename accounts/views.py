from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import SignupForm


signup = CreateView.as_view(
    model=User,
    form_class=SignupForm,
    success_url=settings.LOGIN_URL,
    template_name='accounts/signup.html')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
