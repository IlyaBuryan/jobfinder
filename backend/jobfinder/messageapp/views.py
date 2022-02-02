from rest_framework import viewsets

from .models import Message, MessageResume, MessageVacansy
from .serializers import MessageSerializer, MessageResumeSerializer, MessageVacansySerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by()
    serializer_class = MessageSerializer


class MessageResumeViewSet(viewsets.ModelViewSet):
    queryset = MessageResume.objects.all().order_by()
    serializer_class = MessageResumeSerializer


class MessageVacansyViewSet(viewsets.ModelViewSet):
    queryset = MessageVacansy.objects.all().order_by()
    serializer_class = MessageVacansySerializer
