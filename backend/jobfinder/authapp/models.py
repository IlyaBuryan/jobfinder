from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_TYPES = (
    (1, 'Модератор'),
    (2, 'Работник'),
    (3, 'Компания'),
)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.IntegerField(verbose_name='Роль', choices=ROLE_TYPES, null=True)

