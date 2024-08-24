from django.urls import path
from .views import *

urlpatterns = [
    path('g-cotacao/', get_cotacao, name='get_cotacao'),
    path('c-conta_bancaria/',create_conta_bancaria, name='create_conta_bancaria' ),
    path('c-user/',create_user, name='create_user')
]
