from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase

from companyapp.views import CompanyCardModelViewSet

from authapp.models import CustomUser


class TestCompanyCardViewSet(TestCase):
    url = '/api/v1/companyapp/'

    def setUp(self) -> None:
        self.admin = CustomUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.user = CustomUser.objects.create(username='company', email='company@mai.ru', password='qazwsx', role=3)

    def test_get_list_company_card(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        force_authenticate(request, self.admin)
        view = CompanyCardModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self) -> None:
        pass
