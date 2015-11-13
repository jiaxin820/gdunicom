from django.shortcuts import render
from .models import MapSearch,MapDetail

def template(request):
	return render(request,'template.html')
