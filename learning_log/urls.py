"""Определяет схемуы работы с learning_log"""
from django.urls import path

from . import views

app_name = 'learning_log'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page with a list of all topics
    path('topics/', views.topics, name='topics'),
    # A page with detailed information on a specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # The page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # The page for adding a new record
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing a record
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),


]