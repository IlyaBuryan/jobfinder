from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from authapp.models import CustomUser

from workerapp.models import Worker, Resume


class WorkerTests(APITestCase):
    url = '/api/v1/worker/'

    def setUp(self) -> None:
        self.user = CustomUser.objects.create(username='test_user1', email='test1@mail.ru', password='', role=3)
        self.user.set_password('secret')
        self.user.save()

    def test_get_list_worker(self):
        self.client = APIClient()
        self.client.login(username='test_user1', password='secret')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_create_worker(self):
        self.client = APIClient()
        self.client.login(username='test_user1', password='secret')
        response = self.client.post(f'{self.url}', {
            "first_name": "Иван",
            "last_name": "Иванов",
            "phone": "89375645258",
            "birth_date": "2000-01-01",
            "user": [self.user.id]
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

    def test_edit_worker(self):
        worker = Worker.objects.create(
            first_name="Иван",
            last_name="Иванов",
            phone=89375645258,
            birth_date="2000-01-01",
            user=CustomUser.objects.get(id=1))
        worker.save()

        self.client = APIClient()
        self.client.login(username='test_user1', password='secret')
        response = self.client.put(f'{self.url}{worker.id}/', {
            "first_name": "Иван",
            "last_name": "Иванов",
            "phone": "89379999999",
            "birth_date": "2000-01-01",
            "user": [1],
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        worker = Worker.objects.get(id=worker.id)
        self.assertEqual(worker.phone, 89379999999)
        self.client.logout()

    def test_get_detail_worker(self):
        worker = Worker.objects.create(
            first_name="Иван",
            last_name="Иванов",
            phone=89375645258,
            birth_date="2000-01-01",
            user=CustomUser.objects.get(id=1))
        worker.save()
        self.client = APIClient()
        self.client.login(username='test_user1', password='secret')
        response = self.client.get(f'{self.url}{worker.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def tearDown(self) -> None:
        pass
