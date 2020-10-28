from django.db import models


class Task(models.Model):
    category_choice = (
        ('Category A', 'Category A'),
        ('Category B', 'Category B'),
        ('Category C', 'Category C'),
    )

    task_no = models.CharField(max_length=7, verbose_name='Task No')
    sub_task_no = models.CharField(max_length=50, verbose_name='Sub Task No', null=True)
    task_value = models.IntegerField(null=True, verbose_name='Task Value')
    category = models.CharField(max_length=50, choices=category_choice)
    stage = models.CharField(max_length=50, default='stage1')

    def __str__(self):
        return f"{self.sub_task_no}"

