from django.contrib import admin

# Register your models here.

from .models import Topic, Entry  # the dot before models tells Django to look for the models.py file
# in the same directory as admin.py

admin.site.register(Topic)  # the code imports the registerable Topic model
admin.site.register(Entry)  # tells Django that the model control should  carried out through the administrative site
