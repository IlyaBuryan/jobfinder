from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from authapp.models import CustomUser

from companyapp.models import CompanyCard, Vacancy


class CompanyCardTests(APITestCase):
    url = '/api/v1/companyapp/'

    def setUp(self) -> None:
        self.user = CustomUser.objects.create(username='test_user1', email='test1@mail.ru', password='', role=3)
        self.user.set_password('secret')
        self.user.save()

    def test_get_list_company(self):
        self.client = APIClient()
        self.client.login(username='test_user1', password='secret')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_create_company(self):
        self.client = APIClient()
        self.client.login(username='test_user1', password='secret')
        response = self.client.post(f'{self.url}', {
            "name": "Титул",
            "category": "2",
            "itn": "2334567",
            "company_details": "Адрес, реквизиты",
            "description": "Логистика",
            "user": [self.user.id]
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

    def test_edit_company(self):
        company = CompanyCard.objects.create(
            name="ООО СФЕРА",
            category="3",
            itn="23454567",
            company_details="Адрес, реквизиты",
            description="ЖКХ",
            user=CustomUser.objects.get(id=1))
        company.save()

        self.client = APIClient()
        self.client.login(username='test_user1', password='secret')
        response = self.client.put(f'{self.url}{company.id}/', {
            "name": "Титул",
            "category": "2",
            "itn": "2334567",
            "company_details": "Адрес, реквизиты, телефон",
            "description": "Логистика",
            "user": [1],
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        company = CompanyCard.objects.get(id=company.id)
        self.assertEqual(company.company_details, "Адрес, реквизиты, телефон")
        self.client.logout()

    def test_get_detail_company(self):
        company = CompanyCard.objects.create(
            name="ООО ЖИЗНЬ",
            category="4",
            itn="54544567",
            company_details="Адрес, реквизиты",
            description="ЖКХ",
            user=CustomUser.objects.get(id=1))
        company.save()
        self.client = APIClient()
        self.client.login(username='test_user1', password='secret')
        response = self.client.get(f'{self.url}{company.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def tearDown(self) -> None:
        pass


class VacancyTests(APITestCase):
    url = '/api/v1/vacancyapp/'

    def setUp(self) -> None:
        self.user = CustomUser.objects.create(username='test_user1', email='test1@mail.ru', password='', role=3)
        self.user.set_password('secret')
        self.user.save()

        self.company = CompanyCard.objects.create(
            name="ООО СФЕРА",
            category="3",
            itn="23454567",
            company_details="Адрес, реквизиты",
            description="ЖКХ",
            user=CustomUser.objects.get(id=1))
        self.company.save()

    def test_get_list_vacancy(self):
        self.client = APIClient()
        self.client.login(username='test_user1', password='secret')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_create_vacancy(self):
        self.client = APIClient()
        self.client.login(username='test_user1', password='secret')
        response = self.client.post(f'{self.url}', {
            "position": "Программист",
            "conditions": "Условия",
            "duties": "Обязанности",
            "requirements": "Требования",
            "salary": "50000",
            "city": "Москва",
            "published_date": "2022-02-15",
            "company_card": [1]
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

    def test_edit_vacancy(self):
        vacancy = Vacancy.objects.create(
            position="Программист",
            conditions="Условия",
            duties="Обязанности",
            requirements="Требования",
            salary="50000",
            city="Москва",
            published_date="2022-02-15",
            company_card=CompanyCard.objects.get(id=1))
        vacancy.save()

        self.client = APIClient()
        self.client.login(username='test_user1', password='secret')
        response = self.client.put(f'{self.url}{vacancy.id}/', {
            "position": "Программист",
            "conditions": "Условия",
            "duties": "Обязанности",
            "requirements": "Требования",
            "salary": "100000",
            "city": "Москва",
            "published_date": "2022-02-15",
            "company_card": [1]
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        vacancy = Vacancy.objects.get(id=vacancy.id)
        self.assertEqual(vacancy.salary, "100000")
        self.client.logout()

    def test_get_detail_vacancy(self):
        vacancy = Vacancy.objects.create(
            position="Программист",
            conditions="Условия",
            duties="Обязанности",
            requirements="Требования",
            salary="50000",
            city="Москва",
            published_date="2022-02-15",
            company_card=CompanyCard.objects.get(id=1))
        vacancy.save()

        self.client = APIClient()
        self.client.login(username='test_user1', password='secret')
        response = self.client.get(f'{self.url}{vacancy.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def tearDown(self) -> None:
        pass
