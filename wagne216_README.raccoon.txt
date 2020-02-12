#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:09:37 2020

This is the metadata file for wagne_Evaluate_Raccoon_Life.py python script

@author:Danielle W =  wagne216
"""

SOURCE CODE FILE:
wagne216_Evaluate_Raccoon_Life.py

DATA SOURCE INPUT NEEDED: 
2008Male00006.txt
- This data is based on a raccoon simulation that tracked a raccoon named George
over time. 

OUTPUT TEXT:
Georges_life.txt

Running the source code will result in the following process:

1. Access the data source titled 2008Male00006.txt. A different data source may 
used but the data lengths will need to be changed in most loops in the script. 

2. Specify data types for each column based on viewing the data.

3. Store data in a dictionary called "Raccionary" with each column header saved as a key term.

4. Create functions to calculate the (a) cumuluative sum (b) mean (c) distance between 
2 points. 

5. Use the functions to calculate the racoon's distance traveled and add it to 
Raccionary; total distance; and coordinate averages. 

6. Output a textfile "Georges_life.txt" based on the time and location elements
of Raccionary and the final raccoon status. 