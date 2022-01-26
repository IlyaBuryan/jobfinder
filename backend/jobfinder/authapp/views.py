from rest_framework import viewsets

from authapp.models import CustomUser
from authapp.serializers import CustomUserModelSerializer
from rest_framework.permissions import AllowAny


class CustomUserModelViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer
    permission_classes = [AllowAny]

