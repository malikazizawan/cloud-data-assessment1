# Q No 01
# Write a program that accepts a string from user. Your program should count and display number of vowels in that string.

# text = input("Enter a string: ")
# count = 0
# vowels = "aeiouAEIOU"

# for char in text:
#     if char in vowels:
#         count += 1

# print("Number of vowels in the string:", count)

# Q No 02
# write a program that reads a string from keybord and display the number of upercase letters in the string the number of lowercase letters in the string the number of digits in the string the number of whitespace corector in the string

# text = input("Enter a string")

# upper_count = 0 
# lower_count = 0
# digit_count = 0
# space_count = 0

# for char in text:
#     if char.isupper():
#         upper_count += 1
#     elif char.islower():
#         lower_count += 1
#     elif char.isdigit():
#         digit_count += 1
#     elif char.isspace():
#         space_count += 1

# print("Uppercase letters:", upper_count)
# print("Lowercase letters:", lower_count)
# print("Digits:", digit_count)
# print("Whitespace characters:", space_count)


# write a python program that accepts a string from user. your program should create and display a new string where the first and last characters have been exchange.
text = input("Enter a string: ")

if len(text) <= 1:
    new_text = text
else:
    first_char = text[0]
    last_char = text[-1]

    middle = text[1:-1]

    new_text = last_char + middle + first_char

print("New String:" , new_text)

# Q 04
#  Write a Python program that accepts a string from user. Your program should create a new string in 
# reverse of first string and display it.

text = input("Enter another string: ")

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text   # har naya char ko pehle lagana

print("Reversed string using loop:", reversed_text)

# Q No 06
#  Write a Python program that accepts a string from user. Your program should create a new string by 
# shifting one position to left. 

text = input("Enter a string: ")

if len(text) <= 1:
    new_text = text
else:
    
    new_text = text[1:] + text[0]

print("New String:", new_text)

# Q No 08
# String rotation program
# Write a program that display following output: 
# SHIFT 
# HIFTS 
# IFTSH 
# FTSHI 
# TSHIF 
# SHIFT 

word = "SHIFT"

for i in range(len(word) + 1): 
    print(word)
   
    word = word[1:] + word[0]

# Q No 09
# Write a program in python that accepts a string to setup a passwords. Your entered password must 
# meet the following requirements:

import re  # Regular expression module

password = input("Enter your password: ")

# Conditions check karne ke liye flags
valid = True

if len(password) < 8:
    print("Password must be at least 8 characters long.")
    valid = False

if not re.search("[A-Z]", password):
    print("Password must contain at least one uppercase letter.")
    valid = False

if not re.search("[a-z]", password):
    print("Password must contain at least one lowercase letter.")
    valid = False

if not re.search("[0-9]", password):
    print("Password must contain at least one digit.")
    valid = False

if not re.search("[@#$%^&*]", password):
    print("Password must contain at least one special character (@, #, $, %, &, *).")
    valid = False

if valid:
    print("Password is strong and accepted!")
else:
    print("Please try again with a stronger password.")



