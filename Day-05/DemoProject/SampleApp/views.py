from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sample(request):
	return HttpResponse("Hello World!!!!")

def demo(re,t):
	return HttpResponse("Welcome user {}!!".format(t))

def st(request,y,e):
	return HttpResponse("Welcome User {} your age is: {}".format(y,e))

def gt(request,b):
	return HttpResponse("<h3>Welcome User <span style='color:red'>{}</span></h3>".format(b))

def hk(request,sd):
	return HttpResponse("<script>alert('Hi user {}')</script>".format(sd))

def cds(request):
	return render(request,'sample.html')

def empdtls(request,en,sal,ag):
	return render(request,'ht/e.html',{'empn':en,'emps':sal,'empa':ag})

def empregister(request):
	if request.method == "POST":
		empn = request.POST['en']
		empa = request.POST['ea']
		emps = request.POST['es']
		empe = request.POST['ee']
		return render(request,'ht/edetails.html',{'en':empn,'es':emps,'ea':empa,'ee':empe})
	return render(request,'ht/empr.html')

