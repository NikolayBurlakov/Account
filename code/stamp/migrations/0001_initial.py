# Generated by Django 3.1.7 on 2021-02-26 14:48

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name_of_dillers')),
                ('statistics_User', models.CharField(max_length=100, verbose_name='Statistics')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('name_of_user', models.CharField(max_length=255, verbose_name='User_name')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Plotter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statistics', models.TextField(max_length=1000, verbose_name='Статистика')),
                ('name_plotter', models.CharField(max_length=255, verbose_name='Название')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('diller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stamp.diller', verbose_name='Name_of_dillers')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stamp.user', verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Mold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_mold', models.CharField(max_length=255)),
                ('size', models.IntegerField(default=1, verbose_name='Размер')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('plotter_id', models.ManyToManyField(to='stamp.Plotter', verbose_name='Название')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='diller',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stamp.user', verbose_name='Пользователь'),
        ),
    ]
