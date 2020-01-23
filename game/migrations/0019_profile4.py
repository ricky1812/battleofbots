# Generated by Django 3.0.1 on 2020-01-09 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0018_profile1_profile2_profile3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('points', models.IntegerField(default=0)),
                ('money', models.IntegerField(default=500)),
                ('weapon_list', models.TextField(max_length=500, null=True)),
                ('defence_list', models.TextField(max_length=500, null=True)),
                ('is_playing', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-points',),
            },
        ),
    ]