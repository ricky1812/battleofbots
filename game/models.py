from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from multiselectfield import MultiSelectField


WEAPONS = (('flame_thrower','Flame Thrower'),
    ('water_jet','Water Jet'),
    ('sledge_hammer','Sledge Hammer'),
    ('spinning_blades','Spinning Blades'),
    ('machine_gun','Machine Gun'),
    ('Flipper','Flipper'),
	('None','None')
	)

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	points=models.IntegerField(default=0)
	money=models.IntegerField(default=500)
	weapons= MultiSelectField(choices=WEAPONS,default = 'None')
	
	def __str__(self):
		return str(self.user)

@receiver(post_save,sender=User)

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




