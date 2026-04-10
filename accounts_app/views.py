# accounts views.py

from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import SignupSerializer

class SignupView(CreateAPIView):
    queryset = User.objects.all()  # base queryset
    serializer_class = SignupSerializer  # serializer for signup
    permission_classes = [AllowAny]  # allow public access to register