from django import forms

from planners.models import Task, Planner


class TaskForm(forms.ModelForm):
    """Creating form for create tasks"""
    def __init__(self, *args, owner=None, **kwargs):
        self.owner = owner
        super().__init__(*args, **kwargs)
        self.fields['planner'].queryset = Planner.objects.filter(owner=self.owner)

    class Meta:
        model = Task
        fields = ['title', 'description', 'day_name', 'planner']
