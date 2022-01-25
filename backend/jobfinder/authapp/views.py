from rest_framework import viewsets, permissions, generics, status

from authapp.models import CustomUser
from authapp.serializers import CustomUserModelSerializer


class CustomUserModelViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer

