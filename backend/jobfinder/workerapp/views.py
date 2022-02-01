from workerapp.serializers import WorkerModelSerializer, ResumeModelSerializer, \
    WorkExperienceModelSerializer
from rest_framework import viewsets
from workerapp.models import Worker


class WorkerModelViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerModelSerializer


class ResumeModelViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = ResumeModelSerializer


class WorkExperienceModelViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkExperienceModelSerializer
