from django.shortcuts import render
from .models import Student

# Create your views here.
def bth(request):
	return render(request,'html/bth.html')

def reg(request):
	return render(request,'html/regis.html')

def dsg(request):
	return render(request,'html/bg.html')

def crd(request):
	if request.method == "POST":
		stn = request.POST['sn']
		sta = request.POST['sa']
		ste = request.POST['se']
		y = Student(sname=stn,sage=sta,semail=ste)
		y.save()
	return render(request,'html/crud.html')


