from rest_framework.viewsets import ModelViewSet
from .models import CompanyCard, Vacancy
from .serializers import CompanyCardModelSerializer, VacancyModelSerializer


class CompanyCardModelViewSet(ModelViewSet):
    queryset = CompanyCard.objects.all()
    serializer_class = CompanyCardModelSerializer


class VacancyModelViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyModelSerializer
