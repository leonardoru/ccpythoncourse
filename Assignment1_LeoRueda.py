# Class: CIS 112 #37791 ADVANCED PROGRAMMING USING PYT-Online
# Pasadena City College
# Instructor: Mr. Jason Y. Huh
# Assignment 1: Write a Python program that calculates leap years

# Student: Leonardo Rueda

year = int(input("Please enter the 4 digit year: "))
month = int(input("Please enter the month number: "))

# Array of months that have 31 days:
if month in [1, 3, 5, 7, 8, 10, 12]:
    num_days = 31
# Array of months that have 31 days:
elif month in [4, 6, 9, 11]:
    num_days = 30
# Logic for month 2:
else:
    # Check if it is a leap year
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        num_days = 29
    else:
        num_days = 28
# Array with month names for user response
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]
# Result
print(month_names[month - 1], year, "has", num_days, "days.")

# By Leonardo Rueda