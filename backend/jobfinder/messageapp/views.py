from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from .models import Message
from .serializers import MessageModelSerializer


class MessageModelViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageModelSerializer


