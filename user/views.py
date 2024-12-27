from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomerUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            login(request, user)

            return redirect('/')
    else: 
        form = CustomerUserCreationForm()


    return render(request, 'user/signup.html', {
        'form': form
    })
