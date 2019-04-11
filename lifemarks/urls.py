from django.urls import path
from . import views

urlpatterns = [
    path('', views.mark_list, name='mark_list'),
    path('marks/<int:pk>', views.mark_detail, name='mark_detail'),
    path('mark/new', views.mark_create, name='mark_create'),
    path('marks/<int:pk>/edit', views.mark_edit, name='mark_edit'),
    path('marks/<int:pk>/delete', views.mark_delete, name='mark_delete'),
]