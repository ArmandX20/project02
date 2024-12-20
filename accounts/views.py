from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            # Save the new user and log them in.
            new_user = form.save()
            login(request, new_user)
            # Redirect to home page after successful registration.
            return redirect('learning:index')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

