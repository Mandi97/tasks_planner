from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView


from . import models
from . import forms


class PlannerListView(ListView):
    """Created planners list view on our website"""
    model = models.Planner
    template_name = 'planners/planners_list.html'
    context_object_name = 'planners'


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
