from django.db import models


class Message(models.Model):
    message = models.TextField(blank=True)


class MessageResume(models.Model):
    message_id = models.CharField(max_length=60)
    resume_id = models.CharField(max_length=60)


class MessageVacansy(models.Model):
    message_id = models.CharField(max_length=60)
    vacansy_id = models.CharField(max_length=60)
