from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('move_tasks/', views.move_tasks, name='move_tasks')
]