from django.shortcuts import render,HttpResponse, HttpResponseRedirect, redirect, reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm,Weapons
from .models import *

def index(request):
	return render(request,'game/homepage.html',{})

def index1(request):
	return render(request,'game/index.html')


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
	return render(request,'game/homepage.html',context)

@login_required
def logout_view(request):
	logout(request)
	return render(request,'game/index.html',{})
@login_required
def index2(request):
	user = User.objects.get(username = request.user)
	player = Profile.objects.get(user = user)
	return render(request,'game/index2.html',{'player':player})



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
	p = Profile.objects.get(user = request.user)
	i = Weapons.objects.get(id = key)
	if (p.money < i.cost):
		return render(request,'game/notenoughmoney.html',{})

	else:
		items=Weapons.objects.get(id=key)
		print(items)
		return render(request,'game/confirm.html',{'items':items})



def ordered_weapons(request,key):
	items=Weapons.objects.get(id=key)
	user=User.objects.get(username=request.user.username)
	p = Profile.objects.get(user = user)
	ordered=OrderedWeapons()
	ordered.player=request.user
	ordered.weapons=items
	print(ordered)
	ordered.save()
	#user.profile.points+=items.points
	#user.profile.money-=items.cost
	#user.profile.weapon_list=str(user.profile.weapon_list)+", "+str(items.title)
	#print(user.profile.weapon_list)
	p.points += items.points
	p.money -= items.cost
	p.weapon_list = str(p.weapon_list) + " "+ str(items.title)
	p.save()
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
	p = Profile.objects.get(user = user)
	sell=OrderedWeapons.objects.get(player=request.user, weapons=items)
	p.points-=items.points
	p.money+=items.cost
	#user.profile.weapon_list.remove(items.title)
	print(user.profile.weapon_list)
	sell.delete()
	#sell.save()
	p.save()

	return redirect('/index2/play')



def play2(request):
	items_bought = OrderedDefence.objects.filter(player=request.user)
	item_list=[]
	for i in items_bought:
		item_list.append(Defence.objects.get(title=str(i)))
		print(i)
	print(item_list)
	items=Defence.objects.all()
	print(items)
	user=User.objects.get(username=request.user.username)

	return render(request,'game/defences.html',{'items':items, 'user':user,'items_bought':item_list})

def ordering_defences(request,key):
	p = Profile.objects.get(user = request.user)
	i = Defence.objects.get(id = key)
	if (p.money < i.cost):
		return render(request,'game/notenoughmoney.html',{})
	else:
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
	user.profile.defence_list =str(user.profile.defence_list)+", "+str(items.title)
	user.save()
	return redirect('/index2/play2')       ## redirect to weapons home page



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
	sell=OrderedDefence.objects.get(player=request.user, defence =items)
	user.profile.money+=items.cost
	#user.profile.weapon_list.remove(items.title)
	print(user.profile.weapon_list)
	sell.delete()
	#sell.save()
	user.save()

	return redirect('/index2/play2')


def match(request):
	players = list(Profile.objects.all())
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
		if(i.defence.title == 'Fire Ressistant'):
			for j in weapons1:
				if(j.weapons.title == 'Flame Thrower'):
					player1.points -= 25
		elif(i.defence.title == 'Water Resistant'):
			for j in weapons1:
				if(j.weapons.title == 'Water Jet'):
					player1.points -= 25
		elif(i.defence.title == 'Bulletproof'):
			for j in weapons1:
				if(j.weapons.title == 'Machine Gun'):
					player1.points -= 30
				#player1.save()

	for i in defences1:
		if(i.defence.title == 'Fire Ressistant'):
			for j in weapons2:
				if(j.weapons.title == 'Flame Thrower'):
					player2.points -= 25
		elif(i.defence.title == 'Water Resistant'):
			for j in weapons2:
				if(j.weapons.title == 'Water Jet'):
					player2.points -= 25
		elif(i.defence.title == 'Bulletproof'):
			for j in weapons2:
				if(j.weapons.title == 'Machine Gun'):
					player2.points -= 30
			#player2.save()

	if(player1.points > player2.points):
		winner = player1
		player2.is_playing = False
		loser = player2
		#player2.save()
	elif(player2.points > player1.points):
		winner = player2
		player1.is_playing = False
		loser = player1
		#player1.save()
	#winner.curr_round += 1
	counter = 0
	for i in range(len(Profile1.objects.all())):
		if (winner.user.username == Profile1.objects.all()[i].user.username):
			print(winner)
			print(Profile1.objects.all()[i])
			counter = 1
			break
	print(counter)
	if(counter == 0):
		p = Profile1(user=winner.user, image=winner.image, points=winner.points, money=winner.money,weapon_list=winner.weapon_list, defence_list=winner.defence_list, is_playing=winner.is_playing)
		p.save()
		loser.save()
		winner.save()
		
	return render(request,'game/game.html',{'winner':winner,'loser':loser})


