from django.shortcuts import render
from .models import Boke
# Create your views here.


def boke(request):
	bokes = Boke.objects
	return render(request, 'boke.html', {'bokes': bokes})

