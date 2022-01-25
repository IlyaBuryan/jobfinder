from rest_framework.serializers import ModelSerializer
from workerapp.models import Worker, Resume, Education


class WorkerModelSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class ResumeModelSerializer(ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class EducationModelSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
