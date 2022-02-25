from django.test import TestCase, Client
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase

from .models import CustomUser
from .views import CustomUserModelViewSet


class TestCustomUserViewSet(TestCase):
    url = '/api/v1/user/'

    def setUp(self) -> None:
        self.admin = CustomUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.user = CustomUser.objects.create(username='test_user', email='test@mail.ru', password='qazwsx', role=2)

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        force_authenticate(request, self.admin)
        view = CustomUserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, {'username': 'test_user_x', 'password': 'qazwsx123',
                                          'email': 'mail222@mail.ru', 'role': 2}, format='json')
        force_authenticate(request, self.admin)
        view = CustomUserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        client = APIClient()
        response = client.get(f'{self.url}{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bearer_token(self):
        user = CustomUser.objects.get(id=1)

        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}

    def tearDown(self) -> None:
        pass

