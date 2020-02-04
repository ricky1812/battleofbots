from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime




	

	
        




class Question(models.Model):
	question=models.CharField(max_length=500)
	ans=models.CharField(max_length=500,default=None)
	image = models.ImageField(upload_to='images',default='default.jpg')
	round=models.IntegerField(default=1)

	def __str__(self):
		return self.question






	






