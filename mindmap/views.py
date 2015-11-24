from django.shortcuts import render
from django.utils import timezone
from .models import MapDetail
import tools.genDocx as genDocx
import tools.genRand8 as genRand8

def template(request,_search_text,_version):
	if _search_text is None:
		return render(request,'template.html')
	else:
		a_map=MapDetail.objects.get(search_text=_search_text,version=_version)
		return render(request,'template.html',{"map_xml":a_map.map_text})

def create(request,_search_text,_version):
	_map_text = request.POST['map_xml']
	if _search_text is None:
		_search_text = genRand8.get()	
	else:
		_version = int(_version)+1
	_update_date = timezone.now()
	new_map = MapDetail(map_text=_map_text,search_text=_search_text,version=_version) 
	new_map.save()

def genDoc(request):
	genDocx.get(request.POST["filename"])
