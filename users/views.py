from django.shortcuts import render, redirect
# Readymade Form by Jango / Now cancel this 
#from django.contrib.auth.forms import UserCreationForm
# Flash Message
from django.contrib import messages
# Start using the new form so we capture email min 37
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # Flash Message
            messages.success(request, f'Account created for {username}!')
            return redirect('blogs-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})