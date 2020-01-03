# Generated by Django 3.0.1 on 2020-01-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20200102_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='weapons',
        ),
        migrations.AddField(
            model_name='profile',
            name='flame_thrower',
            field=models.BooleanField(default=False, verbose_name='FLAME THROWER'),
        ),
        migrations.AddField(
            model_name='profile',
            name='flipper',
            field=models.BooleanField(default=False, verbose_name='FLIPPER'),
        ),
        migrations.AddField(
            model_name='profile',
            name='machine_gun',
            field=models.BooleanField(default=False, verbose_name='MACHINE GUN'),
        ),
        migrations.AddField(
            model_name='profile',
            name='sledge_hammer',
            field=models.BooleanField(default=False, verbose_name='SLEDGE HAMMER'),
        ),
        migrations.AddField(
            model_name='profile',
            name='spinning_blades',
            field=models.BooleanField(default=False, verbose_name='SPINNING BLADES'),
        ),
        migrations.AddField(
            model_name='profile',
            name='water_jet',
            field=models.BooleanField(default=False, verbose_name='WATER JET'),
        ),
    ]