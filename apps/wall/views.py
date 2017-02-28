from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from .forms import RegisterForm, LoginForm, EditForm, PostForm, CommentForm
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
    comments = Comment.objects.all()
    post_form = PostForm(request.POST)
    comment_form = CommentForm(request.POST)
    context = {
        'posts': posts,
        'comments': comments,
        'post_form' : post_form,
        'comment_form': comment_form
    }
    return render(request, 'wall/dashboard.html', context)

def show(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return redirect(reverse('dashboard'))
    context = {'user':user}
    print(user)

    return render(request, 'wall/show.html', context)

def edit(request, user_id):
    if request.session['id'] == int(user_id):
        try:
            my_record = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            print "doesn't exist"
            return redirect(reverse('dashboard'))
        if request.method == "GET":
            form = EditForm(instance=my_record)
        if request.method == "POST":
            form = EditForm(request.POST, instance=my_record)
            if form.is_valid():
                print "hurray!"
                form.save()
                return redirect(reverse('show', kwargs={'user_id':user_id}))                
        context = {'form' : form, 'user':my_record}
        print(my_record)
        return render(request, 'wall/edit.html', context)


    return redirect(reverse('dashboard'))



def logout(request):
    print 'hi'
    request.session.delete()
    return redirect(reverse('index'))

def delete(request, user_id):
    if request.method == "POST":
        User.objects.filter(id=user_id).delete()
    return redirect(reverse('dashboard'))

    # if request.method == "POST":
    #     User.objects.filter(id = request.session['user']).delete()
    #     request.session.delete()
    #     return redirect(reverse('index'))
    # return redirect(reverse('dashboard'))

def add_post(request):
    post_form = PostForm(request.POST)
    if post_form.is_valid():
        x = post_form.save(commit=False)
        x.user = User.objects.get(id=request.session['id'])
        x.save()
        return redirect(reverse('dashboard'))
    else:
        context = {'post_form' : post_form}
        return redirect(reverse('dashboard'), context)

def delete_post(request, post_id):
    if request.method == "POST":
        Post.objects.filter(id=post_id).delete()
    return redirect(reverse('dashboard'))


def add_comment(request, post_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        x = comment_form.save(commit=False)
        x.user = User.objects.get(id=request.session['id'])
        x.post = Post.objects.get(id=post_id)
        x.save()
        return redirect(reverse('dashboard'))
    else:
        context = {'comment_form' : comment_form}
        return redirect(reverse('dashboard'), context)

def delete_comment(request, comment_id):
    if request.method == "POST":
        Comment.objects.filter(id=comment_id).delete()
    return redirect(reverse('dashboard'))
