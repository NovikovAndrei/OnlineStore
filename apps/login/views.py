from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib.auth.models import User


class LoginView(View):
    """Отображение авторизации пользователя"""

    def get(self, request):
        return render(request, 'login/login.html')

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:index')
        return render(request, 'login/login.html', {"error": form.errors.get("__all__")})


class LogoutView(View):
    """Функционал выхода из приложения"""
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('home:index')


class SignUpView(View):
    """Функционал авторизации пользователя"""

    def get(self, request):
        form = CustomUserCreationForm()
        profile_form = UserProfileForm()
        return render(request, 'login/signup.html', {'form': form, 'profile_form': profile_form})

    def post(self, request):
        form = CustomUserCreationForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid() and profile_form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username=username, email=email, password=password)

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user, 'django.contrib.auth.backends.ModelBackend')
            return redirect('home:index')

        return render(request, 'login/signup.html', {"form": form, "profile_form": profile_form, "errors": form.errors})
