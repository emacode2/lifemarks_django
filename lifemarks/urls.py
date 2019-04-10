from django.urls import path
from . import views

urlpatterns = [
    path('', views.mark_list, name='mark_list'),
    path('marks/<int:pk>', views.mark_detail, name='mark_detail'),
]