"""model is a normal Class; it contains attributes and methods like all other classes"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):  # a class named Topic that inherits from Model a parent class included with Django
    # that defines the basic functionality of the model
    """The topic the user is studying"""
    text = models.CharField(max_length=200)  # CharField attributes can be used to store small amounts of text
    date_added = models.DateTimeField(auto_now_add=True)  # DateTimeField - block of data to store date and time
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): # implementation of __str__(), which returns the string stored in the text attribute
        """Returns the string representation of the model"""
        return self.text


class Entry(models.Model):  # the Entry class inherits from the base class Model
    """Information studied by the user on the topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # foreign key contains
    # a reference to another record in the database
    # The on_delete=models.CASCADE argument tells Django that when a theme is deleted
    # all posts related to this topic should also be deleted
    text = models.TextField()  # a field of this type does not require a size limit,
    # because the size of individual records are not limited
    date_added = models.DateTimeField(auto_now_add=True)   # date_added allows you to display records in
    # the order of their creation and provide each entry with a timestamp

    class Meta:  # The Meta class stores additional
        # new information on model management; in this case, it allows you to set
        # a special attribute that tells Django to use the multiform
        # a large number of Entries when accessing more than one entry
        verbose_name_plural = 'entries'
    def __str__(self):  # tells Django what information should be displayed when referring to individual records
        """Returns the string representation of the model"""
        if f'{self.text[50:]}':
            return f"{self.text[:50]}..."
        else:
            return f"{self.text[:50]}"
