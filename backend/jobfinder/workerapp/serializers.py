from rest_framework.serializers import ModelSerializer
from workerapp.models import Worker, Resume, WorkExperience


class WorkerModelSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class ResumeModelSerializer(ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class WorkExperienceModelSerializer(ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'
