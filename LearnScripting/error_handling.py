#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 10:33:41 2018

@author: praneeshkhanna
"""

import sys
import re
import os
import pandas as pd

filename = sys.argv[1]
col_names = sys.argv[2:]

show_header = False
if sys.argv[1] == '-l' :
    show_header = True
    filename = sys.argv[2]
    col_names = sys.argv[3:]

text = pd.read_csv(filename, ":")

text_df = pd.DataFrame(text)

final_col_list = []

col_names = [x.lower() for x in col_names]
low_cols = [x.lower() for x in text_df.columns]

for col in col_names:
    if col.lower() in  low_cols:
        final_col_list.append(text_df.columns[low_cols.index(col.lower())])
    else:
        sys.exit('One or more arguments entered are not a column name')

if show_header == True:
    print(" ".join([str(x) for x in final_col_list]))

for row in text_df[final_col_list].values.tolist():
    print(" ".join([str(x) for x in row]))
    
    
    
    