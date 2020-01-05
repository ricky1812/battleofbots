from django.contrib import admin

# Register your models here.
from .models import Profile, Weapons, OrderedWeapons

admin.site.register(Profile)
admin.site.register(Weapons)
admin.site.register(OrderedWeapons)
