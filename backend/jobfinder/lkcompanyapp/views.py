from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from companyapp.models import Vacancy, CompanyCard
from workerapp.models import Resume
from .models import MessageOnResume
from .serializers import MessageOnResumeModelSerializer, \
    MessageOnResumeCommonModelSerializer


class MessageOnResumeModelViewSet(ModelViewSet):
    queryset = MessageOnResume.objects.all()

    def get_queryset(self):
        user = self.request.user
        resumes = Resume.objects.filter(worker=user.id)
        card = CompanyCard.objects.filter(user=user).first()
        vacansyes = Vacancy.objects.filter(company_card=card)
        return MessageOnResume.objects.filter(
            Q(user=user) | Q(resume__in=resumes) | Q(vacancy__in=vacansyes))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return MessageOnResumeModelSerializer
        else:
            return MessageOnResumeCommonModelSerializer
