# Generated by Django 5.0.2 on 2024-02-22 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='todo_list',
            new_name='category',
        ),
    ]
