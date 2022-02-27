from newsapp.serializers import NewsModelSerializer
from rest_framework import viewsets
from newsapp.models import News
from rest_framework.permissions import AllowAny


class NewsModelViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsModelSerializer
    permission_classes = [AllowAny]
