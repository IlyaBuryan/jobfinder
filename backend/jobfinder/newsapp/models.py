from django.db import models
from django.contrib.auth.models import AbstractUser

from authapp.models import CustomUser


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    text = models.CharField(max_length=1000, verbose_name='Текст')
    date_publish = models.DateField(verbose_name='Дата публикации')
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE,
                                related_name='news')
