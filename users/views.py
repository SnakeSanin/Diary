from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Registering a new user"""
    if request.method != 'POST':  # In the register() function, we check if the function is responding to a POST request
        form = UserCreationForm()  # if not, a UserCreationForm instance is created containing no original data
    else:
        form = UserCreationForm(data=request.POST)  # In the case of a response to a POST request, a
        # UserCreationForm instance is created, based on sent data

        if form.is_valid():  # check that the data is correct
            new_user = form.save()  # save username and password hash in database
            login(request, new_user)  # perform an entrance; this process consists of two steps: first, the login()
            # function is called with the request and new_user objects
            return redirect('learning_log:index')  # the user is redirected to the home page


    context = {'form': form} # At the end of the function, a page is built that will either be an empty form or a
    # submitted form containing invalid data.
    return render(request, 'registration/register.html', context)