from django.urls import path

from . import views

app_name = 'planners'

urlpatterns = [
    path('', views.PlannerListView.as_view(), name='planners-list'),
    path('<int:pk>/', views.PlannerDetailView.as_view(), name='planner-detail'),
    path('create/', views.PlannerCreateView.as_view(), name='planner-create'),
    path('delete/<int:pk>', views.PlannerDeleteView.as_view(), name='planner-delete'),
    path('update/<int:pk>', views.PlannerUpdateView.as_view(), name='planner-update'),
    path('create/task', views.TaskCreateView.as_view(), name='task-create'),
    path('task/update/<int:pk>', views.TaskUpdateView.as_view(), name='task-update'),
    path('task/delete/<int:pk>', views.TaskDeleteView.as_view(), name='task-delete'),

]
