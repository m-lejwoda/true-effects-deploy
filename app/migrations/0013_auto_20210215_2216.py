# Generated by Django 3.1.4 on 2021-02-15 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210215_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleseries',
            name='exercise',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.exercise'),
        ),
        migrations.AlterField(
            model_name='singleseries',
            name='ownexercise',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ownexercise'),
        ),
    ]
