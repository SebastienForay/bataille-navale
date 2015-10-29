from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
	text = """<h1>Bienvenue sur le blog ! </h1>"""
	return HttpResponse(text)
	
def end(request):
	text = """<h1>Au revoir ! </h1>"""
	return HttpResponse(text)
	
def add(request, nbr1, nbr2):
	somme = int(nbr1) + int(nbr2)
	return render(request, 'blog/add.html',{'number1': nbr1,'number2': nbr2,'number': somme})
	
def date(request):
	return render(request, 'blog/date.html',{'date': datetime.now()})

def game(request):
	return render(request, 'blog/game.php')