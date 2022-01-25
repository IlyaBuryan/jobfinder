from django.db import models
from django.contrib.auth.models import AbstractUser

from authapp.models import CustomUser


class Worker(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, verbose_name='ID')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    birth_date = models.DateField(verbose_name='Дата Рождения')
    user_id = models.ForeignKey(CustomUser, verbose_name="Пользователь", on_delete=models.DO_NOTHING)


class Education(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, verbose_name='ID')
    name = models.CharField(max_length=100, verbose_name='Образование')


class Resume(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, verbose_name='ID')
    position = models.CharField(max_length=100, verbose_name='Должность')
    education = models.ForeignKey(Education, verbose_name="Образование", on_delete=models.DO_NOTHING)
    institution = models.CharField(max_length=100, verbose_name='Учебное заведение')
    courses = models.CharField(max_length=100, verbose_name='Курсы')
    work_experience = models.IntegerField(verbose_name='Курсы')
    info = models.TextField(verbose_name='Дополнительная информация')
    is_draft = models.BooleanField(default="false", verbose_name='Черновик')
    worker_id = models.ForeignKey(Worker, verbose_name="Сотрудник", on_delete=models.CASCADE)
