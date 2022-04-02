from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('read', read, name='home'),
    path('training_sentences', training_sentences, name='training_sentences'),
]