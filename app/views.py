from django.shortcuts import render
from app.models import MODELNAME
# Create your views here.


def home(request):
	apps = MODELNAME.objects
	return render(request, 'home.html', {'apps': apps})
	