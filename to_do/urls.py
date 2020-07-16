from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('mark_as_done/', views.mark_as_done, name='mark_as_done')
]