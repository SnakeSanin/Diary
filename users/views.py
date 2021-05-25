from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Registering a new user"""
    if request.method != 'POST':
        #Displays an empty registration form.
        form = UserCreationForm()
    else:
        # Processing a completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Logging in and redirecting to the home page.
            login(request, new_user)
            return redirect('learning_log:index')

    # Display empty or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)