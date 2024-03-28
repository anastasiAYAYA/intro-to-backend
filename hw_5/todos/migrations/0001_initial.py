# Generated by Django 5.0.1 on 2024-03-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='', max_length=1000)),
                ('due_date', models.DateField()),
                ('status', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
