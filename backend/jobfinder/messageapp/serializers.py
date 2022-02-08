from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Message


class MessageModelSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


