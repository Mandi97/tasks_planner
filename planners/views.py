from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from . import models
from . import forms
from .models import Planner


class PlannerListView(ListView):
    """Created planners list view on our website"""
    model = models.Planner
    template_name = 'planners/planners_list.html'
    context_object_name = 'planners'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_planner_count = Planner.objects.filter(owner=self.request.user).count()
        context['user_planner_count'] = user_planner_count
        return context


class PlannerDetailView(DetailView):
    """Created detail view for planner on website"""
    model = models.Planner
    template_name = 'planners/planner_details.html'
    context_object_name = 'planner'

    def get_context_data(self, **kwargs):
        """Created sorted group of days with tasks"""
        context = super().get_context_data(**kwargs)
        tasks = {
            'monday': [],
            'tuesday': [],
            'wednesday': [],
            'thursday': [],
            'friday': [],
            'saturday': [],
            'sunday': [],
        }
        planner = context.get('planner')
        for task in planner.tasks.all():
            tasks[task.day_name].append(task)
        context['tasks'] = tasks
        context['user_task_count'] = planner.tasks.filter(owner=self.request.user).count()
        return context


class PlannerCreateView(LoginRequiredMixin, CreateView):
    """Create view for planner adding"""
    model = models.Planner
    fields = ('title', 'slug')
    template_name = 'planners/planner_create.html'
    success_url = reverse_lazy('planners:planners-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PlannerDeleteView(LoginRequiredMixin, DeleteView):
    """Created possibility to delete planner"""
    model = models.Planner
    success_url = reverse_lazy('planners:planners-list')
    template_name = 'planners/planner_delete.html'
    context_object_name = 'planner'


class PlannerUpdateView(LoginRequiredMixin, UpdateView):
    """Created possibility to edit planner"""
    model = models.Planner
    fields = ('title', 'slug')
    template_name = 'planners/planner_update.html'
    context_object_name = 'planner'

    def get_success_url(self):
        """Redirect to the same planner we edited"""
        pk = self.kwargs.get('pk')
        return str(reverse_lazy('planners:planner-detail', kwargs={'pk': pk}))


class TaskCreateView(LoginRequiredMixin, CreateView):
    """Created possibility to add new task"""
    model = models.Task
    form_class = forms.TaskForm
    template_name = 'planners/task_create.html'
    success_url = reverse_lazy('planners:planners-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """Created possibility to edit tasks"""
    model = models.Task
    form_class = forms.TaskForm
    template_name = 'planners/task_update.html'
    context_object_name = 'task'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs

    def get_success_url(self):
        """Redirect to the same planner where we edited task"""
        pk = self.kwargs.get('pk')
        return str(reverse_lazy('planners:planner-detail', kwargs={'pk': pk}))


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """Created possibility to delete task"""
    model = models.Task
    template_name = 'planners/task_delete.html'
    context_object_name = 'task'

    def get_success_url(self):
        """Redirect to the same planner where we deleted task"""
        task = self.get_object()
        planner_pk = task.planner.pk
        return str(reverse_lazy('planners:planner-detail', kwargs={'pk': planner_pk}))
