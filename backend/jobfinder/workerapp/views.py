from workerapp.serializers import WorkerModelSerializer, ResumeModelSerializer, \
    WorkExperienceModelSerializer
from rest_framework import viewsets, generics
from workerapp.models import Worker, Resume, WorkExperience


class WorkerModelViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerModelSerializer

    def get_queryset(self):
        user = self.request.user
        return Worker.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class WorkerListView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerModelSerializer


class ResumeModelViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeModelSerializer


class WorkExperienceModelViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceModelSerializer
