from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from companyapp.models import Vacancy, CompanyCard
from lkworkerapp.models import MessageToVacancy
from lkworkerapp.serializers import MessageToVacancyDetailModelSerializer, \
    MessageToVacancyCommonModelSerializer
from workerapp.models import Resume


class MessageToVacancyModelViewSet(ModelViewSet):
    queryset = MessageToVacancy.objects.all()

    def get_queryset(self):
        user = self.request.user
        card = CompanyCard.objects.filter(user=user).first()
        vacansyes = Vacancy.objects.filter(company_card=card)
        resumes = Resume.objects.filter(worker=user.id)
        return MessageToVacancy.objects.filter(
            Q(user=user) | Q(vacancy__in=vacansyes) | Q(resume__in=resumes))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return MessageToVacancyDetailModelSerializer
        else:
            return MessageToVacancyCommonModelSerializer
