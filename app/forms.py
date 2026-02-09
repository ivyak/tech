from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from app.models import Task

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "is_done",
            "level",
            "photo"
        ]

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]