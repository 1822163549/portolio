from django.shortcuts import render
from app.models import MODELNAME
# Create your views here.


def home(requests):
	apps = MODELNAME.objects
	return render(requests, 'home.html', {'apps': apps})
	