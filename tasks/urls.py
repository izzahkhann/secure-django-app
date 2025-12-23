from django.urls import path
from .views import task_list, task_create, task_delete

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('delete/<int:id>/', task_delete, name='task_delete'),
]
