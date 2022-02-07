from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import MessageOnResume, LetterToWorker
from .serializers import MessageOnResumeModelSerializer, LetterToWorkerSerializer


class MessageOnResumeModelViewSet(ModelViewSet):
    queryset = MessageOnResume.objects.all()
    serializer_class = MessageOnResumeModelSerializer

    def get_queryset(self):
        user = self.request.user
        return MessageOnResume.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class LetterToWorkerModelViewSet(ModelViewSet):
    queryset = LetterToWorker.objects.all()
    serializer_class = LetterToWorkerSerializer

