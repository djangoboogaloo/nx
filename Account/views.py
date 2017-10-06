from django.contrib.auth import (
	authenticate,
	get_user_model,
	login as auth_login,
	logout as auth_logout,
	)
from django.shortcuts import render, redirect
from .form import userloginform,userresignform


def login(request):
	next = request.GET.get("next")
	form=userloginform(request.POST or None)

	context={
		"form":form,
		"title":"login "
		}
	if form.is_valid():
		username=form.cleaned_data.get("username")
		password=form.cleaned_data.get("password")
		user=authenticate(username=username,password=password)
		auth_login(request, user)
		if next:
			return redirect(next)
		else:
			return redirect("/")


	return render(request,"account/login.html",context)

def resign(request):
	title="join with me"
	next = request.GET.get("next")
	form=userresignform(request.POST or None)
	context={
	"title":title,
	"form":form,
	}
	if form.is_valid():
		user=form.save(commit=False)
		password=form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user=authenticate(username=user.username,password=password)
		auth_login(request,new_user)
		if next:
			return redirect(next)
		else:
			return redirect("/")

	return render(request,"account/signup.html",context)










def logout(request):
	auth_logout(request)
	return render(request,"account/logout.html",{})
