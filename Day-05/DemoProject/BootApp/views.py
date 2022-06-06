from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def bth(request):
	return render(request,'html/bth.html')

def reg(request):
	return render(request,'html/regis.html')

def dsg(request):
	return render(request,'html/bg.html')

def crd(request):
	d = Student.objects.all()
	if request.method == "POST":
		stn = request.POST['sn']
		sta = request.POST['sa']
		ste = request.POST['se']
		y = Student(sname=stn,sage=sta,semail=ste)
		y.save()
	return render(request,'html/crud.html',{'st':d})

def usupd(request,e):
	b = Student.objects.get(id=e)
	if request.method == "POST":
		b.sname = request.POST['sn']
		b.sage = request.POST['sa']
		b.semail = request.POST['se']
		b.save()
		return redirect('/cr')
	return render(request,'html/usp.html',{'a':b})

def usdt(request,w):
	c = Student.objects.get(id=w)
	if request.method == "POST":
		c.delete()
		return redirect('/cr')
	return render(request,'html/usd.html',{'q':c})
