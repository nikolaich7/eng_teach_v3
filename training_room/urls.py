from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('read', graph, name='home'),
    path('training_words', training_words, name='training_words'),
    path('training_sentences', training_sentences, name='training_sentences'),
]