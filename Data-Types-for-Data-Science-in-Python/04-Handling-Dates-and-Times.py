# -------------------------------------------------
# Data Types for Data Science in Python - Handling Dates and Times
# 24 set 2020
# VNTBJR
# ------------------------------------------------
# 
# Load packages
reticulate::repl_python()

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
riderships = []
for date in daily_summaries:
  dates_list.append(date[0])
  riderships.append(date[4])
quit()

datetimes_list0 = []
for date in dates_list:
  datetimes_list0.append(datetime.strptime(date, '%m/%d/%Y'))
quit()

daily_summaries2 = list(zip(datetimes_list0, riderships))
print(daily_summaries2)

daily_summaries3 = defaultdict(list)
dict_inside1 = defaultdict(list)
dict_inside2 = defaultdict(list)

# Loop over the list daily_summaries
for daily_summary in daily_summaries:
  # Convert the service_date to a datetime object
  service_datetime = datetime.strptime(daily_summary[0], '%m/%d/%Y')
  # Add the total rides to the current amount for the month
  daily_summaries3[service_datetime] = dict_inside1['day_type'] = daily_summary[1]
  daily_summaries3[service_datetime] = dict_inside2['total_ridership'] = daily_summary[4]
quit()    
# Print monthly_total_rides
print(daily_summaries3)

review_dates = []
for date in daily_summaries:
  review_dates.append(datetime.strptime(date[0], '%m/%d/%Y'))
quit()
review_dates = review_dates[4469:4479]
print(review_dates)
len(review_dates)

#######################################################  
# There and Back Again a Date Time Journey-------------------------------------
#######################################################
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
#######################################################
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

# Creating DateTime Objects... Now
# Import datetime from the datetime module
from datetime import datetime

# Compute the local datetime: local_dt
local_dt = datetime.now()

# Print the local datetime
print(local_dt)

# Compute the UTC datetime: utc_dt
utc_dt = datetime.utcnow()

# Print the UTC datetime
print(utc_dt)

# Timezones
from pytz import timezone 

# Create a Timezone object for Chicago
chicago_usa_tz = timezone('US/Central')

# Create a Timezone object for New York
ny_usa_tz = timezone('US/Eastern')

# Iterate over the daily_summaries list
for orig_dt, ridership in daily_summaries2:
    # Make the orig_dt timezone "aware" for Chicago
    chicago_dt = orig_dt.replace(tzinfo = chicago_usa_tz)
    # Convert chicago_dt to the New York Timezone
    ny_dt = chicago_dt.astimezone(ny_usa_tz)
        # Print the chicago_dt, ny_dt, and ridership
    print('Chicago: %s, NY: %s, Ridership: %s' % (chicago_dt, ny_dt, ridership))
quit()

#######################################################
# Time Travel (Adding and Subtracting Time) ----------------------------------
#######################################################
# Finding a time in the future and from the past
# object daily_summaries for this exercise is missing...
# Import timedelta from the datetime module
from datetime import timedelta

# Build a timedelta of 30 days: glanceback
glanceback = timedelta(days = 30)

# Iterate over the review_dates as date
for date in review_dates:
    # Calculate the date 30 days back: prior_period_dt
    prior_period_dt = date - glanceback
       # Print the review_date, day_type and total_ridership
    print('Date: %s, Type: %s, Total Ridership: %s' %
         (date, 
          daily_summaries[date]['day_type'], 
          daily_summaries[date]['total_ridership']))
    # Print the prior_period_dt, day_type and total_ridership
    print('Date: %s, Type: %s, Total Ridership: %s' %
         (prior_period_dt, 
          daily_summaries[prior_period_dt]['day_type'], 
          daily_summaries[prior_period_dt]['total_ridership']))
quit()

# Finding differences in DateTimes
# object date_ranges for this exercise is missing
# Iterate over the date_ranges
for start_date, end_date in date_ranges:
    # Print the End and Start Date
    print(end_date, start_date)
    # Print the difference between each end and start date
    print(end_date - start_date)
quit()

#######################################################
# HELP! Libraries to make it easier --------------------------------------------
#######################################################
# Pendulum library
# .parse() convert a string to a pendulum datetime object without the need
# of the formating string
# .in_timezone() convert a pendulum object to a desired timezone
# .now() accepts a timezone you want to get the current time in
# .in_XXX() (days, months, years...) provide the difference in a chosen metric
# .in_words() provides the difference in a nice expressive form
# Localizing time with pendulum
# Import the pendulum module
import pendulum

# Create a now datetime for Tokyo: tokyo_dt
tokyo_dt = pendulum.now('Asia/Tokyo')

# Covert the tokyo_dt to Los Angeles: la_dt
la_dt = tokyo_dt.in_timezone('America/Los_Angeles')

# Print the ISO 8601 string of la_dt
print(la_dt.to_iso8601_string())

# Humanizing Differences with Pendulum
# Iterate over date_ranges
for start_date, end_date in date_ranges:

    # Convert the start_date string to a pendulum date: start_dt 
    start_dt = pendulum.parse(start_date, strict = False)
    
    # Convert the end_date string to a pendulum date: end_dt 
    end_dt = pendulum.parse(end_date, strict = False)
    
    # Print the End and Start Date
    print(end_dt, start_dt)
    
    # Calculate the difference between end_dt and start_dt: diff_period
    diff_period = end_dt - start_dt
    
    # Print the difference in days
    print(diff_period.in_days())

#######################################################
