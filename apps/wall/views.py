from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm, LoginForm
from .models import User
import bcrypt


def index(request):
    return render(request, 'wall/index.html')

def signin(request):
    return render(request, 'wall/signin.html')

def register(request):
    context = {}
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print ('yep')
            return redirect(reverse('dashboard'))
        else:
            print form.errors
    else:
        form = RegisterForm()
    context['form'] = form
    return render(request, 'wall/register.html', context)

def dashboard(request):
    users = User.objects.all()
    context = {
    'users': users
    }
    return render(request, 'wall/dashboard.html', context)

def show(request):
    return render(request, 'wall/show.html')

def edit(request):
    return render(request, 'wall/edit.html')
