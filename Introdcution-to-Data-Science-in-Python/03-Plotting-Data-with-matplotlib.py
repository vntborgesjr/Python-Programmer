# -------------------------------------------------
# Introduction to Data Science in Python - Plotting Data with matplotlib
# 10 set 2020
# VNTBJR
# ------------------------------------------------
# 
# Load packages ------------------------------------------------
library(reticulate)

# Loading modules ------------------------------------------------
import pandas as pd
from matplotlib import pyplot as plt

# Pandas loads our data ------------------------------------------------

deshaun = pd.read_csv('Datasets/deshaun.csv', sep = ";")
aditya = pd.read_csv('Datasets/aditya.csv', sep = ";")
mengfei = pd.read_csv('Datasets/mengfei.csv', sep = ";")
six_months = pd.read_csv('Datasets/six_months.csv', sep = ";")

# Plot Officer Deshaun's hours_worked vs. day_of_week ------------------------------------------------

plt.plot(deshaun.day_of_week, deshaun.hours_worked)
plt.show()

# Plot Officer Aditya's hours_worked vs. day_of_week ------------------------------------------------
plt.plot(aditya.day_of_week, aditya.hours_worked)

# Plot Officer Mengfei's hours_worked vs. day_of_week
plt.plot(mengfei.day_of_week, mengfei.hours_worked)

# Adding legends ------------------------------------------------
# Add a label to Deshaun's plot
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label = 'Deshaun')

# Officer Aditya
plt.plot(aditya.day_of_week, aditya.hours_worked, label = 'Aditya')

# Officer Mengfei
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label = 'Mengfei')

# Display legend
plt.legend()

# Adding labbels ------------------------------------------------
# Lines
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a title
plt.title("Worked Hours")

# Add y-axis label
plt.ylabel("Hours of work")

# Legend
plt.legend()
# Display plot
plt.show()

# Adding floating text ------------------------------------------------
# Create plot
plt.plot(six_months.month, six_months.hours_worked)

# Add annotation "Missing June data" at (2.5, 80)
plt.text(2.5, 80, "Missing June data")

# Display graph
plt.show()

# Adding some style ------------------------------------------------
# Changing line color
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
plt.plot(x, y1, color = "tomato")
plt.plot(x, y2, color = "orange")
plt.plot(x, y3, color = "goldenrod")
plt.plot(x, y4, color = "seagreen")
plt.plot(x, y5, color = "dodgerblue")
plt.plot(x, y6, color = "violet")

# Changing line width
plt.plot(x, y1, linewidth = 1)
plt.plot(x, y2, linewidth = 2)
plt.plot(x, y3, linewidth = 3)
plt.plot(x, y4, linewidth = 4)
plt.plot(x, y5, linewidth = 5)
plt.plot(x, y6, linewidth = 6)

# Changing line style
plt.plot(x, y1, linestyle = '-')
plt.plot(x, y2, linestyle = '--')
plt.plot(x, y3, linestyle = '-.')
plt.plot(x, y4, linestyle = ':')

# Adding markers
plt.plot(x, y1, marker = 'x')
plt.plot(x, y2, marker = 's')
plt.plot(x, y3, marker = 'o')
plt.plot(x, y4, marker = 'd')
plt.plot(x, y5, marker = '*')
plt.plot(x, y6, marker = 'h')

# Setting a style (before any other plotting code)
plt.style.use('fivethirtyeight')
plt.style.use('ggplot')
plt.style.use('seaborn')
plt.style.use('default')

# Modifying font size
plt.title('Plot title', fontsize = 20) 

# Modifying font color
plt.legend(color = 'green') # change font color

# Tracking crimes statistics ------------------------------------------------
data = pd.read_csv('Datasets/data.csv', sep = ';')

# Changing the color of Phoenix to 'DarkCyan'
plt.plot(data['Year'], data['Phoenix Police Dept'], label = 'Phoenix', color = 'DarkCyan')

# Make the Los Angeles line dotted
plt.plot(data['Year'], data['Los Angeles Police Dept'], label = 'Los Angeles', linestyle = ':')

# Add square markers to Philadelphia
plt.plot(data['Year'], data['Philadelphia Police Dept'], label = 'Philadelphia', marker = 's')

# Add a legend
plt.legend()

# Display the plot
plt.show()

# Playing with styles ------------------------------------------------
# Changing the style to fivethirtyeight
plt.style.use('fivethirtyeight')

# Plot lines
plt.plot(data['Year'], data['Phoenix Police Dept'], label = 'Phoenix')
plt.plot(data['Year'], data['Los Angeles Police Dept'], label = 'Los Angeles')
plt.plot(data['Year'], data['Philadelphia Police Dept'], label = 'Philadelphia')

# Add a legend
plt.legend()

# Display the plot
plt.show()

# Change the style to ggplot
plt.style.use('ggplot')

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()

# View all styles
print(plt.style.available)

# Choose any of the styles
plt.style.use('dark_background')

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()

# Identifying Bayes' Kidenepper ------------------------------------------------
suspect1 = pd.read_csv('Datasets/suspect1.csv', sep = ';')
suspect2 = pd.read_csv('Datasets/suspect2.csv', sep = ';')

# Plot the letter frequency from the ransom note. The x-values should be 
# ransom.letter. The y-values should be ransom.frequency. The label should be the 
# string 'Ransom'. The line should be gray
plt.plot(ransom.letter, ransom.frequency, label = 'Ransom', linestyle = ':', color = 'gray')

# Display plot 
plt.show()

# Plot a line for each data in suspect1. Use a keyword argument to label that line
# 'Fred Frequentist'
plt.plot(suspect1.letter, suspect1.frequency, label = "Fred Frequentist")

# Display the plot
plt.show()

# Plot a line for the data in suspect2 (labled 'Gertrude Cox')
plt.plot(suspect2.letter, suspect2.frequency, label = "Gertrude Cox")

# Display the plot
plt.show()

# Label the x-axis (Letter) and the y-axis (Frequency), and add a legend
# Add x- and y-labels
plt.xlabel("Letter")
plt.ylabel("Frequency")

# Add a legend
plt.legend()

# Display plot
plt.show()
