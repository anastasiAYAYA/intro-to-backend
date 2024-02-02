from django.db import models


class Movie(models.Model):
    title = models.CharField(null=False, max_length=100, default='')
    description = models.CharField(null=False, max_length=5000, default='')
    producer = models.CharField(null=False, max_length=100, default='')
    duration = models.IntegerField(null=False, default=0)

    def __str__(self):
        return f'{self.id}. {self.title}'
