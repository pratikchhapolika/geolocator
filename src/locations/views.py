from django.shortcuts import render
from .models import Location
from geolocator.functions import locu_details,foursquare_details
# Create your views here.

def single_location(request, id):
	try:
		location=Location.objects.get(locu_id=id) #location contains the name of the location. The locu id is stored in variable 'location'. To access it write 'location.locu_id'
		locu=True
		foursquare=False
	except Location.DoesNotExist:
		location=Location.objects.get(foursquare_id=id)
		foursquare=True
		locu=False
	except:
		location='This location cannot be found'
		foursquare=False
		locu=False

	if locu:
		details=locu_details(location.locu_id)

	elif foursquare:
		details=foursquare_details(location.foursquare_id)
	
	else:
		pass

	return render(request,'locations/single.html',locals())
