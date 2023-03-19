from django.shortcuts import render
from django.views.generic import ListView

from . import models


class PlannerListView(ListView):
    """Created planners list view on our website"""
    model = models.Planner
    template_name = 'planners/planners_list.html'
    context_object_name = 'planners'
