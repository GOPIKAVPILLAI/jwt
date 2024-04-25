from rest_framework import serializers
from core.models import User

from django.core.exceptions import ValidationError
from django.utils import timezone


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','password']