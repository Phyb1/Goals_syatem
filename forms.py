from django import forms
from .models import Goal, Step, Progress, Reward

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'is_specific', 'is_measurable', 'is_attainable', 'is_relevant', 'is_time_bound', 'start_date', 'end_date']

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ['description', 'is_completed', 'due_date']

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['step', 'date', 'progress_made', 'reflection']

class RewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = ['description', 'is_earned']
