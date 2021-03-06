from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['-id']


class Tasks(models.Model):
    text = models.TextField(unique=True, max_length=200, verbose_name='текст на английском')
    translation = models.TextField(max_length=200, verbose_name='перевод')
    audio = models.FileField(upload_to='audio/%Y/%m/%d', null = True, blank=True)
    category = models.ManyToManyField(Category, verbose_name='категории')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'задание'
        verbose_name_plural = 'задания'
        ordering = ['-id']


class DateHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date = models.DateField(verbose_name='дата')
    right_answers_sentences_text = models.PositiveSmallIntegerField(default=0, verbose_name='rast')
    wrong_answers_sentences_text = models.PositiveSmallIntegerField(default=0, verbose_name='wast')
    right_answers_words_text = models.PositiveSmallIntegerField(default=0, verbose_name='rawt')
    wrong_answers_words_text = models.PositiveSmallIntegerField(default=0, verbose_name='wawt')
    right_answers_sentences_audio = models.PositiveSmallIntegerField(default=0, verbose_name='rasa')
    wrong_answers_sentences_audio = models.PositiveSmallIntegerField(default=0, verbose_name='wasa')
    right_answers_words_audio = models.PositiveSmallIntegerField(default=0, verbose_name='rawa')
    wrong_answers_words_audio = models.PositiveSmallIntegerField(default=0, verbose_name='wawa')


    def __str__(self):
        return 'история занятий ' + self.user.username

    class Meta:
        unique_together = ('user', 'date')
        verbose_name = 'история занятий пользователя'
        verbose_name_plural = 'истории занятий пользователей'
        ordering = ['-id']


class TaskHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, verbose_name='Задание')
    right_answers_text = models.PositiveSmallIntegerField(default=0, verbose_name='rat')
    wrong_answers_text = models.PositiveSmallIntegerField(default=0, verbose_name='wat')
    right_answers_audio = models.PositiveSmallIntegerField(default=0, verbose_name='raa')
    wrong_answers_audio = models.PositiveSmallIntegerField(default=0, verbose_name='waa')
    date_start = models.DateField(auto_now_add=True, verbose_name='изучается с ')
    date_last = models.DateTimeField(auto_now=True, verbose_name='последнее изучение')

    def __str__(self):
        return 'история заданий ' + self.user.username

    class Meta:
        unique_together = ('user', 'task')
        verbose_name = 'история заданий пользователя'
        verbose_name_plural = 'истории заданий пользователей'
        ordering = ['-date_last']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь')
    next_task = models.IntegerField(default=1, verbose_name='текущий вопрос')
    last_answer = models.TextField(default='', verbose_name='последний ответ')