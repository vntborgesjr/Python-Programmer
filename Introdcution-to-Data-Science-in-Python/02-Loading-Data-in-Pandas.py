# -------------------------------------------------
# Introduction to Data Science in Python - Loading Data in Pandas
# 10 set 2020
# VNTBJR
# ------------------------------------------------
# 
# Load packages ------------------------------------------------
library(reticulate)

# Loading modules ------------------------------------------------
import pandas as pd

# Loading a CSV ------------------------------------------------
credit_records = pd.read_csv('Datasets/ransom.csv', sep = ';')
print(credit_records)

# Inspect a DataFrame ------------------------------------------------
print(credit_records.head())
credit_records.info()

# Select columns ------------------------------------------------
credit_records.price.sum()
plt.plot(ransom['letter'], ransom['frequency'])

# Columns names are strings ------------------------------------------------
print(credit_records.head())

# Selecting with brackets and strings ------------------------------------------------
suspect = credit_records['suspect']
print(suspect)

# Selecting with a dot ------------------------------------------------
price = credit_records.price
print(price)

# Select the column item from credit_records ------------------------------------------------
# Use barckets and string notation
items = credit_records['item']

# Display the results
print(items)

# Use dot notation
items = credit_records.item

# Display the results
print(items)

# Load 'missing puppy reports
mpr = pd.read_csv("datasets/missing puppy reports.csv", sep = ";")

# Use info() to inspect mpr
print(mpr.info())

# Logical statements in Python to select rows ------------------------------------------------
question = 12 * 8 
solution = 96
question == solution
price = 2.25
price > 5
name = 'bayes'
name != 'Bayes'

# Using logic with DataFrames ------------------------------------------------
credit_records.price > 20.00
credit_records[credit_records.price > 20.00]
credit_records[credit_records.price == "Ronald Aylmer Fisher"]

# Logical test ------------------------------------------------
# Test variables
height_inches = 65
plate1 = "FRQ123"
fur_color = "blond"

# Is height_inches > 70
print(height_inches > 70)

# Is plate1 equal to "FRQ123"
print(plate1 == "FRQ123")

# Is fur_color not equal to "brown"?
print(fur_color != 'brown')

# Selecting missing puppies ------------------------------------------------
# Select the dogs where Age is greater than 2
greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)

# Select the dogs whose Status is equal to Still Missing
still_missing = mpr[mpr.Status == "Still Missing"]
print(still_missing)

# Select all dogs whose Dog Breed is not equal to Poodle
not_poodle = mpr[mpr['Dog Breed'] != 'Poodle']
print(not_poodle)

# Select purchases from 'Pet Paradise'
purchase = ____[____.____ ____ 'Pet Paradise']

# Display
print(purchase)

# Select purchases from 'Pet Paradise'
purchase = credit_records[credit_records.location == 'Pet Paradise']

# Display
print(purchase)
