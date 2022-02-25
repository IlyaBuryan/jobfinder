from django.db import models
from messageapp.models import Message
from companyapp.models import Vacancy
from workerapp.models import Resume
from authapp.models import CustomUser


class MessageToVacancy(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)
    vacancy = models.ManyToManyField(Vacancy, verbose_name='Вакансия')
    resume = models.ForeignKey(Resume, verbose_name='Резюме', on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True, verbose_name='Дата отклика на вакансию')
    message = models.TextField(verbose_name='Отклик', blank=True)
    is_viewed = models.BooleanField(default=False, verbose_name='Просмотрено')


class LetterToCompany(models.Model):
    data = models.DateField(auto_now_add=True, verbose_name='Дата ответа')
    letter_to_company = models.ForeignKey(MessageToVacancy, verbose_name='Ответ на отклик', on_delete=models.CASCADE)
    text = models.TextField(blank=True, verbose_name='Письмо')
