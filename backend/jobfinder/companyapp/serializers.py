from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import CompanyCard, Vacancy


class CompanyCardModelSerializer(ModelSerializer):
    class Meta:
        model = CompanyCard
        fields = '__all__'


class VacancyModelSerializer(ModelSerializer):
    company_name = serializers.ReadOnlyField()

    class Meta:
        model = Vacancy
        fields = '__all__'
