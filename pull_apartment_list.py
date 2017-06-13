import urllib, json
import requests
import time
import os

#Grabbing and parsing the JSON data
def GoogPlac(radius,types,key,Apartments):
  #making the url
  AUTH_KEY = key
  RADIUS = radius
  TYPES = types
  MyUrl = ('https://maps.googleapis.com/maps/api/place/textsearch/json'
           '?query=%s&key=%s') % (TYPES,AUTH_KEY)
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
count = 0
iteration = 0
MyType = ['apartments in north memphis','apartments in south memphis','apartments in east memphis','apartments in southeast memphis','apartments in northeast memphis']
naming = ['north','south','east','southeast','northeast']
for search in MyType:
    Apartments = open("/home/pi/OurMemphis/apartmentdata/Apartments_in_" + naming[iteration] + "memphis.json","w")
    all_json = GoogPlac(100,search,MyKey,Apartments)
    while(1):
        if('next_page_token' in all_json):
            Apartments = open("/home/pi/OurMemphis/apartmentdata/Apartments_in_" + naming[iteration] + "memphis" + str(count) + ".json","w")
            time.sleep(15)
            print "NEXT"
            all_json = next_page(MyKey,str(all_json['next_page_token']),Apartments)
            count += 1
        else:
            break
    iteration += 1