def match1(request):
	players = list(Profile1.objects.all())
	player1 = User.objects.get(username=request.user)
	player1 = Profile1.objects.get(user=player1)
	player1_rank = players.index(player1)
	if (len(players)%2 == 1 and player1_rank == len(players)-1):
		p = Profile2(user=player1.user, image=player1.image, points=player1.points, money=player1.money,weapon_list=player1.weapon_list, defence_list=player1.defence_list, is_playing=player1.is_playing)
		p.save()
		return render(request, 'game/default.html', {'winner': player1})

	else:
		if (player1_rank % 2 == 0):
			player2_rank = player1_rank + 1
		else:
			player2_rank = player1_rank - 1
		player2 = players[player2_rank]
		weapons1 = OrderedWeapons.objects.filter(player=request.user)
		weapons2 = OrderedWeapons.objects.filter(player=player2.user)
		defences1 = OrderedDefence.objects.filter(player=request.user)
		defences2 = OrderedDefence.objects.filter(player=player2.user)

		for i in defences2:
			if (i.defence.title == 'Fire Ressistant'):
				for j in weapons1:
					if (j.weapons.title == 'Flame Thrower'):
						player1.points -= 25
			elif (i.defence.title == 'Water Resistant'):
				for j in weapons1:
					if (j.weapons.title == 'Water Jet'):
						player1.points -= 25
			elif (i.defence.title == 'Bulletproof'):
				for j in weapons1:
					if (j.weapons.title == 'Machine Gun'):
						player1.points -= 30
			player1.save()
		for i in defences1:
			if (i.defence.title == 'Fire Ressistant'):
				for j in weapons2:
					if (j.weapons.title == 'Flame Thrower'):
						player2.points -= 25
			elif (i.defence.title == 'Water Resistant'):
				for j in weapons2:
					if (j.weapons.title == 'Water Jet'):
						player2.points -= 25
			elif (i.defence.title == 'Bulletproof'):
				for j in weapons2:
					if (j.weapons.title == 'Machine Gun'):
						player2.points -= 30
			player2.save()

		if (player1.points > player2.points):
			winner = player1
			loser = player2
			player2.is_playing = False
			player2.save()
		elif (player2.points > player1.points):
			winner = player2
			loser = player1
			player1.is_playing = False
			player1.save()
		counter = 0
		for i in range(len(Profile2.objects.all())):
			if (winner.user.username == Profile2.objects.all()[i].user.username):
				print(winner)
				print(Profile2.objects.all()[i])
				counter = 1
				break
		print(counter)
		if(counter == 0):
			p = Profile2(user=winner.user, image=winner.image, points=winner.points, money=winner.money,weapon_list=winner.weapon_list, defence_list=winner.defence_list, is_playing=winner.is_playing)
			p.save()

		return render(request, 'game/game1.html', {'winner':winner,'loser':loser})


