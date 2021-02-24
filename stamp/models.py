from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Diller(models.Model):
    plotter_id = models.IntegerField()
    user = models.ForeignKey(User, unique=True, verbose_name='Пользователь', on_delete=models.CASCADE)


class Plotter(models.Model):
    statistics = models.CharField(max_length=1000)
    mold_id = models.IntegerField()
    user = models.ForeignKey(User, unique=True, verbose_name='Пользователь', on_delete=models.CASCADE)


class Mold(models.Model):
    size = models.IntegerField()
    price = models.IntegerField()