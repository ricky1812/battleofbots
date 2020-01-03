from django.shortcuts import render,HttpResponse, HttpResponseRedirect, redirect, reverse

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .forms import UserForm,Weapons
from .models import Profile

def index(request):
	return render(request,'game/index.html',{})


def signup(request):
	if request.method=='POST':
		form=UserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
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

def index2(request):
	return render(request,'game/index2.html')

def play(request):
	if request.method == 'POST':
		form = Weapons(request.POST)
		if form.is_valid():
			request.user.weapons = form.cleaned_data['weapons']  ## error as how to add checkbox inputs into textfields
			return HttpResponse("weapons added") ##for testing

	else:
		form = Weapons()
	args={'form': form}
	return render(request,'game/play.html',args)

