from django.core.validators import MaxLengthValidator
from django.db import models

from workerapp.models import Resume
from companyapp.models import Vacancy
from authapp.models import CustomUser
from messageapp.models import Message



# statuses = (
#     (1, 'Не просмотрено'),
#     (2, 'Просмотрено'),
#     (3, 'Отказ'),
#     (4, 'Приглашение')
# )

response_statuses = (
    (1, 'Отказ'),
    (2, 'Приглашение')
)


class MessageOnResume(models.Model): #предложение на резюме
    user = models.ManyToManyField(CustomUser, verbose_name='Пользователь')  # зачем здесь юзер? их же 3 в модели, может permission?
    resume = models.ManyToManyField(Resume, verbose_name='Резюме')
    vacancy = models.ForeignKey(Vacancy, verbose_name='Вакансия', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, verbose_name='Дата предложения')
    message = models.ForeignKey(Message, verbose_name='Отклик', on_delete=models.CASCADE)
    # status = models.CharField(verbose_name='Статус', choices=statuses, default=1)


class LetterToWorker(models.Model): #ответ на отклик работника
    letter = models.TextField(verbose_name='Текст письма',
                            validators=[MaxLengthValidator(limit_value=500,
                                                            message='Превышена максимально допустимая длина')])
    response_status = models.CharField(max_length=500, verbose_name='Статус ответа', choices=response_statuses)
    date = models.DateTimeField(auto_now=True, verbose_name='Дата ответа')
