from geopy.geocoders import Nominatim
import json
from pprint import pprint
import os
import sys

all_addresses = []
all_lats = []
all_longs = []

all_names = []
count = 0
outfile = open("apartments_clean.json",'w')
with open("Apartments_in_memphis.json") as infile:
    infile = json.load(infile)
    for entry in infile['results']:
        all_lats.append(entry['geometry']['location']['lat'])
    for entry in infile['results']:
        all_longs.append(entry['geometry']['location']['lng'])
    for entry in infile['results']:
        all_addresses.append(entry['formatted_address'])
    for entry in infile['results']:
        all_names.append(entry['name'])

for name in all_names:
    outfile.write(json.dumps({'name':name,'address':all_addresses[count],'lats': all_lats[count],'longs': all_longs[count]},indent=4,sort_keys=True))
    outfile.write(",")
    count += 1
