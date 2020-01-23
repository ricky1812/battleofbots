from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Profile)

admin.site.register(Profile1)
admin.site.register(Profile2)
admin.site.register(Profile3)
admin.site.register(Profile4)

admin.site.register(Weapons)
admin.site.register(OrderedWeapons)

admin.site.register(Defence)
admin.site.register(OrderedDefence)

