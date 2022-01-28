from django.core.validators import MaxLengthValidator
from django.db import models
from authapp.models import CustomUser

class CompanyCard(models.Model):
    name = models.CharField(verbose_name='Наименование организации', max_length=64)
    categories = (
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
    category = models.IntegerField(verbose_name='Отрасль', choices=categories)
    itn = models.BigIntegerField(verbose_name='ИНН')
    company_details = models.TextField(verbose_name='Сведения о компании', validators=[MaxLengthValidator(limit_value=1000,
                    message='Превышена максимально допустимая длина')])
    description = models.TextField(verbose_name='Описание', validators=[MaxLengthValidator(limit_value=2000,
                    message='Превышена максимально допустимая длина')])
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)


class Vacancy(models.Model):
    position = models.CharField(verbose_name='Должность', max_length=30)
    conditions = models.TextField(verbose_name='Условия', validators=[MaxLengthValidator(limit_value=2500,
                                        message='Превышена максимально допустимая длина')])
    duties = models.TextField(verbose_name='Обязанности', validators=[MaxLengthValidator(limit_value=2500,
                                        message='Превышена максимально допустимая длина')])
    requirements = models.TextField(verbose_name='Требования', validators=[MaxLengthValidator(limit_value=2500,
                                        message='Превышена максимально допустимая длина')])
    published_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    company_card = models.ForeignKey(CompanyCard, verbose_name='Организация', on_delete=models.CASCADE)


