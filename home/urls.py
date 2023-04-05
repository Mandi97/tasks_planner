from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('read_more', views.ReadMore.as_view(), name='read-more')

]
