# Generated by Django 3.1.4 on 2021-02-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210215_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleseries',
            name='reps',
            field=models.ManyToManyField(related_name='repeats', to='app.Reps'),
        ),
    ]
