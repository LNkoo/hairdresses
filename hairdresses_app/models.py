from django.db import models
from django.utils import timezone


class SEX:
    MALE = 'MALE'
    FEMALE = 'FEMALE'

    choices = {
        MALE: 'Чоловіча',
        FEMALE: 'Жіноча',
    }


class Client(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=255)
    surname = models.CharField(verbose_name="Прізвище", max_length=255)
    sex = models.CharField(verbose_name="Стать", choices=SEX.choices.items(), max_length=15)
    sign_regular_customer = models.BooleanField(verbose_name='Постійний клієнт', default=False)

    def __str__(self):
        return '{0} {1}'.format(self.name, self.surname)

    class Meta:
        verbose_name = "клієнт"
        verbose_name_plural = "Клієнти"


class Hairdo(models.Model):
    name = models.CharField(verbose_name='Назва зачіски', max_length=255)
    price = models.FloatField(verbose_name='Вартість')
    sex = models.CharField(verbose_name='Стать', choices=SEX.choices.items(), max_length=15)

    def __str__(self):
        return '{0}'.format(self.name)

    class Meta:
        verbose_name = "зачіска"
        verbose_name_plural = "Зачіски"


class AdditionalService(models.Model):
    name = models.CharField(verbose_name='Назва послуги', max_length=255)
    price = models.FloatField(verbose_name='Вартість')

    def __str__(self):
        return '{0}'.format(self.name)

    class Meta:
        verbose_name = "додаткова послуга"
        verbose_name_plural = "Додаткові послуги"


class Bill(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, verbose_name='Клієнт')
    hairdo = models.ForeignKey(to=Hairdo, on_delete=models.CASCADE, verbose_name='Зачіска')
    additional_services = models.ManyToManyField(to=AdditionalService, verbose_name='Додаткова послуга')
    date = models.DateField(verbose_name='Дата та час', default=timezone.now)

    def __str__(self):
        return 'Замовлення №{0} та його ціна {1}'.format(self.pk, self.total_sum)

    class Meta:
        verbose_name = "рахунок"
        verbose_name_plural = "Рахунки"

    @property
    def total_sum(self):
        sum_od_additional_services = 0
        for ass in self.additional_services.all():
            sum_od_additional_services += ass.price
        return sum_od_additional_services+self.hairdo.price
