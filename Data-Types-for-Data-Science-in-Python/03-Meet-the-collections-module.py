# -------------------------------------------------
# Data Types for Data Science in Python - Meet the collections module
# 24 set 2020
# VNTBJR
# ------------------------------------------------
# 
# Load packages
library(reticulate)

# Load data
import csv
csvfile = open("Datasets/cta_station.csv", mode ="r")
cta_stations = []
for row in csv.reader(csvfile):
  cta_stations.append(row)
quit()
csvfile.close()

stations = []
date = []
rides = []
for row in cta_stations:
  stations.append(row[1])
  date.append(row[2])
  rides.append(row[4])
quit()

entries = list(zip(date, stations, rides))

date.pop(0)
rides.pop(0)
stations.pop(0)

rides1 = []
for str in rides:
  rides1.append(int(str))

entries1 = list(zip(date, rides1))
entries2 = list(zip(date, stations, rides))

# Counting made easy ------------------------------------------------
# Using Counter on lists
# Import the Counter object
from collections import Counter

# Print the first ten items from the stations list
print(stations[:10])

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Print the station_count
print(station_count)

# Finding most common elements
# Import the Counter object
from collections import Counter

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Find the 5 most common elements
print(station_count.most_common(5))

#######################################################
# Dictionaries of unknown structure - defaultdict ------------------------------
# Creating dictionaries of unknown structure
# Create an empty dictionary: ridership
ridership = {}

# Iterate over the entries
for date, stop, riders in entries:
    # Check to see if date is already in the ridership dictionary
    if date not in ridership:
        # Create an empty list for any missing date
        ridership[date] = []
    # Append the stop and riders as a tuple to the date keys list
    ridership[date].append((stop, riders))
quit()
# Print the ridership for '03/09/2016'
print(ridership['03/09/2016'])

# Import defaultdict
from collections import defaultdict 

# Create a defaultdict with a default type of list: ridership
ridership = defaultdict(list)

# Iterate over the entries
for date, stop, riders in entries:
    # Use the stop as the key of ridership and append the riders to its value
    ridership[stop].append(riders)
quit()    
# Print the first 10 items of the ridership dictionary
print(list(ridership.items())[:10])

#######################################################
# Maintaining Dictionary Order with OrderedDict -------------------------------
# .popitem() method returns titems in reverse insertion order
# (last = False) to return the items in insertion order
# Working with OrderedDicitionaries
# Import OrderedDict from collections
from collections import OrderedDict

# Create an OrderedDict called: ridership_date
ridership_date = OrderedDict()

# Iterate over the entries
for date, riders in entries1:
    # If a key does not exist in ridership_date, set it to 0
    if date not in ridership_date:
        ridership_date[date] = 0
        
    # Add riders to the date key in ridership_date
    ridership_date[date] += riders
quit()    
# Print the first 31 records
print(list(ridership_date.items())[:31])

# Powerfull Ordered popping
# Print the first key in ridership_date
print(list(ridership_date.keys())[0])

# Pop the first item from ridership_date and print it
print(ridership_date.popitem(last = False))

# Print the last key in ridership_date
print(list(ridership_date.keys())[-1])

# Pop the last item from ridership_date and print it
print(ridership_date.popitem())

#######################################################
# What do you mean I don't have any class? Namedtuple --------------------------
# Creating namedtuples for storing data
# Import namedtuple from collections
from collections import namedtuple

# Create the namedtuple: DateDetails
DateDetails = namedtuple('DateDetails', ['date', 'stop', 'riders'])

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the entries list
for date, stop, riders in entries2:
    # Append a new DateDetails namedtuple instance for each entry to 
    #labeled_entries
    details = DateDetails(date,
                          stop, 
                          riders)
    labeled_entries.append(details)
quit()    
# Print the first 5 items in labeled_entries
print(labeled_entries[:5])

# Leveraging attributes on namedtuples
# Iterate over the first twenty items in labeled_entries
for item in labeled_entries[:20]:
    # Print each item's stop
    print(item.stop)
    # Print each item's date
    print(item.date)
    # Print each item's riders
    print(item.riders)
quit()
