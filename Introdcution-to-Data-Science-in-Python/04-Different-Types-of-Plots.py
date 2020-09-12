# -------------------------------------------------
# Introduction to Data Science in Python - Different Types of Plots
# 10 set 2020
# VNTBJR
# ------------------------------------------------
# 
# Load packages ------------------------------------------------
library(reticulate)

# Loading modules ------------------------------------------------
import pandas as pd
from matplotlib import pyplot as plt

# Creating a scatter plot ------------------------------------------------
plt.scatter(df.age, df.height)
plt.xlabel('Age (in months)')
plt.ylabel('Height (in inches)')
plt.show()

# Changing style
plt.scatter(df.age, df.height, color = 'green', marker = 's')

# Changing marker transparency
plt.scatter(df.x_data, df.y_data, alpha = 0.1)

# Charting cellphone data ------------------------------------------------
cellphone = pd.read_csv('Datasets/cellphone.csv', sep = ';')
# Explore data
print(cellphone.head)

# Create a scatter plot of the data from the DataFrame cellphone
plt.scatter(cellphone.x, cellphone.y)

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()

# Modifying a scatterplot
# Change the marker color to red
plt.scatter(cellphone.x, cellphone.y,
           color = 'red')

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()

# Change the marker shape to square
plt.scatter(cellphone.x, cellphone.y,
           color='red',
           marker = 'square')

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()

# Change the transparency to 0.1
plt.scatter(cellphone.x, cellphone.y,
           color='red',
           marker='s',
           alpha = 0.1)

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()

# Making a bar chart ------------------------------------------------
plt.bar(df.percinct, df.pets_abducted)
plt.ylabel('Pet Abductoins')
plt.show()

# Horizontal barcharts
plt.barh(df.precinct, df.pets_abducted)
plt.ylabel('Pet Abductions')
plt.show()

# Adding error bars
plt.bar(df.precinctm df.pet_abductions, yerr = df.error)
plt.label('Pet Abductions')
plt.show()

# Stacked bar charts
plt.bar(df.precinct, df.dog, label = 'Dog')
plt.bar(df.precinct, df.cat, bottom = df.dog, label = 'Cat')
plt.legend()
plt.show()

# Built a simple bar chart ------------------------------------------------
hours = pd.read_csv('Datasets/hours.csv', sep = ';')

# Display the DataFrame hours using print
print(hours)

# Create a bar plot from the DataFrame hours and add error boars
plt.bar(hours.officer, hours.avg_hours_worked, yerr = hours.std_hours_worked)

# Display the plot
plt.show()

# Where did the time go? ------------------------------------------------
# Plot the number of hours spent on desk work
plt.bar(hours.officer, hours.desk_work, label = "Desk Work")

# Plot the hours spent on field work on top of desk work
plt.bar(hours.officer, hours.field_work, bottom = hours.desk_work, label = 'Field Work')

# Add a legend
plt.legend()

# Display the plot
plt.show()

# Making a histogram ------------------------------------------------
plt.hist(gravel.mass)
plt.show()

# Changing bins
plt.hist(gravel.mass, bins = 40)

# Changing range
plt.hist(gravel.mass, range = (50, 100))

# Normalizing
plt.hist(male_weight, density = True)
plt.hist(female_weight, density = True)

# Modifying histograms ------------------------------------------------
puppies = pd.read_csv('Datasets/puppuies.csv', sep = ';')

# Create a histogram of the column weight
# from the DataFrame puppies
plt.hist(puppies.weight)

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()

# Change the number of bins to 50
plt.hist(puppies.weight,
        bins = 50)

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()

# Change the range to start at 5 and end at 35
plt.hist(puppies.weight,
        range=(5, 35))

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show

# Heroes with histograms ------------------------------------------------
gravel = pd.read_csv('Datasets/gavel.csv', sep = ';')
# Create a histogram of gravel.radius
plt.hist(gravel.radius)

# Display histogram
plt.show()

# Create a histogram
# Range is 2 to 8, with 40 bins
plt.hist(gravel.radius, range = (2, 8), bins = 40)

# Display histogram
plt.show()

# Create a histogram
# Normalize to 1
plt.hist(gravel.radius,
         bins=40,
         range=(2, 8),
         density = True)

# Display histogram
plt.show()

# Create a histogram
plt.hist(gravel.radius,
         bins=40,
         range=(2, 8),
         density=True)

# Label plot
plt.xlabel('Gravel Radius (mm)')
plt.ylabel('Frequency')
plt.title('Sample from Shoeprint')

# Display histogram
plt.show()
