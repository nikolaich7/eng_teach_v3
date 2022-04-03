# Generated by Django 4.0.3 on 2022-04-03 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_room', '0006_category_alter_taskhistory_options_tasks_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datehistory',
            name='right_answers',
        ),
        migrations.RemoveField(
            model_name='datehistory',
            name='wrong_answers',
        ),
        migrations.AddField(
            model_name='datehistory',
            name='right_answers_sentences',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='ras'),
        ),
        migrations.AddField(
            model_name='datehistory',
            name='right_answers_words',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='raw'),
        ),
        migrations.AddField(
            model_name='datehistory',
            name='wrong_answers_sentences',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='was'),
        ),
        migrations.AddField(
            model_name='datehistory',
            name='wrong_answers_words',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='waw'),
        ),
    ]