from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField
from django.forms import EmailField, ModelForm
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    """Форма для создания нвоого пользователя"""
    email = EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email Already Exists')

        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        field_classes = {"username": UsernameField}


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']
