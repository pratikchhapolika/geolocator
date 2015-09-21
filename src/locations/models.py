from django.db import models

# Create your models here.
class Location(models.Model):
	name=models.CharField(max_length=120)
	locu_id=models.CharField(max_length=250,null=True,blank=True)
	foursquare_id=models.CharField(max_length=250,null=True,blank=True)

	def __unicode__(self):
		return self.name