from django.shortcuts import render

# Create your views here.
def bth(request):
	return render(request,'html/bth.html')

def reg(request):
	return render(request,'html/regis.html')

def dsg(request):
	return render(request,'html/bg.html')