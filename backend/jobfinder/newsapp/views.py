from newsapp.serializers import NewsModelSerializer
from rest_framework import viewsets
from newsapp.models import News
from rest_framework.permissions import IsAdminUser


class NewsModelViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsModelSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        return News.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
