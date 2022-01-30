from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from authapp.models import CustomUser
from jobfinder.settings import ADMIN_USER, ADMIN_PASSWORD, ADMIN_ROLE


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            user = CustomUser.objects.create_superuser(
                username=f'{ADMIN_USER}',
                email=f'{ADMIN_USER}@mail.ru',
                password=ADMIN_PASSWORD,
                role=ADMIN_ROLE)
            print(f'{user} создан')
        except IntegrityError:
            print(f'Администратор уже зарегистрирован')
