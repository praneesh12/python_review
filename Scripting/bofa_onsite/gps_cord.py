import csv
import sys
import pandas as pd


filename = sys.argv[1]
col_index = sys.argv[2:]

df = pd.read_csv(filename)

for col in col_index:
	print(df.iloc[col])



 
# # Set up input and output variables for the script
# gpsTrack = open("gps_track.txt", "r")
 
# # Set up CSV reader and process the header
# csvReader = csv.reader(gpsTrack)

# next(csvReader)

# for line in csvReader:
# 	print(line[1])
 
# # Make an empty list
# coordList = []
 
# # Loop through the lines in the file and get each coordinate
# for row in csvReader:
#     lat = row[latIndex]
#     lon = row[lonIndex]
#     coordList.append([lat,lon])
 
# # Print the coordinate list
# print(coordList)
