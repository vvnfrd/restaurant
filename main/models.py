from email.policy import default

from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Table(models.Model):
    """Модель стола"""

    number = models.IntegerField(unique=True, verbose_name='номер стола', **NULLABLE)
    free = models.BooleanField(default=True, verbose_name='свободный')
    seats = models.PositiveIntegerField(default=4, verbose_name='кол-во мест')
    is_vip = models.BooleanField(default=False, verbose_name='вип статус')

    def __str__(self):
        return f'стол {self.number} {"свободный" if self.free else "занятый"}'

    class Meta:
        verbose_name = 'стол'
        verbose_name_plural = 'столы'


class Booking(models.Model):
    """Модель бронирования"""

    table = models.ForeignKey("Table", on_delete=models.CASCADE,
                              verbose_name='стол', **NULLABLE)
    time_from = models.DateTimeField(verbose_name='бронь с')
    time_to = models.DateTimeField(verbose_name='бронь до')
    client_email = models.EmailField(unique=True, verbose_name='почта клиента')
    client_name = models.CharField(max_length=50, verbose_name='имя клиента')
    client_phone = models.CharField(max_length=11, verbose_name='телефон клиента')
    is_notified = models.BooleanField(default=False, verbose_name='признак уведомления')

    def __str__(self):
        return f'бронь стола {self.table} с {self.time_from} до {self.time_to}'

    class Meta:
        verbose_name = 'бронь'
        verbose_name_plural = 'бронь'

class Content(models.Model):
    """Модель контента"""
    subsequence = models.PositiveIntegerField(default=1, verbose_name='последовательность')
    text1 = models.TextField(verbose_name='текст1', **NULLABLE)
    text2 = models.TextField(verbose_name='текст2', **NULLABLE)
    text3 = models.TextField(verbose_name='текст3', **NULLABLE)
    image = models.ImageField(verbose_name='изображение', **NULLABLE)
    reversed = models.BooleanField(default=False, verbose_name='отзеркалено')

    def __str__(self):
        return f'контент {self.pk}'

    class Meta:
        verbose_name = 'контент'
        verbose_name_plural = 'контент'