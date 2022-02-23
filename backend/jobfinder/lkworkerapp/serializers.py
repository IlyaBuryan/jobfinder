from rest_framework.serializers import ModelSerializer
from authapp.serializers import CustomUserModelSerializer
from companyapp.serializers import VacancyModelSerializer
from workerapp.serializers import ResumeModelSerializer, WorkerModelSerializer

from lkworkerapp.models import MessageToVacancy, LetterToCompany


class MessageToVacancyModelSerializer(ModelSerializer):
    user = CustomUserModelSerializer(read_only=True)
    vacancy = VacancyModelSerializer(read_only=True)
    resume = ResumeModelSerializer(read_only=True)

    class Meta:
        model = MessageToVacancy
        fields = '__all__'


class LetterToCompanyModelSerializer(ModelSerializer):
    class Meta:
        model = LetterToCompany
        fields = '__all__'
