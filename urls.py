from django.urls import path
from .views import (
    GoalListView, GoalDetailView, GoalCreateView, GoalUpdateView, GoalDeleteView,
    StepCreateView, StepUpdateView, StepDeleteView,
    ProgressCreateView, RewardCreateView
)

urlpatterns = [
    path('', GoalListView.as_view(), name='goal_list'),
    path('goal/<int:pk>/', GoalDetailView.as_view(), name='goal_detail'),
    path('goal/new/', GoalCreateView.as_view(), name='goal_create'),
    path('goal/<int:pk>/edit/', GoalUpdateView.as_view(), name='goal_update'),
    path('goal/<int:pk>/delete/', GoalDeleteView.as_view(), name='goal_delete'),
    path('goal/<int:goal_id>/step/new/', StepCreateView.as_view(), name='step_create'),
    path('goal/<int:goal_id>/step/<int:pk>/edit/', StepUpdateView.as_view(), name='step_update'),
    path('goal/<int:goal_id>/step/<int:pk>/delete/', StepDeleteView.as_view(), name='step_delete'),
    path('goal/<int:goal_id>/progress/new/', ProgressCreateView.as_view(), name='progress_create'),
    path('goal/<int:goal_id>/reward/new/', RewardCreateView.as_view(), name='reward_create'),
]
