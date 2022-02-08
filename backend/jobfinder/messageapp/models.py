from django.db import models


class Message(models.Model):
    message = models.TextField(verbose_name='Отклик', blank=True)
    is_viewed = models.BooleanField(default=False, verbose_name='Просмотрено')



