# -------------------------------------------------
# Data Types for Data Science in Python - Dictionaries - the root of Python
# 23 set 2020
# VNTBJR
# ------------------------------------------------
# 
# Load packages 
library(reticulate)

# Using dictionaries ------------------------------------------------
# .get() - allows to supply the name of a key, and optionally, what you'd like to have returned if
# the key is not found
# .update() - updata a dictionary with keys and values from another dictionary, tuples or
# keyword arguments
female_baby_names_2012 = {}
print(records[0])
for row in records:
  if row[0] == "2012" and row[1] == "FEMALE":
    female_baby_names_2012[row[5]] = row[3]
quit()
print(female_baby_names_2012)

# Creating and looping through dictionaries
# Create an empty dictionary: names_by_rank
names_by_rank = {}

# Loop over the girl names
for rank, name in female_baby_names_2012.items() :
    # Add each name to the names_by_rank dictionary using rank as the key
    names_by_rank[rank] = name
quit()

# Sort the names_by_rank dict by rank in descending order and slice the first 10 items
for rank in sorted(names_by_rank, reverse = True)[:10]:
    # Print each item
    print(names_by_rank[rank])
quit()

# Safely finding by key
names = {1: 'EMMA', 2: 'LEAH', 3: 'SARAH', 4: 'SOPHIA', 5: 'ESTHER', 
6: 'RACHEL', 7: 'CHAYA', 8: 'AVA', 9: 'CHANA', 10: 'MIRIAM', 11: 'ELLA', 
12: 'EMILY', 13: 'MIA', 14: 'SARA', 15: 'CHARLOTTE', 16: 'ISABELLA',
17: 'MAYA', 18: 'ELIZABETH', 19: 'ABIGAIL', 20: 'ALEXANDRA', 21: 'VICTORIA',
22: 'LILY', 23: 'SOFIA', 24: 'RIVKA', 25: 'ZOE', 26: 'JULIA', 27: 'SOPHIE',
28: 'GABRIELLA', 29: 'HANNAH', 30: 'GRACE', 31: 'AVERY', 32: 'STELLA',
33: 'SHAINDY', 34: 'FAIGY', 35: 'GITTY', 36: 'MADISON', 37: 'MALKY', 
38: 'EVA', 39: 'MALKA', 40: 'ALEXA', 41: 'MADELINE', 42: 'PENELOPE',
43: 'TOBY', 44: 'RIVKY', 45: 'NICOLE', 46: 'VIOLET', 47: 'NATALIE', 
48: 'REBECCA', 49: 'MARIA', 50: 'YITTY', 51: 'NINA', 52: 'KATHERINE',
53: 'RILEY', 54: 'SIENNA', 55: 'SYDNEY', 56: 'VIVIENNE', 57: 'VALENTINA',
58: 'TALIA', 59: 'JOSEPHINE', 60: 'FRANCESCA', 61: 'ZISSY', 62: 'SURY', 
63: 'NAOMI', 64: 'YIDES', 65: 'SKYLAR', 66: 'VERONICA', 67: 'TAYLOR', 
68: 'ZOEY', 69: 'LILIANA', 70: 'YAEL', 71: 'SAVANNAH', 72: 'VANESSA', 
73: 'SIMONE', 74: 'SLOANE', 75: 'VERA', 76: 'YEHUDIS', 77: 'SYLVIA',
78: 'SIMA', 79: 'SHAINA', 80: 'TZIPORA', 81: 'YITTA', 82: 'TZIVIA', 83: 'YARA'}

# Safely print rank 7 from the names dictionary
print(names.get(7))

# Safely print the type of rank 100 from the names dictionary
print(type(names.get(100)))

# Safely print rank 105 from the names dictionary or 'Not Found'
print(names.get(105, 'Not Found'))

