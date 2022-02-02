from rest_framework import serializers

from .models import Message, MessageResume, MessageVacansy


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessageResumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MessageResume
        fields = '__all__'


class MessageVacansySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MessageVacansy
        fields = '__all__'
