from datetime import datetime, date
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import pylab
import matplotlib.dates

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


def graph(request):
    date_training = []
    right = []
    wrong = []
    right_w = []
    wrong_w = []
    user = User.objects.get(pk=1)
    print(user)
    tasks = DateHistory.objects.filter(user=user)
    print(tasks)
    for task in tasks:
        date_training.append(task.date)
        right.append(task.right_answers_sentences)
        wrong.append(task.wrong_answers_sentences)
        right_w.append(task.right_answers_words)
        wrong_w.append(task.wrong_answers_words)
    print(date_training, right)

    date_float_r = matplotlib.dates.date2num(date_training) - 0.2
    date_float_w = matplotlib.dates.date2num(date_training) + 0.2
    fig, axes = pylab.subplots(2, 1)


    axes[0].xaxis.set_major_formatter (matplotlib.dates.DateFormatter("%d.%m"))
    axes[1].xaxis.set_major_formatter (matplotlib.dates.DateFormatter("%d.%m"))
    axes[0].bar(date_float_r, right, width=0.4)
    axes[0].bar(date_float_w, wrong, width=0.4)
    axes[1].bar(date_float_r, right_w, width=0.4)
    axes[1].bar(date_float_w, wrong_w, width=0.4)

    axes[0].set_facecolor('seashell')
    axes[1].set_facecolor('seashell')

    #plt.savefig('1.png')
    plt.show()
    return HttpResponse('done')


