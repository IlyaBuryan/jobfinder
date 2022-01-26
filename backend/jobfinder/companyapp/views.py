from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import CompanyCard, Vacancy
from .serializers import CompanyCardModelSerializer, VacancyModelSerializer


class CompanyCardModelViewSet(ModelViewSet):
    queryset = CompanyCard.objects.all()
    serializer_class = CompanyCardModelSerializer
    permission_classes = [AllowAny]


class VacancyModelViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyModelSerializer
