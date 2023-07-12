from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'create_user.html', {'form': form})

def home(request):
    return render(request, 'homepage.html')
