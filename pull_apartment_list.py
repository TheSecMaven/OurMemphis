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
MyKey = 'AIzaSyDlIVa-Ub4V6nRg5uwLO4I8utDpm2VX1kU'
MyType = 'memphis+apartments'
Apartments = open("/home/pi/OurMemphis/apartmentdata/Apartments_in_memphis5.json","w")
all_json = GoogPlac(35.136749,-90.032631,100,MyType,MyKey,Apartments)
Apartments = open("/home/pi/OurMemphis/apartmentdata/Apartments_in_memphis6.json","w")
all_json1 = GoogPlac(35.177747,-89.969617,100,MyType,MyKey,Apartments)
Apartments = open("/home/pi/OurMemphis/apartmentdata/Apartments_in_memphis7.json","w")
all_json2 = GoogPlac(35.167925,-89.920178,100,MyType,MyKey,Apartments)
Apartments = open("/home/pi/OurMemphis/apartmentdata/Apartments_in_memphi83.json","w")
all_json3 = GoogPlac(35.140416,-89.901639,100,MyType,MyKey,Apartments)
Apartments = open("/home/pi/OurMemphis/apartmentdata/Apartments_in_memphis49.json","w")
all_json4 = GoogPlac(35.113460,-89.890309,100,MyType,MyKey,Apartments)
count = 2
while(all_json['next_page_token'] is not 'null'):
    Apartments = open("/home/pi/OurMemphis/apartmentdata/Apartments_in_memphis" + str(count) + ".json","w")
    time.sleep(15)
    all_json = next_page(MyKey,str(all_json['next_page_token']),Apartments)
    count += 1
while(all_json1['next_page_token'] is not 'null'):
    Apartments = open("/home/pi/OurMemphis/apartmentdata/Apartments_in_memphis" + str(count) + ".json","w")
    time.sleep(15)
    all_json1 = next_page(MyKey,str(all_json['next_page_token']),Apartments)
    count += 1
while(all_json2['next_page_token'] is not 'null'):
    Apartments = open("/home/pi/OurMemphis/apartmentdata/Apartments_in_memphis" + str(count) + ".json","w")
    time.sleep(15)
    all_json2 = next_page(MyKey,str(all_json['next_page_token']),Apartments)
    count += 1
while(all_json3['next_page_token'] is not 'null'):
    Apartments = open("/home/pi/OurMemphis/apartmentdata/Apartments_in_memphis" + str(count) + ".json","w")
    time.sleep(15)
    all_json3 = next_page(MyKey,str(all_json['next_page_token']),Apartments)
    count += 1
while(all_json4['next_page_token'] is not 'null'):
    Apartments = open("/home/pi/OurMemphis/apartmentdata/Apartments_in_memphis" + str(count) + ".json","w")
    time.sleep(15)
    all_json4 = next_page(MyKey,str(all_json['next_page_token']),Apartments)
    count += 1
