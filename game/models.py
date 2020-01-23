from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from multiselectfield import MultiSelectField
from django.utils import timezone
from datetime import datetime

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	points=models.IntegerField(default=0)
	money=models.IntegerField(default=0)
	weapon_list=models.TextField(max_length=500, null=True)
	defence_list=models.TextField(max_length=500, null=True)
	is_playing = models.BooleanField(default=True)
	score=models.IntegerField(default=0)
	curr_round=models.IntegerField(default=1)
	submit_time =  models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		ordering = ('-points',)
	
	def __str__(self):
		return str(self.user)

@receiver(post_save,sender=User)

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Weapons(models.Model):
	title=models.CharField(max_length=100)
	description=models.CharField(max_length=500)
	points=models.IntegerField(default=0)
	cost=models.IntegerField(default=0)

	def __str__(self):
		return self.title


class OrderedWeapons(models.Model):
	player=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
	weapons = models.ForeignKey(Weapons, on_delete=models.CASCADE, null=True)
	
	def __str__(self):
		return str(self.weapons)

class Defence(models.Model):
	title=models.CharField(max_length=100)
	description=models.CharField(max_length=500)
	cost=models.IntegerField(default=0)

	def __str__(self):
		return self.title


class OrderedDefence(models.Model):
	player=models.ForeignKey(User,on_delete=models.CASCADE)
	defence = models.ForeignKey(Defence, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str(self.defence)


class Profile1(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	points=models.IntegerField(default=0)
	money=models.IntegerField(default=500)
	weapon_list=models.TextField(max_length=500, null=True)
	defence_list=models.TextField(max_length=500, null=True)
	is_playing = models.BooleanField(default=True)

	class Meta:
		ordering = ('-points',)
	
	def __str__(self):
		return str(self.user)


class Profile2(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	points=models.IntegerField(default=0)
	money=models.IntegerField(default=500)
	weapon_list=models.TextField(max_length=500, null=True)
	defence_list=models.TextField(max_length=500, null=True)
	is_playing = models.BooleanField(default=True)

	class Meta:
		ordering = ('-points',)
	
	def __str__(self):
		return str(self.user)

class Profile3(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	points=models.IntegerField(default=0)
	money=models.IntegerField(default=500)
	weapon_list=models.TextField(max_length=500, null=True)
	defence_list=models.TextField(max_length=500, null=True)
	is_playing = models.BooleanField(default=True)

	class Meta:
		ordering = ('-points',)
	
	def __str__(self):
		return str(self.user)

class Profile4(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	points=models.IntegerField(default=0)
	money=models.IntegerField(default=500)
	weapon_list=models.TextField(max_length=500, null=True)
	defence_list=models.TextField(max_length=500, null=True)
	is_playing = models.BooleanField(default=True)

	class Meta:
		ordering = ('-points',)
	
	def __str__(self):
		return str(self.user)