# Dealing with nested data
boy_names = {2012: {}, 2013: {1: 'David', 2: 'Joseph', 3: 'Michael', 4: 'Moshe', 5: 'Daniel', 6: 'Benjamin', 7: 'James', 8: 'Jacob', 9: 'Jack', 10: 'Alexander', 11: 'William', 12: 'John', 13: 'Henry', 14: 'Noah', 15: 'Samuel', 16: 'Nicholas', 17: 'Matthew', 18: 'Adam', 19: 'Chaim', 20: 'Abraham', 21: 'Liam', 22: 'Ryan', 23: 'Lucas', 24: 'Anthony', 25: 'Isaac', 26: 'Oliver', 27: 'Andrew', 28: 'Gabriel', 29: 'Yosef', 30: 'Leo', 31: 'Thomas', 32: 'Luke', 33: 'Jackson', 34: 'Shimon', 35: 'Theodore', 36: 'Joshua', 37: 'Christopher', 38: 'Sebastian', 39: 'Mason', 40: 'Eli', 41: 'Nathan', 42: 'Aaron', 43: 'Zachary', 44: 'Aron', 45: 'Luca', 46: 'Yehuda', 47: 'Yitzchok', 48: 'Owen', 49: 'Menachem', 50: 'Logan', 51: 'Aiden', 52: 'Yisroel', 53: 'Peter', 54: 'Yaakov', 55: 'Yakov', 56: 'Omar', 57: 'Levi', 58: 'Simon', 59: 'Shmuel', 60: 'Patrick', 61: 'Connor', 62: 'Jonah', 63: 'Zev', 64: 'Tzvi', 65: 'Nathaniel', 66: 'Harrison', 67: 'Tyler', 68: 'Mark', 69: 'Hunter', 70: 'Mohamed', 71: 'Lipa', 72: 'Mendel', 73: 'Sean', 74: 'Sam', 75: 'Solomon', 76: 'Martin', 77: 'Edward', 78: 'Wyatt', 79: 'Parker', 80: 'Steven', 81: 'Yechiel', 82: 'Nicolas', 83: 'Timothy', 84: 'Spencer', 85: 'Usher', 86: 'Rafael', 87: 'Yusuf', 88: 'Yehoshua', 89: 'Shaya', 90: 'Rayan', 91: 'Tristan', 92: 'Yossi', 93: 'Wesley', 94: 'Yoel', 95: 'Sawyer', 96: 'Yousef', 97: 'Walter', 98: 'Zalmen', 99: 'Yeshaya', 100: 'Yitzchak'}, 2014: {1: 'Joseph', 2: 'David', 3: 'Michael', 4: 'Moshe', 5: 'Jacob', 6: 'Benjamin', 7: 'Alexander', 8: 'Daniel', 9: 'Samuel', 10: 'Jack', 11: 'James', 12: 'Adam', 13: 'William', 14: 'Henry', 15: 'Abraham', 16: 'Nicholas', 17: 'John', 18: 'Ethan', 19: 'Liam', 20: 'Ryan', 21: 'Noah', 22: 'Matthew', 23: 'Chaim', 24: 'Theodore', 25: 'Isaac', 26: 'Lucas', 27: 'Thomas', 28: 'Yosef', 29: 'Anthony', 30: 'Oliver', 31: 'Max', 32: 'Gabriel', 33: 'Eli', 34: 'Shimon', 35: 'Luke', 36: 'Mason', 37: 'Mordechai', 38: 'Andrew', 39: 'Zachary', 40: 'Owen', 41: 'Yehuda', 42: 'Jackson', 43: 'Yisroel', 44: 'Nathan', 45: 'Aiden', 46: 'Christopher', 47: 'Jonathan', 48: 'Asher', 49: 'Logan', 50: 'Robert', 51: 'Yitzchok', 52: 'George', 53: 'Christian', 54: 'Aron', 55: 'Mark', 56: 'Levi', 57: 'Shmuel', 58: 'Miles', 59: 'Shlomo', 60: 'Peter', 61: 'Sean', 62: 'Eliezer', 63: 'Solomon', 64: 'Gavin', 65: 'Zev', 66: 'Nathaniel', 67: 'Yaakov', 68: 'Yakov', 69: 'Hunter', 70: 'Vincent', 71: 'Ari', 72: 'Edward', 73: 'Yechiel', 74: 'Oscar', 75: 'Shia', 76: 'Leonardo', 77: 'Victor', 78: 'Tyler', 79: 'Wyatt', 80: 'Sam', 81: 'Shaya', 82: 'Ian', 83: 'Raphael', 84: 'Philip', 85: 'Timothy', 86: 'Yehoshua', 87: 'Xavier', 88: 'Youssef', 89: 'Simcha', 90: 'Naftali', 91: 'Ronan', 92: 'Usher', 93: 'Shmiel', 94: 'Yousef', 95: 'Naftuli', 96: 'Yusuf', 97: 'Yossi', 98: 'Yisrael', 99: 'Shea', 100: 'Yoel', 101: 'Yahya', 102: 'Yidel'}}

