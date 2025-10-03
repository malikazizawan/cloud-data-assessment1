# Q No 01
# A company decided to give bonus of 5% to employee if his/her year of service 
# is more than 5 years. Ask user for their salary and year of service and
#  print the net bonus amount.

salary = int(input("Inter Your Salary"))
service = int(input("Inter Your Jop Years"))

if service > 5:
    bonus = salary * 0.05
    print("Your Bonus is:", bonus)
else:
    print("No Bonus")

# Q No 02
# Write a program to check whether a person is eligible for voting or not. (accept age from user) 
# if age is greater than 17 eligible otherwise not eligible

age = int(input("Inter Your Age"))
if(age > 17):
    print("Eligible for vote")
else:
    print("Not Eligible For Vote")

# Q No 03
# Write a program to check whether a number entered by user is even or odd.

num = int(input("Enter Your Number"))

if(num % 2 == 0):
    print("Your Number Is Odd")
else:
    print("Your Number Is Even")

# Q No 04
# Write a program to check whether a number is divisible by 7 or not. Show Answer
num_d = int(input("Enter Your Number"))

if(num_d % 7 == 0):
    print("a number is divisible by 7")
else:
    print("a number is Not divisible by 7")

# Q No 5
# Write a program to display "Hello" 
# if a number entered by user is a multiple of five , otherwise print "Bye".

num_m = int(input("Enter Your Number"))\

if(num_m % 5 == 0):
    print("Hello")
else:
    print("Bye")

# Q No 07
# Write a program to display the last digit of a number.

num = input("Enter Your Number or Any Name")
print("Last Digit is:", num[-1])

# Q No 09
# Take values of length and breadth of a rectangle from user and print if it is square or rectangle.

length = int(input("Enter Length: "))
breadth = int(input("Enter Breadth: "))

if length == breadth:
    print("It is a Square")
else:
    print("It is a Rectangle")

# Q No 10
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

if a > b:
    print("Greatest Number is:", a)
else:
    print("Greatest Number is:", b)

# Q No 11
# A shop will give discount of 10% if the cost of purchased quantity is more than 1000. 
# Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

quantity = int(input("Enter Quantity: "))

cost_per_unit = 100
total_cost = quantity * cost_per_unit

if total_cost > 1000:
    total_cost = total_cost - (total_cost * 0.10)   # 10% discount

print("Total Cost is:", total_cost)

# Q No 12
# A school has following rules for grading system:
# School Grading System

marks = int(input("Enter your marks: "))

if marks < 25:
    grade = "F"
elif marks >= 25 and marks < 45:
    grade = "E"
elif marks >= 45 and marks < 50:
    grade = "D"
elif marks >= 50 and marks < 60:
    grade = "C"
elif marks >= 60 and marks <= 80:
    grade = "B"
else:
    grade = "A"

print("Your Grade is:", grade)





