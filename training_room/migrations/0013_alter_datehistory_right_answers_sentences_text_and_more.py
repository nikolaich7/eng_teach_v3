# Generated by Django 4.0.3 on 2022-04-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_room', '0012_taskhistory_right_answers_audio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datehistory',
            name='right_answers_sentences_text',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='rast'),
        ),
        migrations.AlterField(
            model_name='datehistory',
            name='right_answers_words_text',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='rawt'),
        ),
        migrations.AlterField(
            model_name='datehistory',
            name='wrong_answers_sentences_text',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='wast'),
        ),
        migrations.AlterField(
            model_name='datehistory',
            name='wrong_answers_words_text',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='wawt'),
        ),
    ]
