from rest_framework.serializers import ModelSerializer
from authapp.serializers import CustomUserModelSerializer
from companyapp.serializers import VacancyModelSerializer
from workerapp.serializers import ResumeModelSerializer
from rest_framework import serializers

from lkworkerapp.models import MessageToVacancy


class MessageToVacancyDetailModelSerializer(ModelSerializer):
    user = CustomUserModelSerializer(read_only=True)
    vacancy = VacancyModelSerializer(read_only=True)
    resume = ResumeModelSerializer(read_only=True)

    class Meta:
        model = MessageToVacancy
        fields = '__all__'


class MessageToVacancyCommonModelSerializer(ModelSerializer):
    class Meta:
        model = MessageToVacancy
        fields = '__all__'
