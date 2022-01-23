from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    ROLE_TYPES = (
        (1, 'Администратор'),
        (2, 'Работник'),
        (3, 'Компания'),
    )
    role = models.IntegerField(verbose_name='Роль', choices=ROLE_TYPES, default='1')
