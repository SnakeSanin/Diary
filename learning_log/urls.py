"""Определяет схемуы работы с learning_log"""
from django.urls import path

from . import views

app_name = 'learning_log'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Cтраница со списком всех тем
    path('topics/', views.topics, name='topics'),
    # Cтраница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Страница добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Старница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),


]