from rest_framework.serializers import ModelSerializer

from .models import MessageOnResume


class MessageOnResumeModelSerializer(ModelSerializer):
    class Meta:
        model = MessageOnResume
        fields = '__all__'
