from rest_framework.serializers import ModelSerializer
from authapp.serializers import CustomUserModelSerializer
from companyapp.serializers import VacancyModelSerializer
from workerapp.serializers import ResumeModelSerializer
from .models import MessageOnResume


class MessageOnResumeModelSerializer(ModelSerializer):
    user = CustomUserModelSerializer(read_only=True)
    vacancy = VacancyModelSerializer(read_only=True)
    resume = ResumeModelSerializer(read_only=True)

    class Meta:
        model = MessageOnResume
        fields = '__all__'


class MessageOnResumeCommonModelSerializer(ModelSerializer):
    class Meta:
        model = MessageOnResume
        fields = '__all__'
