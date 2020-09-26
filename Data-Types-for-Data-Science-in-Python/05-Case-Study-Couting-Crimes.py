# -------------------------------------------------
# Data Types for Data Science in Python - Case Study - Couting Crimes
# 25 set 2020
# VNTBJR
# ------------------------------------------------
# 
# Load packages
reticulate::repl_python()

#######################################################
# Reading your data with CSV Reader and Establishing your Data Containers -------
#######################################################
# Import the csv module
import csv

# Create the file object: csvfile
csvfile = open('Datasets/crime_sampler.csv', mode = 'r')

# Create an empty list: crime_data
crime_data = []

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):
    # Append the date, type of crime, location description, and arrest
    crime_data.append((row[0], row[2], row[4], row[5]))
quit()    
# Remove the first element from crime_data
crime_data.pop(0)

# Print the first 10 records
print(crime_data[:10])

# Find the Months with the Highest Number of Crimes
# Import necessary modules
from collections import Counter
from datetime import datetime

# Create a Counter Object: crimes_by_month
crimes_by_month = Counter()

# Loop over the crime_data list
for row in crime_data:
    # Convert the first element of each item into a Python Datetime Object: date
    date = datetime.strptime(row[0], '%m/%d/%Y %I:%M:%S %p')
    # Increment the counter for the month of the row by one
    crimes_by_month[date.month] += 1
quit()
# Print the 3 most common months for crime
print(crimes_by_month.most_common(3))

# Transforming your Data Containers to Month and Location
# Import necessary modules
from collections import defaultdict
from datetime import datetime

# Create a dictionary that defaults to a list: locations_by_month
locations_by_month = defaultdict(list)

# Loop over the crime_data list
for row in crime_data:
    # Convert the first element to a date object
    date = datetime.strptime(row[0], '%m/%d/%Y %I:%M:%S %p')
    # If the year is 2016 
    if date.year == 2016:
        # Set the dictionary key to the month and append the location 
        # (fifth element) to the values list
        locations_by_month[date.month].append(row[4])
quit()
# Print the dictionary
print(locations_by_month)

# Find the Most Common Crimes by Location Type by Month in 2016
# Import Counter from collections
from collections import Counter

# Loop over the items from locations_by_month using tuple expansion of the month
# and locations
for month, locations in locations_by_month.items():
    # Make a Counter of the locations
    location_count = Counter(locations)
    # Print the month 
    print(month)
    # Print the most common location
    print(location_count.most_common(5))
quit()

#######################################################
# Crimes by District and Differences by Block ------------------------------
#######################################################
