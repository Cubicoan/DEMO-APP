from django.forms import ModelForm
from demoapp.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_no', 'task_value', 'category']
