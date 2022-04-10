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
    graph()
    return render(request, 'home.html')


def training_sentences_text(request):
    context = training(request.POST, 'Sentences', 'text')
    return render(request, 'training_sentences.html', context)


def training_words_text(request):
    context = training(request.POST, 'Words', 'text')
    return render(request, 'training_sentences.html', context)


def training_sentences_audio(request):
    context = training(request.POST, 'Sentences', 'audio')
    return render(request, 'training_sentences.html', context)


def training_words_audio(request):
    context = training(request.POST, 'Words', 'audio')
    return render(request, 'training_sentences.html', context)


def training(form_data, tasks_training, type_training):
    user = User.objects.get(pk=form_data['user'])
    task_history = TaskHistory.objects.filter(user=user, task__category__name=tasks_training)
    date_history = DateHistory.objects.get_or_create(user=user, date=date.today())
    profile = user.profile
    last_task_pk = profile.next_task
    last_task = Tasks.objects.get(pk=last_task_pk)
    if str(last_task_pk) in form_data:
        history_last_task = task_history.get(task=last_task)
        last_answer = form_data[str(last_task_pk)].strip()
        if last_answer.lower() == last_task.text.strip().lower():
            correct_last_answer = True
            if type_training == 'text':
                history_last_task.right_answers_text += 1
                if tasks_training == 'Sentences':
                    date_history[0].right_answers_sentences_text += 1
                elif tasks_training == 'Words':
                    date_history[0].right_answers_words_text += 1
            elif type_training == 'audio':
                history_last_task.right_answers_audio += 1
                if tasks_training == 'Sentences':
                    date_history[0].right_answers_sentences_audio += 1
                elif tasks_training == 'Words':
                    date_history[0].right_answers_words_audio += 1
        else:
            correct_last_answer = False
            if type_training == 'text':
                history_last_task.wrong_answers_text += 1
                if tasks_training == 'Sentences':
                    date_history[0].wrong_answers_sentences_text += 1
                elif tasks_training == 'Words':
                    date_history[0].wrong_answers_words_text += 1
            elif type_training == 'audio':
                history_last_task.wrong_answers_audio += 1
                if tasks_training == 'Sentences':
                    date_history[0].wrong_answers_sentences_audio += 1
                elif tasks_training == 'Words':
                    date_history[0].wrong_answers_words_audio += 1
        history_last_task.save()
        date_history[0].save()
        profile.last_answer = last_answer
        profile.save()
    else:
        correct_last_answer = None
    next_task = task_history.exclude(
        date_last__gt=task_history[100].date_last
    ).order_by(f'right_answers_{type_training}', f'wrong_answers_{type_training}').first()
    profile.next_task = next_task.task.pk
    profile.save()
    if type_training == 'text':
        if tasks_training == 'Sentences':
            right_answers = date_history[0].right_answers_sentences_text
            wrong_answers = date_history[0].wrong_answers_sentences_text
        elif tasks_training == 'Words':
            right_answers = date_history[0].right_answers_words_text
            wrong_answers = date_history[0].wrong_answers_words_text
    elif type_training == 'audio':
        if tasks_training == 'Sentences':
            right_answers = date_history[0].right_answers_sentences_audio
            wrong_answers = date_history[0].wrong_answers_sentences_audio
        elif tasks_training == 'Words':
            right_answers = date_history[0].right_answers_words_audio
            wrong_answers = date_history[0].wrong_answers_words_audio
    context = {
        'next_task': next_task,
        'last_task': last_task,
        'right_answers': right_answers,
        'wrong_answers': wrong_answers,
        'correct_last_answer': correct_last_answer,
        'type_training': type_training,
        'tasks_training': tasks_training,
    }
    return context


def graph():
    date_training = []
    right = []
    wrong = []
    right_w = []
    wrong_w = []
    right_a = []
    wrong_a = []
    right_w_a = []
    wrong_w_a = []
    user = User.objects.get(pk=1)
    print(user)
    tasks = DateHistory.objects.filter(user=user)
    print(tasks)
    for task in tasks:
        date_training.append(task.date)
        right.append(task.right_answers_sentences_text)
        wrong.append(task.wrong_answers_sentences_text)
        right_w.append(task.right_answers_words_text)
        wrong_w.append(task.wrong_answers_words_text)
        right_a.append(task.right_answers_sentences_audio)
        wrong_a.append(task.wrong_answers_sentences_audio)
        right_w_a.append(task.right_answers_words_audio)
        wrong_w_a.append(task.wrong_answers_words_audio)
    print(date_training, right)

    date_float_r = matplotlib.dates.date2num(date_training) - 0.2
    date_float_w = matplotlib.dates.date2num(date_training) + 0.2
    fig, axes = pylab.subplots(4, 1)


    axes[0].xaxis.set_major_formatter (matplotlib.ticker.NullFormatter())
    axes[1].xaxis.set_major_formatter (matplotlib.ticker.NullFormatter())
    axes[2].xaxis.set_major_formatter (matplotlib.ticker.NullFormatter())
    axes[3].xaxis.set_major_formatter (matplotlib.dates.DateFormatter("%d.%m"))
    axes[0].bar(date_float_r, right, width=0.4)
    axes[0].bar(date_float_w, wrong, width=0.4)
    axes[1].bar(date_float_r, right_w, width=0.4)
    axes[1].bar(date_float_w, wrong_w, width=0.4)
    axes[2].bar(date_float_r, right_a, width=0.4)
    axes[2].bar(date_float_w, wrong_a, width=0.4)
    axes[3].bar(date_float_r, right_w_a, width=0.4)
    axes[3].bar(date_float_w, wrong_w_a, width=0.4)

    axes[0].set_facecolor('seashell')
    axes[1].set_facecolor('seashell')

    plt.savefig('media/1.png')


def check(request):
    i = 0
    set_table = set()
    set_file = set()
    with open("1.txt", "r") as file1:
        for line in file1:
            if not line.strip():
                print('Пустая строка')
                break
            if i % 2 == 0:
                pass
            else:
                set_file.add(line.strip())
                print('f', line.strip())
            i += 1

    all_ex = Tasks.objects.all()
    for i in all_ex:
        set_table.add(i.text.strip())
        print('t', i.text)
    print(set_table.isdisjoint(set_file))
    return HttpResponse('done')


def read(request):
    user = User.objects.get(pk=1)
    value = ''
    i = 0
    dict_ex = {}
    with open("1.txt", "r") as file1:
        for line in file1:
            if not line.strip():
                print('Пустая строка')
                break
            if i%2 == 0:
                value = line
            else:
                dict_ex[line.strip()] = value.strip()
            i += 1
    first = Category.objects.get(name='Sentences')
    other = Category.objects.get(name='Past Simple')
    for en, ru in dict_ex.items():
        e = Tasks(text=en, translation=ru)
        e.save()
        e.category.add(first, other)
        f = TaskHistory(user=user, task=e)
        f.save()
        print(e.id)
    return HttpResponse('done')


def read_table(request):
    all_ex = Tasks.objects.filter(pk__gt=1516)
    for i in all_ex:
        f = open(f'media/audio/1672/{i.id}.txt', 'w')
        f.write(i.text)
        f.close()
    return HttpResponse('done')


def add_audio(request):
    for i in range(1517, 1673):
        try:
            ex = Tasks.objects.get(pk=i)
            ex.audio = 'audio/1672/' + str(i) + '.mp3'
            ex.save()
        except Tasks.DoesNotExist:
            pass
        print(str(i) + '.mp3')

    return HttpResponse('done')


def test(request):
    return render(request, 'test.html')
