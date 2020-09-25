# -------------------------------------------------
# Data Types for Data Science in Python - Handling Dates and Times
# 24 set 2020
# VNTBJR
# ------------------------------------------------
# 
# Load packages
library(reticulate)

# Load data
import csv
csvfile2 = open("Datasets/cta_summary.csv", mode = 'r')
daily_summaries = []
for row in csv.reader(csvfile2):
  daily_summaries.append(row)
quit()
csvfile2.close()
daily_summaries.pop(0)
print(daily_summaries)

dates_list = []
for date in daily_summaries:
  dates_list.append(date[0])
quit()

dates_list.pop(0)

# There and Back Again a Date Time Journey-------------------------------------
# Strings to DateTimes
# Import the datetime object from datetime
from datetime import datetime

# Iterate over the dates_list 
datetimes_list = []
for date_str in dates_list:
    # Convert each date to a datetime object: date_dt
    datetimes_list.append(datetime.strptime(date_str, '%m/%d/%Y'))
quit()    
    # Print each date_dt
    print(datetimes_list)

# Converting to a String
# Loop over the first 10 items of the datetimes_list
for item in datetimes_list[:10]:
    # Print out the record as a string in the format of 'MM/DD/YYYY'
    print(datetime.strftime(item, '%m/%d/%Y'))
        # Print out the record as an ISO standard string
    print(datetime.isoformat(item))
quit()

#######################################################
# Working with Datetime Components and Current time -----------------------------
# Pieces of Time
from datetime import datetime
from collections import defaultdict 

# Create a defaultdict of an integer: monthly_total_rides
monthly_total_rides = defaultdict(int)

# Loop over the list daily_summaries
for daily_summary in daily_summaries:
    # Convert the service_date to a datetime object
    service_datetime = datetime.strptime(daily_summary[0], '%m/%d/%Y')
    # Add the total rides to the current amount for the month
    monthly_total_rides[service_datetime.month] += int(daily_summary[4])
quit()    
# Print monthly_total_rides
print(monthly_total_rides)
