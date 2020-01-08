from django.shortcuts import render,HttpResponse, HttpResponseRedirect, redirect, reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm,Weapons
from .models import Profile, Weapons, OrderedWeapons,Defence,OrderedDefence

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
	items_bought = OrderedWeapons.objects.filter(player=request.user)
	item_list=[]
	for i in items_bought:
		item_list.append(Weapons.objects.get(title=str(i)))
		print(i)
	print(item_list)
	items=Weapons.objects.all()
	print(items)
	user=User.objects.get(username=request.user.username)

	return render(request,'game/weapons.html',{'items':items, 'user':user,'items_bought':item_list})

def ordering_weapons(request,key):
	items=Weapons.objects.get(id=key)
	print(items)
	return render(request,'game/confirm.html',{'items':items})


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

def sell_weapons_list(request):
	items=OrderedWeapons.objects.filter(player=request.user)
	print(items)
	item_list=[]
	for i in items:
		item_list.append(Weapons.objects.get(title=str(i)))
		print(i)
	print(item_list)

	return render(request,'game/sell.html',{'items':item_list})


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



def play2(request):
	items_bought = OrderedWeapons.objects.filter(player=request.user)
	item_list=[]
	for i in items_bought:
		item_list.append(Weapons.objects.get(title=str(i)))
		print(i)
	print(item_list)
	items=Defence.objects.all()
	print(items)
	user=User.objects.get(username=request.user.username)

	return render(request,'game/defences.html',{'items':items, 'user':user,'items_bought':item_list})

def ordering_defences(request,key):
	items=Defence.objects.get(id=key)
	print(items)

	return render(request,'game/confirm2.html',{'items':items})

def ordered_defences(request,key):
	items=Defence.objects.get(id=key)
	user=User.objects.get(username=request.user.username)
	ordered=OrderedDefence()
	ordered.player=request.user
	ordered.defence=items
	print(ordered)
	ordered.save()
	user.profile.money-=items.cost
	user.profile.weapon_list=str(user.profile.weapon_list)+", "+str(items.title)
	user.save()
	return redirect('/index2/play')       ## redirect to weapons home page

	

def sell_defence_list(request):
	items=OrderedDefence.objects.filter(player=request.user)
	print(items)
	item_list=[]
	for i in items:
		item_list.append(Defence.objects.get(title=str(i)))
		print(i)
	print(item_list)
	return render(request,'game/sell2.html',{'items':item_list})
	

def sell_defence(request,key):
	items=Defence.objects.get(id=key)
	user=User.objects.get(username=request.user)
	sell=OrderedDefence.objects.get(player=request.user, weapons=items)
	user.profile.money+=items.cost
	#user.profile.weapon_list.remove(items.title)
	print(user.profile.weapon_list)
	sell.delete()
	#sell.save()
	user.save()

	return redirect('/index2/play/play2/sell')


def match(request):
	players = list(Profile.objects.all())
	#players = list(players)
	player1 = User.objects.get(username=request.user)
	player1 = Profile.objects.get(user = player1)
	player1_rank = players.index(player1)
	
	if (player1_rank %2 == 0):
		player2_rank = player1_rank + 1
	else:
		player2_rank = player1_rank - 1
	player2 = players[player2_rank]


	weapons1=OrderedWeapons.objects.filter(player=request.user)
	weapons2=OrderedWeapons.objects.filter(player=player2.user)
	defences1=OrderedDefence.objects.filter(player=request.user)
	defences2=OrderedDefence.objects.filter(player=player2.user)

	for i in defences2:
		if(i.defence.title == 'Neutralizer'):
			for j in weapons1:
				j.points /= 2
				j.save()
		elif (i.defence.title == 'Fire Resistant'):
			for j in weapons1:
				if(j.title == 'Flame Thrower'):
					j.points /= 2
					j.save()
		elif(i.defence.title == 'Water Resistant'):
			for j in weapons1:
				if(j.title == 'Water Jet'):
					j.points /= 2
					j.save()
	sum1 = 0
	for i in weapons1:
		sum1 += i.points
	player1.points = sum1
	player1.save()
	for i in defences1:
		if(i.defence.title == 'Neutralizer'):
			for j in weapons1:
				j.points /= 2
				j.save()
		elif (i.defence.title == 'Fire Resistant'):
			for j in weapons2:
				if(j.title == 'Flame Thrower'):
					j.points /= 2
					j.save()
		elif(i.defence.title == 'Water Resistant'):
			for j in weapons2:
				if(j.title == 'Water Jet'):
					j.points /= 2
					j.save()
	sum1 = 0
	for i in weapons2:
		sum1 += i.points
	player2.points = sum1
	player2.save()
	
	if(player1.points > player2.points):
		winner = player1
	elif(player2.points > player1.points):
		winner = player2
	return render(request,'game/game.html',{'winner':winner})
	 