from django.db import models


class Article(models.Model):
    title = models.CharField(default='', max_length=100, null=False)
    text = models.CharField(default='', max_length=10000, null=False)
    author = models.CharField(default='', max_length=100, null=False)

    def __str__(self):
        return f'{self.id}. {self.title}'
