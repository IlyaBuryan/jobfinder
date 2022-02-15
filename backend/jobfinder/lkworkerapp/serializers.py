from rest_framework.serializers import ModelSerializer

from lkworkerapp.models import MessageToVacancy, LetterToCompany


class MessageToVacancyModelSerializer(ModelSerializer):
    class Meta:
        model = MessageToVacancy
        fields = '__all__'


class LetterToCompanyModelSerializer(ModelSerializer):
    class Meta:
        model = LetterToCompany
        fields = '__all__'
