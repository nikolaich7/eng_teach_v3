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
    context = training(request.POST, Tasks.objects.all())
    return render(request, 'training_sentences.html', context)


def training(form_data, tasks):
    user = User.objects.get(pk=form_data['user'])
    task_history = TaskHistory.objects.filter(user=user)
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
            date_history[0].right_answers += 1
        else:
            correct_last_answer = False
            history_last_task.wrong_answers += 1
            date_history[0].wrong_answers += 1
        history_last_task.save()
        date_history[0].save()
        profile.last_answer = last_answer
        profile.save()
    else:
        correct_last_answer = None
    next_task = task_history.exclude(
        date_last__gt = task_history[30].date_last
    ).first()
    profile.next_task = next_task.task.pk
    profile.save()
    context = {
        'next_task': next_task,
        'last_task': last_task,
        'date_history': date_history[0],
        'correct_last_answer': correct_last_answer,
    }
    return context


def read(request):
    user = User.objects.get(pk=1)
    value = ''
    i = 0
    dict_ex = {}
    with open("1.txt", "r") as file1:
        for line in file1:
            if not line.strip():
                print('Пустпя строка')
                break
            if i%2 == 0:
                value = line
            else:
                dict_ex[line.strip()] = value.strip()
            i += 1
            print(i)
    for en, ru in dict_ex.items():
        e = Tasks(text=en, translation=ru)
        e.save()
        f = TaskHistory(user=user, task=e)
        f.save()
        print(en)
    return HttpResponse('done')