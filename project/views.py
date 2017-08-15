from django.contrib import auth
from django.shortcuts import  redirect

def logout(request):
	auth.logout(request)
	return redirect('/')