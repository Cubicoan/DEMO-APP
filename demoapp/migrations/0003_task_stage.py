# Generated by Django 3.1.2 on 2020-10-28 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_auto_20201028_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='stage',
            field=models.CharField(default='stage1', max_length=50),
        ),
    ]
