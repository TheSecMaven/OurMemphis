import urllib, json
import requests
import time
import os

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
  return jsonRaw
def next_page(MyKey,next_page_token,Apartments):
  MyUrl = ('https://maps.googleapis.com/maps/api/place/textsearch/json'
           '?pagetoken=%s&key=%s') % (next_page_token,MyKey)
  #grabbing the JSON result
  response = requests.get(MyUrl)
  jsonRaw = response.json()
  Apartments.write(json.dumps(jsonRaw,indent=4,sort_keys=True))
  return jsonRaw
#This is a helper to grab the Json data that I want in a list
def IterJson(place):
  x = [place['name'], place['reference'], place['geometry']['location']['lat'], 
         place['geometry']['location']['lng'], place['vicinity']]


path = '/home/pi/OurMemphis/apartmentdata'
os.chdir(path)
MyKey = 'AIzaSyDiK82d8txAMxZyvdIGC0aB1Aw6xmEaD5A'
MyType = 'memphis+apartments'
Apartments = open("/home/pi/OurMemphis/apartmentdata/Apartments_in_memphis.json","w")
all_json = GoogPlac(35.116293,-89.867409,300,MyType,MyKey,Apartments)
count = 2
while(all_json['next_page_token'] is not 'null'):
    Apartments = open("/home/pi/OurMemphis/apartmentdata/Apartments_in_memphis" + str(count) + ".json","w")
    time.sleep(15)
    all_json = next_page(MyKey,str(all_json['next_page_token']),Apartments)
    count += 1
