#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import User

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data.get('nom')
            prenom = form.cleaned_data.get('prenom')
            nin = form.cleaned_data.get('nin')
            try:
                user = User.objects.get(nom=nom,prenom=prenom,NIN=nin)
            except User.DoesNotExist :
                return redirect('login')
            user.isauth = True
            request.session['user_id'] = user.id
            return redirect('vote')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def success(request):
    return render(request, 'success.html')

