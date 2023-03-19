from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

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