def match2(request):
	players = list(Profile2.objects.all())
	player1 = User.objects.get(username=request.user)
	player1 = Profile2.objects.get(user=player1)
	player1_rank = players.index(player1)
	if (len(players)%2 == 1 and player1_rank == len(players)-1):
		p = Profile3(user=player1.user, image=player1.image, points=player1.points, money=player1.money,weapon_list=player1.weapon_list, defence_list=player1.defence_list, is_playing=player1.is_playing)
		p.save()
		return render(request, 'game/default.html', {'player': player1})

	else:
		if (player1_rank % 2 == 0):
			player2_rank = player1_rank + 1
		else:
			player2_rank = player1_rank - 1
		player2 = players[player2_rank]
		weapons1 = OrderedWeapons.objects.filter(player=request.user)
		weapons2 = OrderedWeapons.objects.filter(player=player2.user)
		defences1 = OrderedDefence.objects.filter(player=request.user)
		defences2 = OrderedDefence.objects.filter(player=player2.user)

		for i in defences2:
			if (i.defence.title == 'Fire Ressistant'):
				for j in weapons1:
					if (j.weapons.title == 'Flame Thrower'):
						player1.points -= 25
			elif (i.defence.title == 'Water Resistant'):
				for j in weapons1:
					if (j.weapons.title == 'Water Jet'):
						player1.points -= 25
			elif (i.defence.title == 'Bulletproof'):
				for j in weapons1:
					if (j.weapons.title == 'Machine Gun'):
						player1.points -= 30
					player1.save()

		for i in defences1:
			if (i.defence.title == 'Fire Ressistant'):
				for j in weapons2:
					if (j.weapons.title == 'Flame Thrower'):
						player2.points -= 25
			elif (i.defence.title == 'Water Resistant'):
				for j in weapons2:
					if (j.weapons.title == 'Water Jet'):
						player2.points -= 25
			elif (i.defence.title == 'Bulletproof'):
				for j in weapons2:
					if (j.weapons.title == 'Machine Gun'):
						player2.points -= 30
				player2.save()

		if (player1.points > player2.points):
			winner = player1
			loser = player2
			player2.is_playing = False
			player2.save()
		elif (player2.points > player1.points):
			winner = player2
			loser = player1
			player1.is_playing = False
			player1.save()
		counter = 0
		for i in range(len(Profile3.objects.all())):
			if (winner.user.username == Profile2.objects.all()[i].user.username):
				print(winner)
				print(Profile3.objects.all()[i])
				counter = 1
				break
		print(counter)
		if(counter == 0):
			p = Profile3(user=winner.user, image=winner.image, points=winner.points, money=winner.money,weapon_list=winner.weapon_list, defence_list=winner.defence_list, is_playing=winner.is_playing)
			p.save()

		return render(request, 'game/game2.html', {'winner':winner,'loser':loser})


	


def match3(request):
	players = list(Profile3.objects.all())
	player1 = User.objects.get(username=request.user)
	player1 = Profile3.objects.get(user=player1)
	player1_rank = players.index(player1)
	if (len(players)%2 == 1 and player1_rank == len(players)-1):
		p = Profile4(user=player1.user, image=player1.image, points=player1.points, money=player1.money,weapon_list=player1.weapon_list, defence_list=player1.defence_list, is_playing=player1.is_playing)
		p.save()
		return render(request, 'game/default.html', {'player': player1})

	else:
		if (player1_rank % 2 == 0):
			player2_rank = player1_rank + 1
		else:
			player2_rank = player1_rank - 1
		player2 = players[player2_rank]
		weapons1 = OrderedWeapons.objects.filter(player=request.user)
		weapons2 = OrderedWeapons.objects.filter(player=player2.user)
		defences1 = OrderedDefence.objects.filter(player=request.user)
		defences2 = OrderedDefence.objects.filter(player=player2.user)

		for i in defences2:
			if (i.defence.title == 'Fire Ressistant'):
				for j in weapons1:
					if (j.weapons.title == 'Flame Thrower'):
						player1.points -= 25
			elif (i.defence.title == 'Water Resistant'):
				for j in weapons1:
					if (j.weapons.title == 'Water Jet'):
						player1.points -= 25
			elif (i.defence.title == 'Bulletproof'):
				for j in weapons1:
					if (j.weapons.title == 'Machine Gun'):
						player1.points -= 30
					player1.save()

		for i in defences1:
			if (i.defence.title == 'Fire Ressistant'):
				for j in weapons2:
					if (j.weapons.title == 'Flame Thrower'):
						player2.points -= 25
			elif (i.defence.title == 'Water Resistant'):
				for j in weapons2:
					if (j.weapons.title == 'Water Jet'):
						player2.points -= 25
			elif (i.defence.title == 'Bulletproof'):
				for j in weapons2:
					if (j.weapons.title == 'Machine Gun'):
						player2.points -= 30
				player2.save()

		if (player1.points > player2.points):
			winner = player1
			loser = player2
			player2.is_playing = False
			player2.save()
		elif (player2.points > player1.points):
			winner = player2
			loser = player1
			player1.is_playing = False
			player1.save()
		counter = 0
		for i in range(len(Profile4.objects.all())):
			if (winner.user.username == Profile2.objects.all()[i].user.username):
				print(winner)
				print(Profile4.objects.all()[i])
				counter = 1
				break
		print(counter)
		if(counter == 0):
			p = Profile4(user=winner.user, image=winner.image, points=winner.points, money=winner.money,weapon_list=winner.weapon_list, defence_list=winner.defence_list, is_playing=winner.is_playing)
			p.save()

		return render(request, 'game/game3.html', {'winner':winner,'loser':loser})