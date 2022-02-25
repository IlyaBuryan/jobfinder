from django.db import models

from authapp.models import CustomUser
from companyapp.models import Vacancy
from workerapp.models import Resume

response_statuses = (
    (1, 'Отказ'),
    (2, 'Приглашение')
)


class MessageOnResume(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, verbose_name='Резюме',
                               on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, verbose_name='Вакансия',
                                on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, verbose_name='Дата предложения')
    message = models.TextField(verbose_name='Отклик', blank=True)
    is_viewed = models.BooleanField(default=False, verbose_name='Просмотрено')
    response_status = models.CharField(verbose_name='Статус ответа',
                                       choices=response_statuses,
                                       blank=True,
                                       max_length=1)