# Print a list of keys from the boy_names dictionary
print(boy_names.keys())

# Print a list of keys from the boy_names dictionary for the year 2013
print(boy_names[2013].keys())

# Loop over the dictionary
for year in boy_names:
    # Safely print the year and the third ranked name or 'Unknown'
    print(year, boy_names[year].get(3, "Unknown"))
quit()

# Adding and extending dictionaries
boy_names = {2012: {}, 2013: {1: 'David', 2: 'Joseph', 3: 'Michael', 4: 'Moshe', 5: 'Daniel', 6: 'Benjamin', 7: 'James', 8: 'Jacob', 9: 'Jack', 10: 'Alexander', 11: 'William', 12: 'John', 13: 'Henry', 14: 'Noah', 15: 'Samuel', 16: 'Nicholas', 17: 'Matthew', 18: 'Adam', 19: 'Chaim', 20: 'Abraham', 21: 'Liam', 22: 'Ryan', 23: 'Lucas', 24: 'Anthony', 25: 'Isaac', 26: 'Oliver', 27: 'Andrew', 28: 'Gabriel', 29: 'Yosef', 30: 'Leo', 31: 'Thomas', 32: 'Luke', 33: 'Jackson', 34: 'Shimon', 35: 'Theodore', 36: 'Joshua', 37: 'Christopher', 38: 'Sebastian', 39: 'Mason', 40: 'Eli', 41: 'Nathan', 42: 'Aaron', 43: 'Zachary', 44: 'Aron', 45: 'Luca', 46: 'Yehuda', 47: 'Yitzchok', 48: 'Owen', 49: 'Menachem', 50: 'Logan', 51: 'Aiden', 52: 'Yisroel', 53: 'Peter', 54: 'Yaakov', 55: 'Yakov', 56: 'Omar', 57: 'Levi', 58: 'Simon', 59: 'Shmuel', 60: 'Patrick', 61: 'Connor', 62: 'Jonah', 63: 'Zev', 64: 'Tzvi', 65: 'Nathaniel', 66: 'Harrison', 67: 'Tyler', 68: 'Mark', 69: 'Hunter', 70: 'Mohamed', 71: 'Lipa', 72: 'Mendel', 73: 'Sean', 74: 'Sam', 75: 'Solomon', 76: 'Martin', 77: 'Edward', 78: 'Wyatt', 79: 'Parker', 80: 'Steven', 81: 'Yechiel', 82: 'Nicolas', 83: 'Timothy', 84: 'Spencer', 85: 'Usher', 86: 'Rafael', 87: 'Yusuf', 88: 'Yehoshua', 89: 'Shaya', 90: 'Rayan', 91: 'Tristan', 92: 'Yossi', 93: 'Wesley', 94: 'Yoel', 95: 'Sawyer', 96: 'Yousef', 97: 'Walter', 98: 'Zalmen', 99: 'Yeshaya', 100: 'Yitzchak'}, 2014: {1: 'Joseph', 2: 'David', 3: 'Michael', 4: 'Moshe', 5: 'Jacob', 6: 'Benjamin', 7: 'Alexander', 8: 'Daniel', 9: 'Samuel', 10: 'Jack', 11: 'James', 12: 'Adam', 13: 'William', 14: 'Henry', 15: 'Abraham', 16: 'Nicholas', 17: 'John', 18: 'Ethan', 19: 'Liam', 20: 'Ryan', 21: 'Noah', 22: 'Matthew', 23: 'Chaim', 24: 'Theodore', 25: 'Isaac', 26: 'Lucas', 27: 'Thomas', 28: 'Yosef', 29: 'Anthony', 30: 'Oliver', 31: 'Max', 32: 'Gabriel', 33: 'Eli', 34: 'Shimon', 35: 'Luke', 36: 'Mason', 37: 'Mordechai', 38: 'Andrew', 39: 'Zachary', 40: 'Owen', 41: 'Yehuda', 42: 'Jackson', 43: 'Yisroel', 44: 'Nathan', 45: 'Aiden', 46: 'Christopher', 47: 'Jonathan', 48: 'Asher', 49: 'Logan', 50: 'Robert', 51: 'Yitzchok', 52: 'George', 53: 'Christian', 54: 'Aron', 55: 'Mark', 56: 'Levi', 57: 'Shmuel', 58: 'Miles', 59: 'Shlomo', 60: 'Peter', 61: 'Sean', 62: 'Eliezer', 63: 'Solomon', 64: 'Gavin', 65: 'Zev', 66: 'Nathaniel', 67: 'Yaakov', 68: 'Yakov', 69: 'Hunter', 70: 'Vincent', 71: 'Ari', 72: 'Edward', 73: 'Yechiel', 74: 'Oscar', 75: 'Shia', 76: 'Leonardo', 77: 'Victor', 78: 'Tyler', 79: 'Wyatt', 80: 'Sam', 81: 'Shaya', 82: 'Ian', 83: 'Raphael', 84: 'Philip', 85: 'Timothy', 86: 'Yehoshua', 87: 'Xavier', 88: 'Youssef', 89: 'Simcha', 90: 'Naftali', 91: 'Ronan', 92: 'Usher', 93: 'Shmiel', 94: 'Yousef', 95: 'Naftuli', 96: 'Yusuf', 97: 'Yossi', 98: 'Yisrael', 99: 'Shea', 100: 'Yoel', 101: 'Yahya', 102: 'Yidel'}}
names_2011 = {1: 'Michael', 2: 'Joseph', 3: 'Jacob', 4: 'David', 5: 'Benjamin', 6: 'Moshe', 7: 'Daniel', 8: 'Alexander', 9: 'Matthew', 10: 'Jack', 11: 'Samuel', 12: 'James', 13: 'William', 14: 'John', 15: 'Nicholas', 16: 'Henry', 17: 'Chaim', 18: 'Anthony', 19: 'Andrew', 20: 'Liam', 21: 'Charles', 22: 'Lucas', 23: 'Dylan', 24: 'Ryan', 25: 'Thomas', 26: 'Ethan', 27: 'Menachem', 28: 'Yosef', 29: 'Luke', 30: 'Oliver', 31: 'Noah', 32: 'Eli', 33: 'Gabriel', 34: 'Max', 35: 'Shimon', 36: 'Isaac', 37: 'Joshua', 38: 'Zachary', 39: 'Leo', 40: 'Julian', 41: 'Aiden', 42: 'Jake', 43: 'Mordechai', 44: 'Yisroel', 45: 'Yehuda', 46: 'Sebastian', 47: 'Mark', 48: 'Robert', 49: 'Logan', 50: 'George', 51: 'Owen', 52: 'Vincent', 53: 'Tyler', 54: 'Yakov', 55: 'Aidan', 56: 'Yitzchok', 57: 'Asher', 58: 'Theodore', 59: 'Peter', 60: 'Solomon', 61: 'Zev', 62: 'Nathaniel', 63: 'Yaakov', 64: 'Shmuel', 65: 'Shulem', 66: 'Tzvi', 67: 'Levi', 68: 'Jayden', 69: 'Mohamed', 70: 'Cole', 71: 'Sean', 72: 'Sam', 73: 'Victor', 74: 'Omar', 75: 'Steven', 76: 'Moses', 77: 'Shia', 78: 'Usher', 79: 'Nicolas', 80: 'Yechiel', 81: 'Shaya', 82: 'Wyatt', 83: 'Tristan', 84: 'Louis', 85: 'Yehoshua', 86: 'Sholom', 87: 'Yoel', 88: 'Rocco', 89: 'Xavier', 90: 'Yitzchak', 91: 'Shea', 92: 'Spencer', 93: 'Zalmen', 94: 'Yida', 95: 'Yousef', 96: 'Youssef', 97: 'Yonah'}

