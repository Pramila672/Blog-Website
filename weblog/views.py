from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.urls import reverse
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponseForbidden



# Create your views here.
def blog(request):
    return HttpResponse('<div style="text-align: center;"><h1>Welcome to My Blog.</h1></div>')


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        u_form = UserRegisterForm(request.POST)
        if u_form.is_valid():
            password = u_form.cleaned_data['password']
            users = u_form.save()
            users.set_password(password)
            users.save()
            username = u_form.cleaned_data.get('username') 
            messages.success(request, f'Account Created for {username}!')
            return redirect(reverse('weblog:login'))
    else:
        u_form = UserRegisterForm()
    return render(request, "register.html", {'u_form': u_form})


def user_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            validate_user = authenticate(username=username, password=password)
            if validate_user is not None:
                login( request,validate_user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('weblog:home') 
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    posts = Blog.objects.all()
    return render(request, 'home.html', {'posts': posts})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    authors = User.objects.all()
    return render(request, 'blog_detail.html', {'blog': blog, 'authors': authors})


def blog_view(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weblog:home')
        else:
            return render(request,'blog_form.html',{'form':form})
    else:
        form = BlogForm()
        context = {
            'form':form
        }
        return render(request,'blog_form.html',context)
    

def user_list(request):
    users = User.objects.all()  
    blogs = Blog.objects.select_related('author').all() 
    return render(request, 'authorlist.html', {'users': users, 'blogs': blogs})


def blog_update_view(request,pk):
    blog = Blog.objects.get(pk=pk)
    if request.method =="POST":
        form = BlogForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('weblog:home')
        else:
            return render(request,'blog_form.html',{'form':form})
    else:
        form = BlogForm(instance=blog)
        context = {
            'form':form
        }
        return render(request, 'blog_form.html', context)


def blog_delete_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    
    # Check if the current user is the author of the blog
    if blog.author != request.user:
        return HttpResponseForbidden("You are not authorized to delete this blog post.")
    
    if request.method == "POST":
        blog.delete()
        messages.success(request, 'Blog post deleted successfully!')
        return redirect('weblog:home')
    
    return render(request, 'blog_confirm_delete.html', {'blog': blog})



def logout_view(request):
    logout (request)
    # Redirect to a desired page after logout
    return redirect('weblog:login')