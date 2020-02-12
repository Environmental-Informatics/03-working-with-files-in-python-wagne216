#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:59:44 2020

ABE651 Assignment 3: Using Files & Simple Data Structures with Python
When run, this file will: 
    1. Access given data that includes modeled raccoon (named Georged) movement 
    2. Correctly store info. in a dictionary
    3. Perform computations using the data
    4. Save information as a text file ('Georges_life.txt')
    
--> for more details visit README.raccoon.txt metadata file
    
@author: Danielle Wanger  = wagne216
"""
# %% Access file
# 1. Open 2008Male00006.txt racoon behavior file in readable mode
frac = open("2008Male00006.txt", 'r') # raccoon file

# read file and save all data as 1 var
fullset = frac.readlines() # 
HowdItEnd = fullset[-1] # save last line for later

# close file 
frac.close()

# create list of 0's equal to file width; initializes variable to be faster
Data = [0]*len(fullset)

## split data for first row as strings, based on commas
for headx in range(16):
        header = fullset[0].split(',') # and divides into list
    
# specify data types for all but header and last line based on commas
for lidx in range(1,len(fullset)-1): # goes through each line
    Data[lidx] = fullset[lidx].strip().split(',') # and divides into list row by row
    Data[lidx][3] = int(Data[lidx][3]) # set row lidx, col 4 as integer field
    Data[lidx][4:5] = map(float,Data[lidx][4:5]) # floating point fields
    Data[lidx][5] = float(Data[lidx][5]) # floating point fields; had to reiterate making this a float
    Data[lidx][8:15] = map(float,Data[lidx][8:15]) # floating point fields
   
Data[0] = header
print(Data)
# %% Store Data in Dictionary
Raccionary = {} # initialize dictionary

# first define each key word

for idx_col in range(15): # goes through each key term
    temp_list = []
    for idx_row in range(1,15): # goes through one key term's values
        temp_list.append(Data[idx_row][idx_col]) # build value list

    Raccionary[Data[0][idx_col]] = temp_list # add list of values to dictionary

print(Raccionary)

# Last Line

# %% Analysis Functions
        
# CumSum: calculate cumulative sum of a list
def calc_cumsum(input_list):
    count = len(input_list) # no. items in list
    sum = 0 # initialize total sum
    for idx_list in range(count): # got rhrough and add each value
        sum = sum + input_list[idx_list] # sum is cumulative
    return sum
    
# Calculate mean from a list 
def calc_mean(input_list):
    count = len(input_list)
    mean = calc_cumsum(input_list)/count
    return mean

# Bring back function previously used to calc square root 
def mysqrt(k):
    threshold = 1e-16
    i = 3 # initial guess
    while True: # loop forever as long as estimate not close enough
#        print(x) # every round of x will be printed until final answer
        j = (i + k/i)/2 # new iterative estimate 
#       when close enough
        if abs(j-i) < threshold:
            return i
            break
        i = j
        
# Distance bewteen points based on pythagorean's theorem
# uses a^2 + b^2 = c^2
def calc_dist(x, y, a, b): # with points (x,y) and (a,b) 
    d = mysqrt(abs(x-a)**2 + abs(y-b)**2)
    return d

# In the raccoon dataset, each time corresponds to George's x and y coordinates
# Create a list of distances that George moves from one time to the next:

temp_move_list = [0]  # initiate list for distances moved before loop
for idx_move in range(1,len(Raccionary)-1):
# Assign coordinates to variables that will be input into calc_dist     
    x = Raccionary.get(' X')[idx_move-1]
    y = Raccionary.get(' Y')[idx_move-1]
    a = Raccionary.get(' X')[idx_move]
    b = Raccionary.get(' Y')[idx_move]
    d_moved = calc_dist(x,y,a,b)
    temp_move_list.append(d_moved) # build value list

# Add distances moved to dictionary- these will correspond to the dist moved between each row of coord's
Raccionary['Distance'] = temp_move_list # (coordinate units)

# %% George Info
# George's avg energy level: 
meanE = calc_mean(Raccionary.get('Energy Level')) # (raccoon energy units)
# George's avg location: 
meanX = calc_mean(Raccionary.get(' X')) # (raccoon x-coord units)
meanY = calc_mean(Raccionary.get(' Y')) # (raccoon y-coord units)
# Compute total movement distance
Tdist = calc_cumsum(Raccionary.get('Energy Level')) # (raccoon distance units)
# %% Output Georges_life.tx files

# Open file in writeable mode
fwrite = open('Georges_life.txt','w')

# Add header to file: 
with open('Georges_life.txt','w') as f: # with the file open, pritn statements: 
    print(' Raccoon name: George \n', 'Average location: ', meanX,' , ', 
             meanY,'\n Distance traveled: ',Tdist,'\n Average energy level: ',
             meanE,'\n Raccoon end state: ', HowdItEnd,'\n',  file = f)

# %%
# Can import dictionary with no format specs- bychanging to string- but is in a chunk:
#pk = Raccionary.keys()
#with open('Georges_life.txt','a') as f: # with the file open, print statements: 
#    print(pk, sep='\t', file = f)

#    f.write(str(Raccionary))
# %%
#iCan import pickle - works but is not human readable in the txt
# with open('Georges_life.txt','w') as f:
#    file.write(pickle.dumps(Raccionary))
#    print(Raccionary, file = f)
# print dictionary keys
#pk = Raccionary.keys()
import struct

with open('Georges_life.txt','a') as f: # with the file open 
    print('Year', 'Date', 'Time', ' X', ' Y', 'Asleep', 'Behavior Mode', 'Distance', sep = '\t', file = f)
    for element_key in range(len(Raccionary)-2):
# First add column headers
## Convert strings to byte data so it can be packed
#        Raccionary['Day'][element_key] = bytes(Raccionary['Day'][element_key], 'utf-8')
#        Raccionary['Time'][element_key] = bytes(Raccionary['Time'][element_key], 'utf-8')
#        Raccionary[' Asleep'][element_key] = bytes(Raccionary[' Asleep'][element_key], 'utf-8')
#        Raccionary['Behavior Mode'][element_key] = bytes(Raccionary['Behavior Mode'][element_key], 'utf-8')
## Pack into structure 
#        Bdata = struct.pack("@ssddssf", Raccionary['Day'][element_key], Raccionary['Time'][element_key],
#        Raccionary[' X'][element_key], Raccionary[' Y'][element_key],Raccionary[' Asleep'][element_key],
#        Raccionary['Behavior Mode'][element_key], Raccionary['Distance'][element_key]) # pack data into short int's using system endian setting.
# Straight print 
        print(Raccionary['Day'][element_key], Raccionary['Time'][element_key],
        Raccionary[' X'][element_key], Raccionary[' Y'][element_key],Raccionary[' Asleep'][element_key],
        Raccionary['Behavior Mode'][element_key], Raccionary['Distance'][element_key], '\n', sep = '\t', file = f) # pack data into short int's using system endian setting.
# Write to file
        
#    fwrite.write(Bdata) # write current line to the output file
#        print(Bdata)
#        val = Raccionary[element_key].split('\t')
#        (val, key) = element_key.splot('\t')
    
# %% Format into bytes



    # %%
# %
#for key_elemnt in range(len(Raccionary)):
# Compress data into native (@) format as p (character), p, d (double), d, p, p, f (float)   
#    Bdata = struct.pack("@ppddppf", Raccionary[4], Raccionary[14], Raccionary[1], Raccionary[2],  Raccionary[0],
#    Raccionary[3],  Raccionary[5]) # pack data into short int's using system endian setting.
#    Bdata = struct.pack("@ppddppf", Raccionary['Day'][key_elemnt], Raccionary['Time'][key_elemnt], Raccionary[' X'][key_elemnt],...
#                        Raccionary[' Y'][key_elemnt],  Raccionary[' Asleep'][key_elemnt],  Raccionary['Behavior Mode'][key_elemnt],...
#                        Raccionary['Distance'][key_elemnt]) # pack data into short int's using system endian setting.
#    Bdata = struct.pack("@f", Raccionary[' X'][key_elemnt])
#    fwrite.write(Bdata) # write current line to the output file
    

#>>> fwrite.close()
# %%
""" Remaining: 
2. Output text file with given header
1. README file
"""