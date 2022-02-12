from django.db import models
from messageapp.models import Message
from companyapp.models import Vacancy
from workerapp.models import Resume
from authapp.models import CustomUser


class MessageToVacancy(models.Model):
    vacancy = models.ManyToManyField(Vacancy, verbose_name='Вакансия')
    user = models.ManyToManyField(CustomUser, verbose_name='Пользователь')
    message = models.ForeignKey(Message, verbose_name='Отклик', on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, verbose_name='Резюме', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True, verbose_name='Дата отклика на вакансию')


class LetterToCompany(models.Model):
    data = models.DateTimeField(auto_now=True, verbose_name='Дата ответа')
    letter_to_company = models.ForeignKey(MessageToVacancy, verbose_name='Ответ на отклик', on_delete=models.CASCADE)
    text = models.TextField(blank=True, verbose_name='Письмо')