# -------------------------------------------------
# Introduction to Data Science in Python - Getting Started in Python
# 10 set 2020
# VNTBJR
# ------------------------------------------------
# 
# Load packages ------------------------------------------------

library(reticulate)

# Load modules ------------------------------------------------

import pandas as pd
from matplotlib import pyplot as plt

# Pandas loads our data ------------------------------------------------

ransom = pd.read_csv('Datasets/ransom.csv', sep = ";")

# Matplotlib plots and displays ------------------------------------------------

plt.plot(ransom.letter, ransom.frequency)
plt.show()

# Use an import statement to import statsmodels ------------------------------------------------

import statsmodels

# Import statsmodels under the alias sm ------------------------------------------------

import statsmodels as sm

# Use an import statement to import seaborn with alias sns ------------------------------------------------

import seaborn as sns

# Fix the import of numpy to run without errors ------------------------------------------------

import numpy as np

# Filing a missing puppy report with variables ------------------------------------------------

name = 'Bayes' 
height = 24
weight = 75.5

# Floats and Strings ------------------------------------------------
# floats represents an integer or decimal number

heigh = 24
weight = 75.5

# string representes text

name = "Bayes"
breed = 'Golden Retriever'

# Displaying variables ------------------------------------------------

print(height)

# Creating a float ------------------------------------------------

# Fill in Bayes' age (4.0)

bayes_age = 4.0
print(bayes_age)

# Create strings ------------------------------------------------

# Bayes' favorite  toy

favorite_toy = "Mr. Squeaky"

# Bayes' owner
owner = 'DataCamp'

# Display variables

print(favorite_toy)
print(owner)

# Functions in code ------------------------------------------------

# Import pandas

import pandas as pd

# Load the 'ransom.csv' into a DataFrame

ransom = pd.read_csv('Datasets/ransom.csv', sep = ";")

# Display DataFrame

print(r)

# Plot a graph

x_values = ransom.letter
y_values = ransom.frequency
plt.plot(x_values, y_values)

# Display the graph

plt.show()

# define the function lookup_plate()

def lookup_plate(plate, color):
  if color == 'Green':
    print('Fred Frequentist \nJohn W. Tukey \nRonald Aylmer Fisher \nKarl Pearson \nGertrude Cox \nKristine Smith')
  else:
    print('Fred Frequentist \nRonald Aylmer Fisher \nGertrude Cox \nKristine Smith')
  
# Define plate to represent a plate beginning with FRQ
# Use * to represent the missing four letters

plate = 'FRQ****'

# Call the function lookup_plate()

lookup_plate(plate, color = '')
