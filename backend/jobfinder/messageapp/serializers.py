from rest_framework import serializers

from .models import Message


class MessageModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


