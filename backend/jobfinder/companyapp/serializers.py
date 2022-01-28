from rest_framework.serializers import ModelSerializer

from .models import CompanyCard, Vacancy

class CompanyCardModelSerializer(ModelSerializer):
    class Meta:
        model = CompanyCard
        fields = '__all__'


class VacancyModelSerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'