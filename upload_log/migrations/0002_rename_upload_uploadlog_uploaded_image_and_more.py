# Generated by Django 4.2 on 2023-04-16 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('upload_log', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadlog',
            old_name='upload',
            new_name='uploaded_image',
        ),
        migrations.RemoveField(
            model_name='uploadlog',
            name='created_at',
        ),
        migrations.AddField(
            model_name='uploadlog',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]