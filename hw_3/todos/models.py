from django.db import models
from django.forms import DateInput

class Todo(models.Model):
    title = models.CharField(null=False, max_length=100, default='')
    description = models.CharField(null=False, max_length=1000, default='')
    due_date = models.DateField(null=False)
    status = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f'{self.id}. {self.title}'
