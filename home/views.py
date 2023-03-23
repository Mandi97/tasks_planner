from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Display homepage view"""
    template_name = 'home/home.html'

