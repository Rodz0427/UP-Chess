from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddPlayerForm
from .models import Player


def home(request):
	players = Player.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again")
			return redirect('home')
	else:
		return render(request, 'home.html', {'players': players})



def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out!")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



def player_profile(request, pk):
	if request.user.is_authenticated:
		# Look up Players
		player_profile = Player.objects.get(id=pk)
		return render(request, 'player.html', {'player_profile':player_profile})
	else:
		messages.success(request, "You Must Be Logged In To View That Page")
		return redirect('home')



def remove_player(request, pk):
	if request.user.is_authenticated:
		remove_it = Player.objects.get(id=pk)
		remove_it.delete()
		messages.success(request, "Player Removed")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In")
		return redirect('home')


def add_player(request):
	form = AddPlayerForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid(): 
				add_player = form.save()
				messages.success(request, "Player Added")
				return redirect('home')
		return render(request, 'add_player.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In")
		return redirect('home')

def update_player(request, pk):
	if request.user.is_authenticated:
		current_player = Player.objects.get(id=pk)
		form = AddPlayerForm(request.POST or None, instance=current_player)
		if form.is_valid(): 
			form.save()
			messages.success(request, "Player Has Been Updated")
			return redirect('home')
		return render(request, 'update_player.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In")
		return redirect('home')



