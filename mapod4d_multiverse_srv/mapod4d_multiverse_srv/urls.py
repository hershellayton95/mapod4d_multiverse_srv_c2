"""mapod4d_multiverse_srv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from knox import views as knox_views
from users.api.views import CustomLoginView


urlpatterns = [
    path('admin/', admin.site.urls),

    ## REST API
    #path('api/auth/login/', CustomLoginView.as_view(), name='knox_login'),
    #path('api/auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    #path('api/auth/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('api/auth/', include('users.api.urls')),

    ## 
    path('multiverse/', include('multiverse.urls')),
    #path('projects/', include('projects.urls')),
]
