from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *

class UserCreationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'