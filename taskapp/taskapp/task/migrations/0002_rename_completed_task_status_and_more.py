# Generated by Django 4.1.3 on 2023-01-13 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='completed',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='task',
            name='scheduled_date',
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
