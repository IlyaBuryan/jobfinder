from django.shortcuts import render
from rest_framework import generics

from rest_framework.viewsets import ModelViewSet
from .models import CompanyCard, Vacancy
from .serializers import CompanyCardModelSerializer, VacancyModelSerializer


class CompanyCardModelViewSet(ModelViewSet):
    queryset = CompanyCard.objects.all()
    serializer_class = CompanyCardModelSerializer


class CompanyCardListView(generics.ListAPIView):
    queryset = CompanyCard.objects.all()
    serializer_class = CompanyCardModelSerializer


class CompanyCardCreateView(generics.CreateAPIView):
    queryset = CompanyCard.objects.all()
    serializer_class = CompanyCardModelSerializer


class CompanyCardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyCard.objects.all()
    serializer_class = CompanyCardModelSerializer





class VacancyModelViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyModelSerializer


class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyModelSerializer


class VacancyCreateView(generics.CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyModelSerializer


class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyModelSerializer