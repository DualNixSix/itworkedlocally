# accounts serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]  # required signup fields

    def create(self, validated_data):
        return User.objects.create_user(  # ensure password is hashed
            username=validated_data["username"],
            password=validated_data["password"],
        )