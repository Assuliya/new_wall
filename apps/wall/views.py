from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .forms import RegisterForm, LoginForm, PostForm
from .models import User, Post, Comment
import bcrypt

class Form(View):
    form_action = ''
    form_type = ''
    def get(self, request):
        if 'id' in request.session:
            return redirect(reverse('dashboard'))
        form = self.form_type()
        context = {'form' : form}
        template = 'wall/' +self.form_action+ '.html'
        return render(request, template, context)
    def post(self, request):
        form = self.form_type(request.POST)
        if form.is_valid():
            if self.form_action == 'register':
                form.save()
            user = User.objects.get(email=request.POST['email'])
            request.session['id'] = user.id
            return redirect(reverse('dashboard'))
        else:
            context = {'form' : form}
            template = 'wall/' +self.form_action+ '.html'
            return render(request, template, context)

def index(request):
    return render(request, 'wall/index.html')

def admin(request):
    if 'id' in request.session:
        print request.session['id']
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'wall/admin.html', context)

def dashboard(request):
    posts = Post.objects.all()
    form = PostForm(request.POST)
    context = {'posts': posts, 'form' : form}
    return render(request, 'wall/dashboard.html', context)

def show(request):
    return render(request, 'wall/show.html')

def edit(request):
    return render(request, 'wall/edit.html')

def logout(request):
    print 'hi'
    request.session.delete()
    return redirect(reverse('index'))

def delete(request, user_id):
    if request.method == "POST":
        user = User.objects.filter(id=user_id).delete()
    return redirect(reverse('dashboard'))

    # if request.method == "POST":
    #     User.objects.filter(id = request.session['user']).delete()
    #     request.session.delete()
    #     return redirect(reverse('index'))
    # return redirect(reverse('dashboard'))

def add_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        x = form.save(commit=False)
        x.user = User.objects.get(id=request.session['id'])
        x.save()
        return redirect(reverse('dashboard'))
    else:
        context = {'form' : form}
        return redirect(reverse('dashboard'), context)
