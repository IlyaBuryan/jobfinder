from django.db import models
from django.contrib.auth.models import AbstractUser

from authapp.models import CustomUser


class Worker(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.BigIntegerField(max_length=20, verbose_name='Телефон')
    birth_date = models.DateField(verbose_name='Дата Рождения')
    user = models.OneToOneField(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='worker')


class WorkExperience(models.Model):
    organization = models.CharField(verbose_name='организация', max_length=128)
    start = models.DateField(verbose_name='начало работы')
    end = models.DateField(verbose_name='окончание работы')
    position = models.CharField(verbose_name='должность', max_length=64)
    functions = models.TextField(verbose_name='обязанности', blank=True)


class Resume(models.Model):
    position = models.CharField(max_length=100, verbose_name='Должность')
    types = (
        (1, 'Среднее'),
        (2, 'Среднее профессиональное'),
        (3, 'Высшее'),
    )
    education_types = models.IntegerField(verbose_name='Образование', choices=types)
    institution = models.CharField(max_length=100, verbose_name='Учебное заведение')
    courses = models.CharField(max_length=100, verbose_name='Курсы')
    work_experience = models.ForeignKey(WorkExperience, verbose_name="Опыт работы", on_delete=models.CASCADE)
    info = models.TextField(verbose_name='Дополнительная информация')
    is_draft = models.BooleanField(default="false", verbose_name='Черновик')
    worker_id = models.ForeignKey(Worker, verbose_name="Сотрудник", on_delete=models.CASCADE)