# Assign the names_2011 dictionary as the value to the 2011 key of boy_names
boy_names[2011] = names_2011

# Update the 2012 key in the boy_names dictionary
boy_names[2012].update([(1, 'Casey'), (2, 'Aiden')])

# Loop over the years in the boy_names dictionary 
for year in boy_names :
    # Sort the data for each year by descending rank and get the lowest one
    lowest_ranked =  sorted(boy_names[year], reverse=True)[0]
    # Safely print the year and the least popular name or 'Not Available'
    print(year, boy_names[year].get(lowest_ranked, 'Not Available'))
quit()

# Popping and deleting from dictionaries
female_names ={2011: {1: 'Olivia', 2: 'Esther', 3: 'Rachel', 4: 'Leah', 5: 'Emma', 6: 'Chaya', 7: 'Sarah', 8: 'Sophia', 9: 'Ava', 10: 'Miriam'}, 2012: {}, 2013: {1: 'Olivia', 2: 'Emma', 3: 'Esther', 4: 'Sophia', 5: 'Sarah', 6: 'Leah', 7: 'Rachel', 8: 'Chaya', 9: 'Miriam', 10: 'Chana'}, 2014: {1: 'Olivia', 2: 'Esther', 3: 'Rachel', 4: 'Leah', 5: 'Emma', 6: 'Chaya', 7: 'Sarah', 8: 'Sophia', 9: 'Ava', 10: 'Miriam'}}

