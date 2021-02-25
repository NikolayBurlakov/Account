from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Diller(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name_of_dillers')
    user = models.ManyToManyField(User, verbose_name='Пользователь')
    statistics_users = models.CharField(verbose_name='Statistics', max_length=100)

    def __str__(self):
        return self.name


class Plotter(models.Model):
    diller_id = models.ForeignKey(Diller, verbose_name='diller_id', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    statistics = models.TextField(max_length=1000, verbose_name='Статистика')
    name = models.CharField(max_length=255, verbose_name='Название')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Mold(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField(verbose_name='Размер', default=1)
    price = models.IntegerField(verbose_name='Цена', default=0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    plotter_id = models.ManyToManyField(Plotter, verbose_name='plotter_id')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name