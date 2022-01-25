# Generated by Django 4.0.1 on 2022-01-25 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.IntegerField(choices=[(1, 'Модератор'), (2, 'Работник'), (3, 'Компания')], default='1', verbose_name='Роль'),
        ),
    ]