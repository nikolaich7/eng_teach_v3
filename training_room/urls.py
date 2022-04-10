from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('test', add_audio),
    path('training_words_text', training_words_text, name='training_words_text'),
    path('training_words_audio', training_words_audio, name='training_words_audio'),
    path('training_sentences_text', training_sentences_text, name='training_sentences_text'),
    path('training_sentences_audio', training_sentences_audio, name='training_sentences_audio'),
]