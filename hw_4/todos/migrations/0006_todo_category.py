# Generated by Django 5.0.2 on 2024-02-28 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_todolist'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todos.todolist'),
        ),
    ]
