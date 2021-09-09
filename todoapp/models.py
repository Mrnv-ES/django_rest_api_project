from django.db import models
from usersapp.models import User


class Project(models.Model):
    name = models.CharField(max_length=64, unique=True)
    repository = models.URLField(blank=True, null=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name}'


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    note_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
