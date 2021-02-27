from django.db import models
from django.contrib.auth.models import User as DefaultUser, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.permissions import BasePermission


class User(DefaultUser):
    login_user = models.CharField(max_length=255, default='', verbose_name='Login name')

    def __str__(self):
        return self.login_user


class Diller(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name_of_dillers')
    statistics_User = models.CharField(verbose_name='Statistics', max_length=100)
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Diller.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Plotter(models.Model):
    diller_id = models.ForeignKey(Diller, verbose_name='Name_of_dillers', on_delete=models.CASCADE)
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
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
    plotter_id = models.ManyToManyField(Plotter, verbose_name='Плоттер')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name_mold
