from django.db import models
from authapp.serializers import CustomUserModelSerializer

from authapp.models import CustomUser


class Worker(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.BigIntegerField(verbose_name='Телефон')
    birth_date = models.DateField(verbose_name='Дата Рождения')
    user = models.OneToOneField(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE,
                                related_name='worker')


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
    info = models.TextField(verbose_name='Дополнительная информация')
    is_draft = models.BooleanField(default="false", verbose_name='Черновик')
    worker = models.ForeignKey(CustomUser, verbose_name="Сотрудник", on_delete=models.CASCADE)

    @property
    def worker_info(self):
        id_user = CustomUserModelSerializer(self.worker).data['id']
        user_card = Worker.objects.filter(user=id_user).first()
        data = {
            'first_name': user_card.first_name,
            'last_name': user_card.last_name,
            'phone': user_card.phone
        }
        return data


class WorkExperience(models.Model):
    organization = models.CharField(verbose_name='организация', max_length=128)
    start = models.DateField(verbose_name='начало работы')
    end = models.DateField(verbose_name='окончание работы')
    position = models.CharField(verbose_name='должность', max_length=64)
    functions = models.TextField(verbose_name='обязанности', blank=True)
    resume = models.ManyToManyField(Resume, verbose_name="Опыт работы", related_name="experience")
