from rest_framework.serializers import ModelSerializer

from authapp.models import CustomUser
from authapp import models


class CustomUserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'password', 'username', 'email', 'role')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
