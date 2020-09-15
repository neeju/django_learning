from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,Http404,HttpResponseRedirect

# Create your views here.
def login_user_index(request):
	if not request.user.is_authenticated:
		return render(request,"auth/login_index.html",{"message":None})
	context = {
		"user":request.user,
		}
	return render(request,"auth/user.html",context)

def login_user(request):
	username=request.POST["username"]
	password=request.POST["password"]
	user=authenticate(request,username=username,password=password)
	if user is not None:
		login(request,user)
		return render(request,"auth/user.html")
	else:
		return render(request,"auth/login_index.html",{"message":"Invaild Credentials"})


def logout_user(request):
	logout(request)
	return render(request,"auth/logout.html")


