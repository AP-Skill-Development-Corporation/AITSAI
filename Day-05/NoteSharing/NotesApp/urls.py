from django.urls import path
from NotesApp import views

urlpatterns = [
	path('',views.home,name="hm"),
	
]