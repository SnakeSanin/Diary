from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/userslogin/')  # the login_required() code checks if the user is logged in and
# Django only runs the topics() code if that condition is done
def topics(request):  # functions topics() requires one parameter: the request object received by Django from the server
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')  # if the user is signed in, the attribute
    # is set on the request object request.user with information about the user.
    # code snippet Topic.objects. filter(owner=request.user) tells Django
    # to fetch only those Topic objects whose owner attribute matches the current user.
    context = {'topics': topics}  # defines the context that will be passed to the template
    return render(request, 'topics.html', context)  # when building a page that uses the data, the context variable
    # is passed to the render() function, as well as the request object and the path to the template

@login_required
def topic(request, topic_id):  # The function gets the value that matches the expression
    # /<int:topic_id>/ and store it in topic_id
    topic = Topic.objects.get(id=topic_id)  # the get() function is used to get the topic
    # Checking that the topic belongs to the current user.
    if topic.owner != request.user:  # if the topic does not belong to the current user, an Http404 exception is thrown
        raise Http404  # Django returns 404 error page
    entries = topic.entry_set.order_by('-date_added') # posts related to the topic are loaded and ordered by date_added:
    # a minus sign before date_added sorts the results in reverse order
    context = {'topic': topic, 'entries': entries}  # The subject and entries are stored in the context dictionary
    return render(request, 'topic.html', context)  # which is passed to topic.html template

@login_required
def new_topic(request):
    if request.method != 'POST':
        # No data submitted empty form
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)  # POST data has been sent; process data.
        if form.is_valid():
            new_topic = form.save(commit=False)  # the first time form.save() is called, the commit=False
            # argument is passed because the new theme must be modified before being stored in the database
            new_topic.owner = request.user  # the new theme's owner attribute is set to the current user
            form.save()  # we call save() on the newly defined theme instance
            return redirect('learning_log:topics')
    # Display empty or invalid form
    context = {'form': form}
    return render(request, 'new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)   # the theme ID will be needed to render the page and process the form data
    if request.method != 'POST':  # the request method - GET or POST - is checked at the point
        form = EntryForm()  # No data was sent; an empty form is created.
    else:
        form = EntryForm(data=request.POST)  # for the POST request method, we handle the data by creating
        # an EntryForm instance populated with the POST data from the request object
        if form.is_valid():  # the is_valid() function checks that all required fields have been filled in
            new_entry = form.save(commit=False)  # when we call save() we include set the commit=False argument
            # in order to create a new entry object and store it in new_entry without saving it to the database yet
            new_entry.topic = topic  # assign the topic attribute of the new_entry object to the topic read from the
            # database at the start of the function, then call save() with no arguments
            new_entry.save()  # the entry is stored in the database with a properly associated topic
            return redirect('learning_log:topic', topic_id=topic_id)  # the call to redirect() at the point takes
            # two arguments - the name of the view to which control is passed, and an argument for the view function
    context = {'topic': topic, 'form': form}  # context is defined at the end of the view function
    return render(request, 'new_entry.html', context)  # the page is based on the template new_topic.html

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)  # get the post object the user wants to change and the subject
    # associated with that post
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':  # in the if block that is executed for the GET request,
        # the EntryForm is instantiated
        form = EntryForm(instance=entry)  # the argument tells Django to create a form
        # pre-populated with information from an existing record object
    else:
        form = EntryForm(instance=entry, data=request.POST)  # passing instance=entry and data=request.POST
        # arguments tell Django to instantiate the form based on the information of an existing entry object,
        # updated with the data from request.POST. then the correctness of the form data is checked
        if form.is_valid():  # if the data is correct, save() should be called with no arguments.
            form.save()
            return redirect('learning_log:topic', topic_id=topic.id)  # redirects to the topic page and
            # the user sees an updated version of the post they edited.

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)  # if the original entry edit form is displayed, or
    # if the submitted form is not valid, a context dictionary is created and the page is
    # built based on the edit_entry.html template.
