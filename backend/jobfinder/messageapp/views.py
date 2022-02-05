from rest_framework import viewsets

from .models import Message
from .serializers import MessageModelSerializer


class MessageModelViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by()
    serializer_class = MessageModelSerializer


