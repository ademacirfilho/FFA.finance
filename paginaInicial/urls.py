from django.urls import path
from . import views

app_name = 'paginaInicial'

urlpatterns = [
    path('', views.index, name='index'),   
]