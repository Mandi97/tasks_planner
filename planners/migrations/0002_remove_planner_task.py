# Generated by Django 4.1.7 on 2023-03-22 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planners', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planner',
            name='task',
        ),
    ]