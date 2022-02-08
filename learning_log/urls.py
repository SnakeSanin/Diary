"""Defines the schemes for working with learning_log"""
from django.urls import path

from . import views

app_name = 'learning_log'  # The app_name variable helps Django distinguish
# this urls.py file from the files of the same name in other applications in the project

"""
The URL scheme is a call to the path() function with three arguments:
The first argument contains a string that helps Django route the current request correctly.
The second argument to path() specifies the function to call from views.py
The third argument specifies the index name for this URL scheme so that it can be referenced in other parts of the code
"""


urlpatterns = [  # the urlpatterns variable in this module is
    # a list of pages that can be requested from the learning_logs application
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