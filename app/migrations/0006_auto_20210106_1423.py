# Generated by Django 3.1.4 on 2021-01-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_descriptiongoals'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldimensions',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='personaldimensions',
            name='growth',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='personaldimensions',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
