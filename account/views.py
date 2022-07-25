from django.contrib.auth import login, authenticate, logout
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages

from .forms import RegistrationForm, UserForm

def register_request(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegistrationForm()
	return render (request=request, template_name="account/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = UserForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_staff == True:
					login(request, user)
					messages.info(request, f"You are now logged in as {username}.")
					return redirect("staffpage")
				else:
					login(request, user)
					messages.info(request, f"You are now logged in as {username}.")
					return redirect("homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = UserForm()
	return render(request=request, template_name="account/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("homepage")