# Generated by Django 2.0.2 on 2020-02-05 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20200205_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(default='/images/default.png', upload_to='images'),
        ),
    ]