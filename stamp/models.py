from django.db import models
from django.contrib.auth.models import User


class Diller(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name_of_dillers')
    statistics_users = models.CharField(verbose_name='Statistics', max_length=100)

    def __str__(self):
        return self.name


class Users(models.Model):
    name_of_user = models.CharField(max_length=255, verbose_name='User_name')
    diller = models.ManyToManyField(Diller, verbose_name='Диллер')

    def __str__(self):
        return self.name_of_user


class Plotter(models.Model):
    diller_id = models.ForeignKey(Diller, verbose_name='Name_of_dillers', on_delete=models.CASCADE)
    user = models.OneToOneField(Users, verbose_name='Пользователь', on_delete=models.CASCADE)
    statistics = models.TextField(max_length=1000, verbose_name='Статистика')
    name_plotter = models.CharField(max_length=255, verbose_name='Название')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name_plotter


class Mold(models.Model):
    name_mold = models.CharField(max_length=255)
    size = models.IntegerField(verbose_name='Размер', default=1)
    price = models.IntegerField(verbose_name='Цена', default=0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    plotter_id = models.ManyToManyField(Plotter, verbose_name='Название')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name_mold
