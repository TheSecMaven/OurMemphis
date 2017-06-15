from geopy.geocoders import Nominatim
import json
from pprint import pprint
import os
import sys 
import csv
all_addresses = []
all_lats = []
all_longs = []

all_types = []
all_names = []
all_dates = []

outfile = open("/home/pi/OurMemphis/crime_data_clean.json",'w')
count = 0
path = "/home/pi/OurMemphis/crimedata/"
input_files = [f for f in os.listdir(path)]
iterate = 0
os.chdir(path)
while(iterate < len(input_files)):
    with open(input_files[iterate]) as infile:
        infile.readline()
        spamreader = csv.reader(infile, delimiter=',', quotechar='|')
        for line in spamreader:
            all_lats.append(line[0])
        iterate += 1
iterate = 0
while(iterate < len(input_files)):
    with open(input_files[iterate]) as infile:
        infile.readline()
        spamreader = csv.reader(infile, delimiter=',', quotechar='|')
        for line in spamreader:
            all_longs.append(line[1])
        iterate += 1
iterate = 0
while(iterate < len(input_files)):
    with open(input_files[iterate]) as infile:
        infile.readline()
        spamreader = csv.reader(infile,delimiter=',',quotechar='|')
        for line in spamreader:
            all_types.append(line[2])
        iterate += 1
iterate = 0

while(iterate < len(input_files)):
    with open(input_files[iterate]) as infile:
        infile.readline()
        spamreader = csv.reader(infile,delimiter=',',quotechar='|')
        for line in spamreader:
            all_addresses.append((line[5]))
        iterate += 1
iterate = 0
while(iterate < len(input_files)):
    with open(input_files[iterate]) as infile:
        infile.readline()
        spamreader = csv.reader(infile,delimiter=',',quotechar='|')
        for line in spamreader:
            all_names.append(line[6])
        iterate += 1
iterate = 0

while(iterate < len(input_files)):
    with open(input_files[iterate]) as infile:
        infile.readline()
        spamreader = csv.reader(infile,delimiter=',',quotechar='|')
        for line in spamreader:
            all_dates.append(line[9])
        iterate += 1
iterate = 0

crime_summary = {}
for lat in all_lats:
    crime_summary[lat] = {'name':all_names[count],'address':all_addresses[count],'lats': lat ,'longs': all_longs[count],'type': all_types[count],'date':all_dates[count]}
    count += 1
print "Total Crime Count: " + str((len(crime_summary.keys())))
outfile.write(json.dumps(crime_summary,indent=4,sort_keys=True))
