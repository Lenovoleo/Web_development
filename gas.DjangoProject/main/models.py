from django.db import models
class BaseOfOil(models.Model):
    title = models.CharField('Название', max_length = 250)
    address = models.CharField('Адрес', max_length = 250)
    buildDate = models.DateField('Год постройки')
    tel = models.CharField('Телефон', max_length = 250)
    dayOfWork = models.CharField('Рабочие дни', max_length = 250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'База'
        verbose_name_plural = 'Базы'
class Worker(models.Model):
    surname = models.CharField('Фамилия', max_length = 250)
    name = models.CharField('Имя', max_length = 250)
    middleName = models.CharField('Отчество', max_length = 250)
    birthDate = models.DateField('Дата рождение')
    address = models.CharField('Адрес', max_length = 250)
    tel = models.CharField('Телефон', max_length = 250)
    mail = models.CharField('Почта', max_length = 250)
    base = models.ForeignKey(BaseOfOil, on_delete=models.CASCADE)

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Clients(models.Model):
    company = models.CharField('Компания', max_length=250)
    surname = models.CharField('Фамилия', max_length=250)
    name = models.CharField('Имя', max_length=250)
    middleName = models.CharField('Отчество', max_length=250)
    address = models.CharField('Адрес', max_length=250)
    tel = models.CharField('Телефон', max_length=250)
    mail = models.CharField('Почта', max_length=250)
    base = models.ForeignKey(BaseOfOil, on_delete=models.CASCADE)

    def __str__(self):
        return self.company


    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'