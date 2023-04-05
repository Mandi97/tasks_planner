from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Display homepage view"""
    template_name = 'home/home.html'


class ReadMore(TemplateView):
    """Display read more page"""
    template_name = 'home/read_more.html'