# Remove 2011 from female_names and store it: female_names_2011
female_names_2011 = female_names.pop(2011)

# Safely remove 2015 from female_names with an empty dictionary as the default: female_names_2015
female_names_2015 = female_names.pop(2015, {})

# Delete 2012 from female_names
del female_names[2012]

# Print female_names
print(female_names)

# Working with dictionaries more pythonically
baby_names = {2012: {}, 2013: {1: 'David', 2: 'Joseph', 3: 'Michael', 4: 'Moshe', 5: 'Daniel', 6: 'Benjamin', 7: 'James', 8: 'Jacob', 9: 'Jack', 10: 'Alexander'}, 2014: {1: 'Joseph', 2: 'David', 3: 'Michael', 4: 'Moshe', 5: 'Jacob', 6: 'Benjamin', 7: 'Alexander', 8: 'Daniel', 9: 'Samuel', 10: 'Jack'}}
# Iterate over the 2014 nested dictionary
for rank, name in baby_names[2014].items():
    # Print rank and name
    print(rank, name)
quit()    
# Iterate over the 2012 nested dictionary
for rank, name in baby_names[2012].items : 
    # Print rank and name
  print(rank, name)
quit()

# Checking dictionaries for data
# Check to see if 2011 is in baby_names
if 2011 in baby_names:
    # Print 'Found 2011'
    print('Found 2011')
quit()

# Check to see if rank 1 is in 2012
if 1 in baby_names[2012]:
    # Print 'Found Rank 1 in 2012' if found
    print('Found Rank 1 in 2012')
else:
    # Print 'Rank 1 missing from 2012' if not found
    print('Rank 1 missing from 2012')
quit()

# Check to see if Rank 5 is in 2013
if 5 in baby_names[2013]:
   # Print 'Found Rank 5'
   print('Found Rank 5')
quit()

#######################################################
# Working with CSV files ------------------------------------------------
# csv module
# open() - provides a variable that represents a file, takes a path and 
# a mode ('r' for read or 'w' for write)
# .reader() - reads a file object and returns the lines from the files as tuple
# .close() method closes file objects
# Reading from a file using CSV reader
baby_names = {}
# Import the python CSV module
import csv

# Create a python file object in read mode for the baby_names.csv file: csvfile
csvfile = open("Datasets/babynames.csv", mode = 'r')

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):
    # Print each row 
    print(row)
    # Add the rank and name to the dictionary
    baby_names[row[5]] = row[3]
quit()
# Print the dictionary keys
print(baby_names.keys())

csvfile.close()

# Creting a dictionary from a file
baby_names = {}
# Import the python CSV module
import csv

# Create a python file object in read mode for the `baby_names.csv` file: csvfile
csvfile = open("Datasets/babynames.csv", mode = 'r')

# Loop over a DictReader on the file
for row in csv.DictReader(csvfile):
    # Print each row 
    print(row)
    # Add the rank and name to the dictionary: baby_names
    baby_names[row['RANK']] = row['NAME']
quit()
# Print the dictionary keys
print(baby_names.keys())

csvfile.close()

#######################################################

