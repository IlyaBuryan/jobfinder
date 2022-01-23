from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


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
        (10, 'Энергетика')
    )
    category = models.IntegerField(verbose_name='Отрасль', choices=categories)
    ITN = models.IntegerField(verbose_name='ИНН')
    company_details = models.CharField(verbose_name='Сведения о компании', max_length=5000)
    description = models.CharField(verbose_name='Описание', max_length=5000)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)


class Vacancy(models.Model):
    position = models.CharField(verbose_name='Должность', max_length=30)
    conditions = models.CharField(verbose_name='Условия', max_length=500)
    duties = models.CharField(verbose_name='Обязанности', max_length=500)
    requirements = models.CharField(verbose_name='Требования', max_length=500)
    published_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    company_card = models.ForeignKey(CompanyCard, verbose_name='Организация', on_delete=models.CASCADE)
