from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from users.models import Account

DAY_CHOICES = (
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday'),
    ('sunday', 'Sunday'),

)


class Task(models.Model):
    """Creating tasks for database"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    day_name = models.CharField(max_length=20, choices=DAY_CHOICES, default=None)
    planner = models.ForeignKey('Planner', on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tasks_owner')

    def __str__(self):
        return self.title


class Planner(models.Model):
    """Creating planner for database with slug"""
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='planners_creator')
    members = models.ManyToManyField(get_user_model(), related_name='planners_member')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
