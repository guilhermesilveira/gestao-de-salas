from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/add/', views.add_room, name='add_room'),
]
