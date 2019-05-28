from django.urls import path
from . import views

app_name = 'kms'
urlpatterns = [
    path('', views.index, name='index'),
]
