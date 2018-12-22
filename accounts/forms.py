from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].validators = [validate_email]
            self.fields['username'].help_text = 'Enter E-mail Format.'
            self.fields['username'].label = 'E-mail'
            
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = user.username
        if commit:
            user.save()
        return user
