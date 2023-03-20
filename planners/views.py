from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from . import models


class PlannerListView(ListView):
    """Created planners list view on our website"""
    model = models.Planner
    template_name = 'planners/planners_list.html'
    context_object_name = 'planners'


class PlannerDetailView(DetailView):
    model = models.Planner
    template_name = 'planners/planner_details.html'
    context_object_name = 'planner'


class PlannerCreateView(LoginRequiredMixin, CreateView):
    model = models.Planner
    fields = ('title', 'slug')
    template_name = 'planners/planner_create.html'
    success_url = reverse_lazy('planners:planners-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PlannerDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Planner
    success_url = reverse_lazy('planners:planners-list')
    template_name = 'planners/planner_delete.html'
    context_object_name = 'planner'


class PlannerUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Planner
    fields = ('title', 'slug')
    template_name = 'planners/planner_update.html'
    context_object_name = 'planner'

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return str(reverse_lazy('planners:planner-detail', kwargs={'pk': pk}))
