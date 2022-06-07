from django.shortcuts import render,redirect
from .forms import Usreg
from django.contrib import messages
# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def register(request):
	if request.method == "POST":
		p = Usreg(request.POST)
		if p.is_valid():
			p.save()
			messages.success(request,'User Created Successfully')
			return redirect('/lgn')
	p = Usreg()
	return render(request,'html/register.html',{'h':p})