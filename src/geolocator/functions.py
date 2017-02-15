import urllib2
import json
from geopy import geocoders
from geopy.geocoders import Nominatim

def find_city_lat_lng(laT,lnG):
	g=geocoders.GoogleV3()
	lat_lng="%s, %s" %(laT,lnG)
	place, (lat, lng)=g.geocode(lat_lng,timeout=10)
	full=str(place)
	full_address=full.split(', ')
	city=full_address[2]
	return str(city)
	

def locu_search(query):
	locu_api='YOUR API KEY'
	api_key=locu_api
	url='https://api.locu.com/v1_0/venue/search/?'
	locality=query.replace(' ','%20')
	final_url=url+"has_menu=True&locality="+locality+"&api_key="+api_key
	json_obj=urllib2.urlopen(final_url)
	data=json.load(json_obj)
	locations=[]
	for item in data['objects']:
		item_list=[item['name'],item['id']]
		locations.append(item_list)

	return locations


def locu_details(locu_id):
	locu_api='YOUR API KEY'
	api_key=locu_api
	url='http://api.locu.com/v1_0/venue/'
	new_url = url + locu_id + "/?api_key=" + api_key
	obj=urllib2.urlopen(new_url)
	data=json.load(obj)

	details=[]
	for item in data['objects']:
		details.append(item['lat'])
		details.append(item['long'])
		details.append(item['phone'])
		details.append(item['street_address'])
		
	return details

def find_place(query):
	g=geocoders.GoogleV3()
	place, (lat, lng)=g.geocode(query,timeout=10)
	return place, lat, lng


def foursquare_search(query):
	token='YOUR API KEY'
	
	place,lat,lng=find_place(query)
	latlng=str(lat)+'%2C'+str(lng)
	url='https://api.foursquare.com/v2/venues/explore?oauth_token='+token+'&v=20131016&ll='+latlng+'&section=food&limit=1000&novelty=new'
	#url='https://api.foursquare.com/v2/venues/search?oauth_token='+token+'&v=20131016&ll='+latlng+'&query=food&intent=checkin'
	obj=urllib2.urlopen(url)
	data=json.load(obj)
	locations=[]

	for i in data['response']['groups']:
		for item in i['items']:
			locations.append([item['venue']['name'],item['venue']['id']])
	
	'''
	for i in data['response']['venue']:
		#print i['name'], i['location']['lat'], i['location']['lng']
		# i['contact']['formattedPhone'], i['location']['formattedAddress']
		locations.append([i['name'],i['id']])
	'''
	
	return locations


def foursquare_details(foursquare_id):
	token='YOUR API KEY'
	
	url='https://api.foursquare.com/v2/venues/'+ foursquare_id +'?v=20131016&oauth_token='+token
	obj=urllib2.urlopen(url)
	data=json.load(obj)
	details=[]
	details.append(data['response']['venue']['location']['lat'])
	details.append(data['response']['venue']['location']['lng'])
	if 'address' in data['response']['venue']['location']:
		details.append(data['response']['venue']['location']['address'])
	else:
		details.append('Not available')
	if 'formattedPhone' in data['response']['venue']['contact']:
		details.append(data['response']['venue']['contact']['formattedPhone'])
	else:
		details.append('Not available')
		
	return details

def foursquare_search_location(lat,lng):
	token='Your_api_key'
	latlng=str(lat)+'%2C'+str(lng)
	url='https://api.foursquare.com/v2/venues/explore?oauth_token='+token+'&v=20131016&ll='+latlng+'&section=food&limit=1000&novelty=new'
	#url='https://api.foursquare.com/v2/venues/search?oauth_token='+token+'&v=20131016&ll='+latlng+'&query=food&intent=checkin'
	obj=urllib2.urlopen(url)
	data=json.load(obj)
	locations=[]

	for i in data['response']['groups']:
		for item in i['items']:
			locations.append([item['venue']['name'],item['venue']['id']])
	
	
	return locations








