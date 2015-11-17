from django.shortcuts import render
from .models import MapDetail

def template(request):
	return render(request,'template.html')
