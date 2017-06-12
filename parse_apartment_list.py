from geopy.geocoders import Nominatim
import json
from pprint import pprint
import os
import sys

all_addresses = []
all_lats = []
all_longs = []
iterate = 0
all_names = []
count = 0
counter = 0
path = '/home/pi/OurMemphis/apartmentdata/'
os.chdir(path)
files = [f for f in os.listdir(path)]
print files
outfile = open("/home/pi/OurMemphis/apartments_clean.json",'w')
while( iterate < len(files) ):
    with open('/home/pi/OurMemphis/apartmentdata/' + files[iterate]) as infile:
        infile = json.load(infile)
        for entry in infile['results']:
            all_lats.append(entry['geometry']['location']['lat'])
        for entry in infile['results']:
            all_longs.append(entry['geometry']['location']['lng'])
        for entry in infile['results']:
            all_addresses.append(entry['formatted_address'])
        for entry in infile['results']:
            all_names.append(entry['name'])
            counter += 1
    iterate += 1
    print "ITERATE"
apartment_summary = {}
print counter
print "ADDRESS COUNT: " + str(len(all_addresses))
for address in all_addresses:
    if(address in apartment_summary):
        print "KEY FOUND"
        print address
    else:
        apartment_summary[address] = {'info':{'name':all_names[count],'address':all_addresses[count],'lats': all_lats[count],'longs': all_longs[count]}}
        print address
        count += 1
print count
print "KEYS:" + str((len(apartment_summary.keys())))
outfile.write(json.dumps(apartment_summary,indent=4))
