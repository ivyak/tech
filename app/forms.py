from django import forms

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


