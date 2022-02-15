from django.core.validators import MaxLengthValidator
from django.db import models
from authapp.models import CustomUser

categories_choices = (
    (1, 'Автомобильный бизнес'),
    (2, 'Гостиницы, рестораны, общепит, кейтеринг'),
    (3, 'Государственные организации'),
    (4, 'Добывающая отрасль'),
    (5, 'ЖКХ'),
    (6, 'Строительство, недвижимость, эксплуатация, проектирование'),
    (7, 'Услуги для бизнеса'),
    (8, 'Финансовый сектор'),
    (9, 'Электроника, приборостроение, бытовая техника, компьютеры и оргтехника'),
    (10, 'Энергетика'),
    (11, 'Другое')
)


class CompanyCard(models.Model):
    name = models.CharField(verbose_name='Наименование организации', max_length=64)
    categories = categories_choices
    category = models.IntegerField(verbose_name='Отрасль', choices=categories)
    itn = models.BigIntegerField(verbose_name='ИНН', unique=True)
    company_details = models.TextField(verbose_name='Сведения о компании', validators=[MaxLengthValidator(limit_value=1000,
                    message='Превышена максимально допустимая длина')])
    description = models.TextField(verbose_name='Описание', validators=[MaxLengthValidator(limit_value=2000,
                    message='Превышена максимально допустимая длина')])
    user = models.OneToOneField(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='company')


class Vacancy(models.Model):
    position = models.CharField(verbose_name='Должность', max_length=30)
    conditions = models.TextField(verbose_name='Условия', validators=[MaxLengthValidator(limit_value=2500,
                                        message='Превышена максимально допустимая длина')])
    duties = models.TextField(verbose_name='Обязанности', validators=[MaxLengthValidator(limit_value=2500,
                                        message='Превышена максимально допустимая длина')])
    requirements = models.TextField(verbose_name='Требования', validators=[MaxLengthValidator(limit_value=2500,
                                        message='Превышена максимально допустимая длина')])
    salary = models.CharField(verbose_name='Зарплата', max_length=64, null=True, blank=True)
    city = models.CharField(verbose_name='Город', max_length=64, null=True, blank=True)
    published_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    company_card = models.ForeignKey(CompanyCard, verbose_name='Организация', on_delete=models.CASCADE)