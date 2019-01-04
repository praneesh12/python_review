#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pandas as pd
import csv

filename = sys.argv[1]

col_name_request = '-l'

if sys.argv[2] == col_name_request:
	col_names = sys.argv[3:]
else:
	col_names = sys.argv[2:]

df = pd.read_csv(filename, delimiter = ':')

col_names = [x.upper() for x in col_names]

for col in col_names:
	if col not in df.columns:
		sys.exit("{} does not exist".format(col))

if sys.argv[2] == col_name_request:
	print(df[col_names].to_string(index = False))
else:
	print(df[col_names].to_string(index=False, header =False))



#print(df[col_names].values)



#print(df.columns)

#print(df.head())
#for col in df[col_names].values:
#	print(col)

# with open (filename, 'r') as f:
# 	csvReader = csv.reader(f, delimiter = ':')
# 	second_col = list(zip(*csvReader))
	
# 	# for row in csvReader:
# 	# 	print(row[0])

# print(second_col[0])

	
# import csv

# with open('path/to/file.txt') as inf:
#     reader = csv.reader(inf, delimiter=" ")
#     second_col = list(zip(*reader))[1]

# 	for line in f:
# 		field1 = line.split(":")
# 		field2 = line.split(":")

# for i in field1:
# 	print(i)
# print(field1)




