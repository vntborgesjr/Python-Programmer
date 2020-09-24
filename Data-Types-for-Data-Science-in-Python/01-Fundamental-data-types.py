# -------------------------------------------------
# Data Types for Data Science in Python - Fundamental data types
# 23 set 2020
# VNTBJR
# ------------------------------------------------
# 
# Load packages
library(reticulate)

# Lists ------------------------------------------------
# Manipulating lists for fun and profit
# .append() - add individual elements to a list
# . extend() - combine a list with another array type (list, set, tuple)
# . index() - find the position of an item in a list
# .pop() - remove the item using its position
# Create a list containing the names: baby_names
baby_names = ["Ximena", "Aliza", "Ayden", "Calvin"]

# Extend baby_names with 'Rowen' and 'Sandeep'
baby_names.extend(["Rowen", "Sandeep"])

# Print baby_names
print(baby_names)

# Find the position of 'Aliza': position
position = baby_names.index("Aliza")

# Remove 'Aliza' from baby_names
baby_names.pop(position)

# Print baby_names
print(baby_names)

# Load data
import csv
csvfile0 = open("Datasets/baby_names.csv", mode ='r')
records = []
for row in csv.reader(csvfile0):
  records.append(row)
quit()
print(records)
csvfile0.close()

# Looping over lists
# Create the empty list: baby_names
baby_names = []

# Loop over records 
for row in records:
    # Add the name to the list
    baby_names.append(row[3])
quit()    
# Sort the names in alphabetical order
for name in sorted(baby_names):
    # Print each name
    print(name)
quit()

#######################################################
girl_names = []
boy_names = []
for row in records:
  if row[1] == 'FEMALE':
    girl_names.append(row[3])
  elif row[1] == 'MALE':
    boy_names.append(row[3])
quit()
print(girl_names)
print(boy_names)

# Meet the Tuples ------------------------------------------------
# Using and unpacking tuples
# Pair up the girl and boy names: pairs
pairs = list(zip(girl_names, boy_names))

# Iterate over pairs
for idx, pair in enumerate(pairs) :
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print('Rank {}: {} and {}'.format(idx, girl_name, boy_name))
quit()

# Making tuples by accident
# Create the normal variable: normal
normal = 'simple'

# Create the mistaken variable: error
error = 'trailing comma',

# Print the types of the variables
print(type(normal))
print(type(error))

#######################################################
# Sets for unordered and unique data ------------------------------------------------
# We use sets when we want to store unique data elements in an unordered fashion
# .add() - adds new single elements to the set
# .update() - merges in another set or list with multiple itens
# .discard() - safely removes an element from the set by value
# .pop() - removes and returns an arbitrary element from the set
# .union() - returns a method of all the names (or)
# .intersction() - identifies overlapping data (and)
# .difference() - identifies data present in the set on which the method was used that is not
# in the arguments (-)
baby_names_2011 = set()
baby_names_2014 = set()
for row in records:
  if row[0] == "2011":
    baby_names_2011.add(row[3])
  elif row[0] == "2014":
    baby_names_2014.add(row[3])
quit()
print(baby_names_2011)
print(baby_names_2014)

# Finding all the data and the overlapping data between sets
# Find the union: all_names
all_names = baby_names_2011.union(baby_names_2014)

# Print the count of names in all_names
print(len(all_names))


# Find the intersection: overlapping_names
overlapping_names = baby_names_2011.intersection(baby_names_2014)

# Print the count of names in overlapping_names
print(len(overlapping_names))

# Determining set difference
# Create the empty set: baby_names_2011
baby_names_2011 = set()

# Loop over records and add the names from 2011 to the baby_names_2011 set
for row in records:
    # Check if the first column is '2011'
    if row[0] == '2011':
        # Add the fourth column to the set
        baby_names_2011.add(row[3])
quit()
# Find the difference between 2011 and 2014: differences
differences = baby_names_2011.difference(baby_names_2014)

# Print the differences
print(differences)

#######################################################
