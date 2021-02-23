from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Diller(models.Model):
    plotter = models.CharField()
    user = models.ForeignKey(User, unique=True, verbose_name='Пользователь', on_delete=models.CASCADE)


class Plotter(models.Model):
    pass


class Mold(models.Model):
    pass