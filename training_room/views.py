from datetime import datetime, date
from time import sleep

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader


from .models import *


def home(request):
    return render(request, 'home.html')


def training_sentences(request):
    context = training(request.POST, 'Sentences')
    return render(request, 'training_sentences.html', context)


def training_words(request):
    context = training(request.POST, 'Words')
    return render(request, 'training_sentences.html', context)


def training(form_data, type_training):
    user = User.objects.get(pk=form_data['user'])
    task_history = TaskHistory.objects.filter(user=user, task__category__name=type_training)
    date_history = DateHistory.objects.get_or_create(user=user, date=date.today())
    profile = user.profile
    last_task_pk = profile.next_task
    last_task = Tasks.objects.get(pk=last_task_pk)
    if str(last_task_pk) in form_data:
        history_last_task = task_history.get(task=last_task)
        last_answer = form_data[str(last_task_pk)].strip()
        if last_answer.lower() == last_task.text.strip().lower():
            correct_last_answer = True
            history_last_task.right_answers += 1
            if type_training == 'Sentences':
                date_history[0].right_answers_sentences += 1
            elif type_training == 'Words':
                date_history[0].right_answers_words += 1
        else:
            correct_last_answer = False
            history_last_task.wrong_answers += 1
            if type_training == 'Sentences':
                date_history[0].wrong_answers_sentences += 1
            elif type_training == 'Words':
                date_history[0].wrong_answers_words += 1
        history_last_task.save()
        date_history[0].save()
        profile.last_answer = last_answer
        profile.save()
    else:
        correct_last_answer = None
    next_task = task_history.exclude(
        date_last__gt = task_history[100].date_last
    ).order_by('right_answers').first()
    profile.next_task = next_task.task.pk
    profile.save()
    if type_training == 'Sentences':
        right_answers = date_history[0].right_answers_sentences
        wrong_answers = date_history[0].wrong_answers_sentences
    elif type_training == 'Words':
        right_answers = date_history[0].right_answers_words
        wrong_answers = date_history[0].wrong_answers_words
    context = {
        'next_task': next_task,
        'last_task': last_task,
        'right_answers': right_answers,
        'wrong_answers': wrong_answers,
        'correct_last_answer': correct_last_answer,
        'type_training': type_training,
    }
    return context
