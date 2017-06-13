from geopy.distance import vincenty
from geopy.geocoders import Nominatim
import json
from pprint import pprint

all_lats = []
all_longs = []
list_of_crimes = []
apartments = {}
apartments_out = {}
outfile = open('apartment_summary_vectors_with_crimes.json', 'w+')

with open('crime_data_clean.json') as crime_data1:
    crime_data = json.load(crime_data1)
    with open('apartments_clean.json') as apartment_data1:
        apartment_data = json.load(apartment_data1)
        for apartment in apartment_data:
            apartments[apartment] = apartment_data[apartment], {'crimes':[]}

        for crime in crime_data:
            crime_lat_long = tuple(((crime_data[crime]['lats']), (crime_data[crime]['longs'])))
            for i, apartment in enumerate(apartment_data):
                apartment_long_lat = (apartment_data[apartment]['info']['lats'],apartment_data[apartment]['info']['longs'])
                if (vincenty(crime_lat_long, apartment_long_lat).miles) <= .25:
                    apartments[apartment][1]['crimes'].append(crime_data[crime])

for key in apartments.iterkeys():
    apartments_out[key] = {'name': apartments[key][0]['info']['name'],'address': apartments[key][0]["info"]['address'], 'lats': apartments[key][0]['info']["lats"], 'longs': apartments[key][0]['info']["longs"], 'crimes': apartments[key][1]["crimes"]}
outfile.write(json.dumps(apartments_out,indent=4,sort_keys=True))
