from django.db import models

class MapDetail(models.Model):
	map_text = models.TextField()
	last_update = models.DateTimeField("last update date")

class MapSearch(models.Model):
	version = models.IntegerField(default=0)
	search_text = models.CharField(max_length=50)
	map_id = models.ForeignKey(MapDetail)
	
	def __str__(self):
		return self.search_text+'/'+ str(self.version)

