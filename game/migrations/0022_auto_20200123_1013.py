# Generated by Django 2.0.2 on 2020-01-23 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0021_auto_20200119_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='money',
            field=models.IntegerField(default=0),
        ),
    ]
