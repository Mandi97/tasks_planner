from django.urls import path

from . import views

app_name = 'planners'

urlpatterns = [
    path('', views.PlannerListView.as_view(), name='planners-list'),
    path('<int:pk>/', views.PlannerDetailView.as_view(), name='planner-detail'),

]
