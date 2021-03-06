#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:46:07 2018

@author: praneeshkhanna
"""

# =============================================================================
# #Importing the libraries
# =============================================================================
import pandas as pd
import re
import os
import sys

# =============================================================================
# Read data
# =============================================================================
file_name = sys.argv[1]
column_names = sys.argv[2:]

show_header = False
if sys.argv[1] == "-l" :
    show_header = True
    file_name = sys.argv[2]
    column_names = sys.argv[3:]   

text = pd.read_csv(file_name, ":")

# Changing input data to data frame object
df_text = pd.DataFrame(text)
df_text.columns

# =============================================================================
# Error Handling
# =============================================================================
col_names = [str(x.lower()) for x in col_names]

final_col_list = []

low_cols = [x.lower() for x in df_text.columns]
for col in col_names:
    if col.lower() in low_cols:
        final_col_list.append(df_text.columns[low_cols.index(col.lower())])
    else :
        sys.exit("One or more input columns were not present in the file")

if show_header == True:
    print(" ".join([str(x) for x in final_col_list]))

for row in df_text[final_col_list].values.tolist():
    print(" ".join([str(x) for x in row]))
