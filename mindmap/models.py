from django.db import models

class MapDetail(models.Model):
	version = models.IntegerField(default=0)
	search_text = models.CharField(max_length=50)
	map_text = models.TextField()
	
	def __str__(self):
		return self.search_text+'/'+ str(self.version)

