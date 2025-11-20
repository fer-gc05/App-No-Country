from .api import login, register, logout, refresh, me
from django.urls import path

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('refresh/', refresh, name='refresh'),
    path('me/', me, name='me'),
]