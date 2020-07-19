from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('move_tasks/', views.move_tasks, name='move_tasks'),
    path('add_new_task/', views.add_new_task, name='add_new_task'),
    path('delete_task/', views.delete_task, name='delete_task'),
    path('delete_all_completed_tasks', views.delete_all_completed_tasks, name='delete_all_completed_tasks')
]