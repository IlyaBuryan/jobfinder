from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from workerapp.models import Worker, Resume, WorkExperience


class WorkerModelSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class WorkExperienceModelSerializer(ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'


class ResumeModelSerializer(serializers.ModelSerializer):
    worker_info = serializers.ReadOnlyField()
    experience = WorkExperienceModelSerializer(read_only=True, many=True)

    class Meta:
        model = Resume
        fields = '__all__'



