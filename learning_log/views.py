from django.shortcuts import render, redirect  # render() function, which generates a response
# to based on data obtained from submissions
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry  # the model associated with the desired data is imported
from .forms import TopicForm, EntryForm


# Create your views here.

def index(request):
    """Application home page diary"""
    return render(request, 'index.html')

@login_required(login_url='/userslogin/')
def topics(request):  # functions topics() requires one parameter: the request object received by Django from the server
    """Lists topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')  # database context to get Topic objects
    # sorted by date_added attribute
    # context is a dictionary in which the keys are the names used in the template for accessing data,
    # and the values are the data that should be transferred patterned
    context = {'topics': topics}  # defines the context that will be passed to the template
    return render(request, 'topics.html', context)  # when building a page that uses the data, the context variable
    # is passed to the render() function, as well as the request object and the path to the template

@login_required
def topic(request, topic_id):  # The function gets the value that matches the expression
    # /<int:topic_id>/ and store it in topic_id
    """Displays one topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)  # the get() function is used to get the topic
    # Checking that the topic belongs to the current user.
    if topic.owner != request.user:  # error output if you are not the topic owner
        raise Http404
    entries = topic.entry_set.order_by('-date_added') # posts related to the topic are loaded and ordered by date_added:
    # a minus sign before date_added sorts the results in reverse order
    context = {'topic': topic, 'entries': entries}  # The subject and entries are stored in the context dictionary
    return render(request, 'topic.html', context)  # which is passed to topic.html template

@login_required
def new_topic(request):
    """Defines a new topic"""
    if request.method != 'POST':
        # No data submitted empty form
        form = TopicForm()
    else:
        # POST data has been sent; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            form.save()
            return redirect('learning_log:topics')
    # Display empty or invalid form
    context = {'form': form}
    return render(request, 'new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Adds a new post on a specific topic."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data was sent; an empty form is created.
        form = EntryForm()
    else:
        # POST data has been sent; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_log:topic', topic_id=topic_id)
    # Display empty or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edits an existing profile"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Original request; the form is filled with the data of the current record.
        form = EntryForm(instance=entry)
    else:
        # Sending POST data; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_log:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)
