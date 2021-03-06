# Generated by Django 4.0.3 on 2022-04-02 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200, unique=True, verbose_name='текст на английском')),
                ('translation', models.TextField(max_length=200, verbose_name='перевод')),
            ],
            options={
                'verbose_name': 'задание',
                'verbose_name_plural': 'задания',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_answers', models.PositiveSmallIntegerField(default=0, verbose_name='правильных ответов')),
                ('wrong_answers', models.PositiveSmallIntegerField(default=0, verbose_name='неправильных ответов')),
                ('date_start', models.DateField(verbose_name='изучается с ')),
                ('date_last', models.DateTimeField(verbose_name='изучается с ')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='training_room.tasks', verbose_name='Задание')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'история заданий пользователя',
                'verbose_name_plural': 'истории заданий пользователей',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='DateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='дата')),
                ('right_answers', models.PositiveSmallIntegerField(default=0, verbose_name='правильных ответов')),
                ('wrong_answers', models.PositiveSmallIntegerField(default=0, verbose_name='неправильных ответов')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'история занятий пользователя',
                'verbose_name_plural': 'истории занятий пользователей',
                'ordering': ['-id'],
            },
        ),
    ]
