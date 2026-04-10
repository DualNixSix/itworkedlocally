# accounts urls.py

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import SignupView

urlpatterns = [
    path("signup/", SignupView.as_view()),  # create new user
    path("token/", obtain_auth_token),  # exchange credentials for token
]