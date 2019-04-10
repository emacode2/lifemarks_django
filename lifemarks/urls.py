from django.urls import path
from . import views

urlpatterns = [
    path('', views.mark_list, title='mark_list'),
]