from django.shortcuts import render
from functions import locu_search,foursquare_search,find_city_lat_lng,foursquare_search_location
from locations.models import Location

def home(request):
	if request.method=="POST":
		query=request.POST['search']
		#lat=request.POST['lat']
		#lng=request.POST['lng']
		'''
		#query=find_city_lat_lng(lat,lng)
		locations=locu_search(query)
		for item in locations:
			name,locu_id=item[0], item[1]
			new_location, created= Location.objects.get_or_create(name=name, locu_id=locu_id)
			if created:
				pass
				#print "Created new id for %s with id of %s" %(name, locu_id)
		
		'''
		
		locations=foursquare_search(query)
		for item in locations:
			name, foursquare_id=item[0],item[1]
			new_location, created= Location.objects.get_or_create(name=name, foursquare_id=foursquare_id)
			if created:
				pass
				#print "Created new id for %s with id of %s" %(name, foursquare_id)

	
	templates="home.html"
	context=locals()

	return render(request,templates,context)

def location(request):
	if request.method=="POST":
		lat=request.POST.get("lat",None)
		lng=request.POST.get("lng",None)
		locations=foursquare_search_location(lat,lng)
		for item in locations:
			name, foursquare_id=item[0],item[1]
			new_location, created= Location.objects.get_or_create(name=name, foursquare_id=foursquare_id)
			if created:
				pass

	templates="search_location.html"
	context=locals()

	return render(request,templates,context)

def main_home(request):
	templates="main_home.html"
	context=locals()

	return render(request,templates,context)
