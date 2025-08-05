from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account has been created successfully!')
            return redirect('login')
    else:
        form = RegisterForm()
        
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'users/profile.html')
    else:
        messages.warning(request, 'You need to be logged in to view your profile.')
        return redirect('login')