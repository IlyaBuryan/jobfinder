from rest_framework.serializers import ModelSerializer

from .models import MessageOnResume, LetterToWorker

class MessageOnResumeModelSerializer(ModelSerializer):
    class Meta:
        model = MessageOnResume
        fields = '__all__'


class LetterToWorkerSerializer(ModelSerializer):
    class Meta:
        model = LetterToWorker
        fields = '__all__'