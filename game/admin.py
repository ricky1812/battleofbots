from django.contrib import admin

# Register your models here.
from .models import Profile, Weapons, OrderedWeapons,Defence,OrderedDefence

admin.site.register(Profile)
admin.site.register(Weapons)
admin.site.register(OrderedWeapons)

admin.site.register(Defence)
admin.site.register(OrderedDefence)

