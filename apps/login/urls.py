from django.urls import path
from .views import LoginView, SignUpView, LogoutView

app_name = "login"

urlpatterns = [
   path('', LoginView.as_view(), name="login"),
   path('signup/', SignUpView.as_view(), name="signup"),
   path('logout/', LogoutView.as_view(), name="logout"),
]