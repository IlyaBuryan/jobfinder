from rest_framework.viewsets import ModelViewSet
from lkworkerapp.models import MessageToVacancy, LetterToCompany
from lkworkerapp.serializers import MessageToVacancyModelSerializer, \
    LetterToCompanyModelSerializer
from companyapp.models import Vacancy, CompanyCard
from django.db.models import Q


class MessageToVacancyModelViewSet(ModelViewSet):
    queryset = MessageToVacancy.objects.all()
    serializer_class = MessageToVacancyModelSerializer

    def get_queryset(self):
        user = self.request.user
        card = CompanyCard.objects.filter(user=user).first()
        vacansyes = Vacancy.objects.filter(company_card=card)
        return MessageToVacancy.objects.filter(Q(user=user) | Q(vacancy__in=vacansyes))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class LetterToCompanyModelViewSet(ModelViewSet):
    queryset = LetterToCompany.objects.all()
    serializer_class = LetterToCompanyModelSerializer
