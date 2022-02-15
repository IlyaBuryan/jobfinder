from collections import OrderedDict
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from authapp.models import CustomUser


class CustomUserModelSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(read_only=True)
    worker = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'password', 'username', 'email', 'role', 'company', 'worker')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')
