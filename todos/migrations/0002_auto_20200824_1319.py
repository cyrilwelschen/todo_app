# Generated by Django 3.1 on 2020-08-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='imp_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='todo',
            name='job_rank',
            field=models.IntegerField(default=0),
        ),
    ]