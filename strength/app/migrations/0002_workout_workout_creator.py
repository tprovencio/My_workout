# Generated by Django 2.2.4 on 2020-12-15 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='workout_creator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='app.User'),
            preserve_default=False,
        ),
    ]
