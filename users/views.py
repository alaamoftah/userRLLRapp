from django.shortcuts import render, redirect
# Readymade Form by Jango / Now cancel this 
#from django.contrib.auth.forms import UserCreationForm
# Flash Message
from django.contrib import messages
# Start using the new form so we capture email min 37
from .forms import UserRegisterForm
# this is to ask user login before open profile - simple 
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # Flash Message
            messages.success(request, f'Account created success as:{username}, you will redirect now to login Page!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')