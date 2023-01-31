from django.contrib import admin
from django.urls import path, include
from knox import views as knox_views
from users.api.views import CustomLoginView


urlpatterns = [
    path('user/login/', CustomLoginView.as_view(), name='knox_login'),
    path('user/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('users/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]
