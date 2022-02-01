from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import CompanyCard, Vacancy
from .serializers import CompanyCardModelSerializer, VacancyModelSerializer


class CompanyCardModelViewSet(ModelViewSet):
    queryset = CompanyCard.objects.all()
    serializer_class = CompanyCardModelSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        return CompanyCard.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class VacancyModelViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyModelSerializer


class CategoriesViewSet(ViewSet):

    def list(self, request):
        companies = CompanyCard.objects.filter().first()
        return Response(companies.get_categories())