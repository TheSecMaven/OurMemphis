from geopy.geocoders import Nominatim
import json
from pprint import pprint
import os
import sys 

all_addresses = []
all_lats = []
all_longs = []

all_types = []
all_names = []
all_dates = []

outfile = open("/home/pi/ourMemphis/crime_data_clean.json",'w')
count = 0
path = "/home/pi/ourMemphis/crimedata/"
input_files = [f for f in os.listdir(path)]
iterate = 0
os.chdir(path)

while(iterate < len(input_files)):
    with open(input_files[iterate]) as infile:
        all_lats = [line.split(',')[0] for line in infile.readlines()]
        iterate += 1
iterate = 0
while(iterate < len(input_files)):
    with open(input_files[iterate]) as infile:
        all_longs = [line.split(',')[1] for line in infile.readlines()]
        iterate += 1
iterate = 0

while(iterate < len(input_files)):
    with open(input_files[iterate]) as infile:
        all_types = [line.split(',')[2] for line in infile.readlines()]
        iterate += 1
iterate = 0

while(iterate < len(input_files)):
    with open(input_files[iterate]) as infile:
        all_addresses = [line.split(',')[5] for line in infile.readlines()]
        iterate += 1
iterate = 0

while(iterate < len(input_files)):
    with open(input_files[iterate]) as infile:
        all_names = [line.split(',')[6] for line in infile.readlines()]
        iterate += 1
iterate = 0

while(iterate < len(input_files)):
    with open(input_files[iterate]) as infile:
        all_dates = [line.split(',')[9] for line in infile.readlines()]
        iterate += 1
iterate = 0



for name in all_names:
    outfile.write(json.dumps({'name': name, 'address': all_addresses[count], 'lats': all_lats[count],'longs': all_longs[count],'date': all_dates[count],'type': all_types[count]},indent=4,sort_keys=True))
    outfile.write(',')
    count += 1
