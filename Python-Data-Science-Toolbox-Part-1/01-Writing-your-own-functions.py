####################################################
# Python Data Science Toolbox (Part 1) - Writing your own functions
# 29 Out 2020
# VNTBJR
####################################################
#
# Load packages
library(reticulate)

####################################################
# Use-defined functions ------------------------------
####################################################
# Define a function
def square(): # <- Function header
    new_value = 4 ** 2 # <- Function body
    print(new_value)
quit()
square()

# Function parameters
# Define a function
def square(value): # <- Function header with one parameter
    new_value = value ** 2 # <- Function body with one parameter
    print(new_value)
quit()
square(5)

# Return values from functions
# Define a function
def square(value): # <- Function header
    new_value = value ** 2 # <- Function body
    return(new_value)
quit()
num = square(4) # now we can assign to a variable num the result of the function
# call
print(num)

# Docstrings describe what your function does and serve as documentation for your 
# function. It's placed in the immediate line affter the function header, in 
# between triple quotation marks ''' '''
def square(value): # <- Function header
    ''' Return the square of a value''' # appropriate Docstring for our square function
    new_value = value ** 2 # <- Function body
    return(new_value)
quit()

# Strings in Python
object1 = 'data' + 'analysis' + 'visualization'
object2 = 1 * 3
object3 =  '1' * 3
print(object1, object2, object3)

# Recapping built-in functions
x = 4.89
y1 = str(x)
y2 = print(x) # assingn a variable to a function that prints a value but not 
# return a value will result in that variable being of type NoneType
type(x)
type(y1)
type(y2)

# Write a simple function
# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations' + '!!!'
    # Print shout_word
    print(shout_word)
quit()
# Call shout
shout()

# Single-parameter functions
# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'
    # Print shout_word
    print(shout_word)
quit()

# Call shout with the string 'congratulations'
shout('congratulations')

# Functions that return single values
# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'
    # Replace print with return
    return(shout_word)
quit()
# Pass 'congratulations' to shout: yell
yell = shout('congratulations')

# Print yell
print(yell)

####################################################
# Multiple Parameters and Return Values ------------------------------
####################################################
#
# Multiple fucntion parameters 
def raise_to_power(value1, value2):
    '''Raise value1 to the power of value2'''
    new_value = value1 ** value2
    return(new_value)
quit()

result = raise_to_power(2, 3)
print(result)

# Return multiple values using tuples
def raise_to_power(value1, value2):
    '''Raise value1 to the power of value2'''
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    new_tuple = (new_value1, new_value2)
    return(new_tuple)
quit()

result = raise_to_power(2, 3)
print(result)

# Unpacking tuple in different variable
a, b = result
print(a)
print(b)

# Functions with multiple parameters
# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    # Concatenate shout1 with shout2: new_shout
    new_shout = shout1 + shout2
    # Return new_shout
    return(new_shout)
quit()
# Pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulation', 'you')

# Print yell
print(yell)

# A brief introduction to tuples
nums = (3, 4, 6)
# Unpack nums into num1, num2, and num3
num1,  num2, num3 = nums

# Construct even_nums
even_nums = (2, num2, num3)

# Functions that return multiple values
# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)
    # Return shout_words
    return(shout_words)
quit()
# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')

# Print yell1 and yell2
print(yell1)
print(yell2)

####################################################
# Bringing it all together ------------------------------
####################################################
#
# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv('Datasets/tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:
    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1
quit()
# Print the populated dictionary
print(langs_count)

# Bring it all together (2)
tweets_df = pd.read_csv('Datasets/tweets.csv')

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""
    # Initialize an empty dictionary: langs_count
    langs_count = {}
    # Extract column from DataFrame: col
    col = df[col_name]
    # Iterate over lang column in DataFrame
    for entry in col:
        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1
    # Return the langs_count dictionary
    return(langs_count)
quit()
# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)