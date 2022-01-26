from rest_framework.serializers import ModelSerializer

from authapp.models import CustomUser
from authapp import models


class CustomUserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'password', 'username', 'email', 'role')

    def create(self, validated_data):
        user = models.CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user
