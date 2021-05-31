# Class: CIS 112 #37791 ADVANCED PROGRAMMING USING PYT-Online
# Pasadena City College
# Instructor: Mr. Jason Y. Huh
# Assignment 4: Write a Python program that identifies prime numbers
# Student: Leonardo Rueda

repeat = True
while repeat:   
    num = input('What is the number you would like to check?')
    num = int(num)
    
    # If given number is greater than 1
    if num > 1:
    
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
    
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    
    else:
        print(num, "is not a prime number")
    repe = input('Would you like to try again?, (y,n)')
    if repe == 'n' or repe == 'N' or  repe == 'no' or  repe == 'No':
        repeat = False
        print ('Goodbye')
