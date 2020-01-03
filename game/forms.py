from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email','password')

Weapons = [
    ('flame_thrower','Flame Thrower'),
    ('water_jet','Water Jet'),
    ('sledge_hammer','Sledge Hammer'),
    ('spinning_blades','Spinning Blades'),
    ('machine_gun','Machine Gun'),
    ('Flipper','Flipper'),
    ('None','None')
]

class Weapons(forms.Form):
    weapons = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=Weapons,
    )
