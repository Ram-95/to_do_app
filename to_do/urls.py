from django.urls import path, include
from . import views
#from rest_framework import routers
# Using Classbased views - ListView
from .views import TaskListView

# These are the routers for the API
#router = routers.DefaultRouter()
#router.register(r'tasks_info', views.TaskViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    # Uncomment this if using Class Based View
    #path('tasks/', TaskListView.as_view(), name='tasks'),
    # Using Function based view
    path('tasks/', views.tasks, name='tasks'),
    path('test/', views.test, name='test'),
    path('move_tasks/', views.move_tasks, name='move_tasks'),
    path('add_new_task/', views.add_new_task, name='add_new_task'),
    path('delete_task/', views.delete_task, name='delete_task'),
    path('delete_all_completed_tasks/', views.delete_all_completed_tasks,
         name='delete_all_completed_tasks'),
    path('update_task/', views.update_task, name='update_task'),
    path('refresh_data/', views.refresh_data, name='refresh_data'),
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
