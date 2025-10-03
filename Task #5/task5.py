# Q No 01
# Write a Python program to print the numbers from 1 to 10 using a for loop.

# for i in range(1, 11):
#     print(i)

# Q No 02
# Write a Python program to print the numbers from 20 to 1 using a while loop. 
# Print numbers from 20 to 1 using while loop

# i = 20
# while i >= 1:
#     print(i)
#     i -= 1

# Q No 03
# Write a program to print even numbers from 1 to 10.   

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)

# Q No 04
# Write a program that prompts the user to enter a number n and prints all the 
# numbers from 1 to n.   

# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     print(i)

# Q No 05
# Write a program that prompts the user to enter a number n, and then prints all the 
# odd numbers between 1 and n.  

# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     if i % 2 ==1:
#         print(i)

# Q No 06
# Write a program that prints 'Happy Birthday!' five times on screen. 

# for i in range(5):
#     print("Happy Barthday!")

# Program to print the first n terms of square series

# Q No 07
# Write a program that takes a number n as input from the user and generates the first 
# n terms of the series formed by squaring the natural numbers. 
# Sample output 
# Enter a number: 6 
# The first 6 terms of the series are: 
# 1 4 9 16 25 36

# n = int(input("Enter a number: "))

# print("The first", n, "terms of the series are:")

# for i in range(1, n + 1):
#     print(i * i, end=" ")

# Q no 08
#  Write a program that prompts the user to input a number and prints its multiplication 
# table. 

n = int(input("Enter a number: "))

print("Multiplication Table of", n)

for i in range(1, 11):
    print(n, "x", i, "=", n * 1)


