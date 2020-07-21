"""to_do_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# To Use the default Django's Login and Logout Views
from django.contrib.auth import views as auth_views
# Importing the Views of users app for routing purpose
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Home Page - By default, loading the To-Do List
    path('', include('to_do.urls')),
    path('admin/', admin.site.urls),
    # Routing to User Registration Page
    path('register/', user_views.register, name='register'),
    # The template_name = 'some path' tells django to look for the login page in 'users' -> 'templates' Directory
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
]

# Adding the Routes to serve static files - media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
