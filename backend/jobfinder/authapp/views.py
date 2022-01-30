from rest_framework import viewsets, generics, status, permissions

from authapp.models import CustomUser
from authapp.serializers import CustomUserModelSerializer, LogoutSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class CustomUserModelViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer
    permission_classes = [AllowAny]


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
