from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Todo(models.Model):
    title = models.CharField(null=False, max_length=100, default='')
    description = models.TextField(null=False, max_length=1000, default='')
    due_date = models.DateField(null=False)
    status = models.BooleanField(default=False, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return f'{self.id}. {self.title}'
