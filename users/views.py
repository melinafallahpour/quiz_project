
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from django.urls import reverse_lazy



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username="username", password=raw_password)
            # login(request, user)
            return redirect(reverse_lazy('login'))
    else:
        form = UserRegistrationForm()
        
        

    return render(request, 'register.html', {'form': form})
