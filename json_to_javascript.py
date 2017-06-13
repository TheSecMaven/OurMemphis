import json
import os



apartments = []
crimes = []

infile = open('apartment_summary_vectors_with_crimes.json', 'r')

infile_crime = open("crime_data_clean.json","r")
outfile_crime = open("crime_data_final.json",'w')
i = 0
outfile = open('final_vectors.json','w+')
infile = json.load(infile)
infile_crime = json.load(infile_crime)
for entry in infile:
    apartments.append(infile[entry])
    i += 1
outfile.write("var apartmentsJson = {'apartments':")
outfile.write(json.dumps(apartments))
outfile.write("}")

for entry in infile_crime:
    crimes.append(infile_crime[entry])
outfile_crime.write("var crimeDataJson = {'crimes':")
outfile_crime.write(json.dumps(crimes))
outfile_crime.write("}")
