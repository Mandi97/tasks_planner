from django import forms

from planners.models import Task


class TaskForm(forms.ModelForm):
    """Creating form for tasks"""
    class Meta:
        model = Task
        fields = ['title', 'description', 'day_name', 'planner']
