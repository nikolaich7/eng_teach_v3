# Generated by Django 4.0.3 on 2022-04-04 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training_room', '0009_remove_tasks_pronunciation_tasks_audio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datehistory',
            old_name='right_answers_sentences',
            new_name='right_answers_sentences_text',
        ),
        migrations.RenameField(
            model_name='datehistory',
            old_name='right_answers_words',
            new_name='right_answers_words_text',
        ),
        migrations.RenameField(
            model_name='datehistory',
            old_name='wrong_answers_sentences',
            new_name='wrong_answers_sentences_text',
        ),
        migrations.RenameField(
            model_name='datehistory',
            old_name='wrong_answers_words',
            new_name='wrong_answers_words_text',
        ),
    ]