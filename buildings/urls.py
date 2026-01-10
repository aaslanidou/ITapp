from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Building URLs
    path('building/add/', views.add_building, name='add_building'),
    path('building/edit/<int:pk>/', views.edit_building, name='edit_building'),
    path('building/delete/<int:pk>/', views.delete_building, name='delete_building'),

    # Room URLs
    path('room/add/', views.add_room, name='add_room'),
    path('room/edit/<int:pk>/', views.edit_room, name='edit_room'),
    path('room/delete/<int:pk>/', views.delete_room, name='delete_room'),
    path('rooms/add/', views.add_room, name='add_room'),
    
    # Computer URLs
    path('computer/add/', views.add_computer, name='add_computer'),
    path('computer/edit/<int:pk>/', views.edit_computer, name='edit_computer'),
    path('computer/delete/<int:pk>/', views.delete_computer, name='delete_computer'),
    path('computer/update-position/', views.update_computer_position, name='update_computer_position'),

]
