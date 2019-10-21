from django.shortcuts import render, get_object_or_404
from .models import Boke
# Create your views here.


def boke_page(request):
	bokes = Boke.objects
	return render(request, 'boke.html', {'bokes': bokes})


def boke_text(request,boke_id):
	boke = get_object_or_404(Boke,pk=boke_id)
	return render(request, 'boke_text.html', {'boke': boke})

