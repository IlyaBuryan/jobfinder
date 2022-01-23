from rest_framework.serializers import ModelSerializer

from authapp.models import CustomUser


class CustomUserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'password', 'username', 'first_name', 'last_name', 'email', 'role')