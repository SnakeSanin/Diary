from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):  # ModelForm consists of a nested Meta class
    # that tells Django which model the form should be based on and which fields it should have should be
    class Meta:
        model = Topic  # the form is created based on the Topic model
        fields = ['text']  # only the text field is placed
        labels = {'text': ''}  # the code tells Django not to generate the signature for text field

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}  # the 'text' field is again assigned an empty label
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # the widgets attribute is included.
        # a widget is an HTML form element: a single-line or multi-line text field, a drop-down list
