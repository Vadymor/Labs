from django.urls import path
from . import views

app_name = 'gks'
urlpatterns = [
    path('', views.index, name='index'),
    path('table', views.table, name='table'),
    path('result', views.result, name='result')
]
