from django.urls import path
from . import views

urlpatterns = [
    path('', views.mark_list, name='mark_list'),
]