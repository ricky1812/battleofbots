from django.shortcuts import render,HttpResponse, HttpResponseRedirect, redirect, reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm,Weapons
from .models import Profile, Weapons, OrderedWeapons

def index(request):
	return render(request,'game/index.html',{})


def signup(request):
	if request.method=='POST':
		form=UserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password=form.cleaned_data.get('password1')
			return redirect('login')
	else:
		form=UserForm()
	args={'form': form}
	return render(request,'game/signup.html',args)


def login_view(request):
	message='Log In'
	if request.method=='POST':
		_username=request.POST['username']
		_password=request.POST['password']
		user=authenticate(username=_username,password=_password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect('index2')
			else:
				message='Not Activated'
		else:
			message='Invalid Login'
	context={'message':message}
	return render(request,'game/login.html',context)

@login_required
def logout_view(request):
	logout(request)
	return render(request,'game/index.html',{})
@login_required
def index2(request):
	return render(request,'game/index2.html')



@login_required
def play(request):
	items=Weapons.objects.all()
	print(items)
	user=User.objects.get(username=request.user.username)

	return render(request,'game/weapons.html',{'items':items, 'user':user})

def ordering_weapons(request,key):
	items=Weapons.objects.get(id=key)
	print(items)

	return render(request,'game/confirm.html',{'items':items})

def sell_weapons_list(request):
	items=OrderedWeapons.objects.filter(player=request.user)
	print(items)
	item_list=[]
	for i in items:
		item_list.append(Weapons.objects.get(title=str(i)))
		print(i)
	print(item_list)

	return render(request,'game/sell.html',{'items':item_list})



def ordered_weapons(request,key):
	items=Weapons.objects.get(id=key)
	user=User.objects.get(username=request.user.username)
	ordered=OrderedWeapons()
	ordered.player=request.user
	ordered.weapons=items
	print(ordered)
	ordered.save()
	user.profile.points+=items.points
	user.profile.money-=items.cost
	user.profile.weapon_list=str(user.profile.weapon_list)+", "+str(items.title)
	#print(user.profile.weapon_list)
	user.save()
	#if request.method=="POST":

	
	return redirect('/index2/play')

def sell_weapons(request,key):
	items=Weapons.objects.get(id=key)
	user=User.objects.get(username=request.user)
	sell=OrderedWeapons.objects.get(player=request.user, weapons=items)
	user.profile.points-=items.points
	user.profile.money+=items.cost
	#user.profile.weapon_list.remove(items.title)
	print(user.profile.weapon_list)
	sell.delete()
	#sell.save()
	user.save()

	return redirect('/index2/play/sell')




