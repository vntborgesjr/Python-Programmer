####################################################
# Data Manipulation with Pandas - Slicing and Indexing
# 26 Out 2020
# VNTBJR
####################################################
# 
# Load packages
library(reticulate)

####################################################
# Explicit indexes ------------------------------
####################################################
# .set_index() - moves a column from the body of the DataFrame to the index
# .reset_index(drop =) - undo what .set_index() did. drop argument allows to 
# dsicard an index
# .sort_index(level =, ascending =) - sorts by index values.By default, it sorts all index levels  
# from outer to inner, in ascending order. The sorting can be controled by passing
# lists to the level and ascending arguments.

# Settindg and removing indexes 
import pandas as pd 
temperatures = pd.read_csv('Datasets/temperatures.csv', sep = ',')

# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop = True))

# Subsetting with .loc[]
# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures['city'].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

# Setting multi-level indexes
# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['country', 'city'])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [('Brazil', 'Rio De Janeiro'), ('Pakistan', 'Lahore')]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])

# Sorting by index values
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level = 'city'))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level = ['country', 'city'], ascending = [True, False]))

####################################################
# section title ------------------------------
####################################################