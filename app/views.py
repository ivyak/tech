from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from app import forms
from app.models import Task
from django.contrib.auth import login


# Create your views here.

@login_required
def home(request):
    tasks = Task.objects.filter(created_by=request.user).order_by("-created_at")
    context = {
        "tasks": tasks,
    }
    return render(request, "app/home.html", context)

@login_required
def task_detail(request, pk):
    task = Task.objects.get(created_by=request.user, pk=pk)
    context = {
        "task": task,
    }
    return render(request, "app/task_detail.html", context)

@login_required
def task_create(request):
    if request.method == "POST":
        form = forms.TaskCreationForm(request.POST, request.FILES)
        if form.is_valid():
            non_user_form = form.save(commit=False)
            non_user_form.created_by = request.user
            non_user_form.save()
            return redirect("home")
    
    else:
        form = forms.TaskCreationForm()
            
    context = {
        "form": form,
    }
    return render(request, "app/task_create.html", context)

@login_required
def task_edit(request, pk):
    task = Task.objects.get(created_by=request.user, pk=pk)
    if request.method == "POST":
        form = forms.TaskCreationForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    
    else:
        form = forms.TaskCreationForm(instance=task)
            
    context = {
        "form": form,
        "task": task,
    }
    return render(request, "app/task_edit.html", context)

@login_required
def task_delete(request, pk):
    task = Task.objects.get(created_by=request.user, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("home")
            
    context = {
        "task": task,
    }
    return render(request, "app/task_delete.html", context)

class CustomLoginView(LoginView):
    template_name = "app/login.html"
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    pass

def signup(request):
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    
    else:
        form = forms.CustomUserCreationForm()
            
    context = {
        "form": form,
    }
    return render(request, "app/signup.html", context)