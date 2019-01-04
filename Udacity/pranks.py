#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 01:45:42 2019

@author: praneeshkhanna
"""

# =============================================================================
# Reassemble the file names to find out the message
# =============================================================================

import os

def rename_files():
    # get the file names
    folder_path = '/Users/praneeshkhanna/Desktop/DataScience/Python/Udacity/prank'
    file_list = os.listdir(folder_path)
    
    saved_path = os.getcwd()
    
    os.chdir(folder_path)
    
    # rename the file names
    for file in file_list:
        os.rename(file, (''.join([f for f in file if f.isalpha()])))
    
    os.chdir(saved_path)
        

rename_files()   
        
    
    
    
    

        