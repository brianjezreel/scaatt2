# Generated by Django 5.1.4 on 2025-03-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_sessions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='is_closed',
            field=models.BooleanField(default=False, help_text='Whether the session has been manually closed by the teacher'),
        ),
    ]
