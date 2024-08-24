from django.urls import path
from .views import *

urlpatterns = [
    path('c-cotacao/', create_cotacao, name='create_cotacao'),
    path('g-cotacao/', get_cotacao, name='get_cotacao')
]
