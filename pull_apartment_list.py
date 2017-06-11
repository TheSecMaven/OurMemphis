import urllib, json
import requests
#Grabbing and parsing the JSON data
def GoogPlac(lat,lng,radius,types,key,Apartments):
  #making the url
  AUTH_KEY = key
  LOCATION = str(lat) + "," + str(lng)
  RADIUS = radius
  TYPES = types
  MyUrl = ('https://maps.googleapis.com/maps/api/place/textsearch/json'
           '?query=%s&location=%s&radius=%s&key=%s') % (TYPES,LOCATION,RADIUS,AUTH_KEY)
  #grabbing the JSON result
  response = requests.get(MyUrl)
  jsonRaw = response.json()
  Apartments.write(json.dumps(jsonRaw,indent=4,sort_keys=True))

#This is a helper to grab the Json data that I want in a list
def IterJson(place):
  x = [place['name'], place['reference'], place['geometry']['location']['lat'], 
         place['geometry']['location']['lng'], place['vicinity']]




MyKey = 'GOOGLE PLACES API KEY'
MyType = 'memphis+apartments'
Apartments = open("Apartments_in_memphis.json","w")
GoogPlac(35.116293,-89.867409,300,MyType,MyKey,Apartments)

