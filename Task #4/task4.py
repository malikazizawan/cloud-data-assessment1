# Q No 01
# 1. Write a program that accepts a list from user and print the alternate element of list. 


numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Alternate elements are:", numbers[::2])


# Q No 02
#  Write a program that accepts a list from user. Your program should reverse the content of list and 
# display it. Do not use reverse() method.  

number = list(map(int, input("Enter numbers separated by space:").split()))
reversed_list = number[::-1]
print("Reversed list:", reversed_list)

# Q No 03
#  Find and display the largest number of a list without using built-in function max(). Your program 
# should ask the user to input values in list from keyboard.  

numbers = list(map(int, input("Enter number separated by space: ").split()))
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)

# Q no 04
#  Write a program that rotates the element of a list so that the element at the first index moves to the 
# second index, the element in the second index moves to the third index, etc., and the element in the last 
# index moves to the first index.  

numbers = list(map(int, input("Enter numbers separated by space:").split()))

last = numbers[-1]

rotated_list = [last] + numbers[:-1]

print("Rotated List:", rotated_list)


# Q No 05
# Write a program that input a string and ask user to delete a given word from a string.  

text = input("Enter a string: ")

word = input("Enter the word to delete : ")

new_text = text.replace(word, "")

print("Updated string:", new_text)

# Q No 09
# . Write a program to add two matrices of size n x m.
# Program to add two matrices of size n x m

# Step 1: Take matrix size input
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

# Step 2: Input first matrix
print("Enter elements of first matrix row by row:")
matrix1 = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Step 3: Input second matrix
print("Enter elements of second matrix row by row:")
matrix2 = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix2.append(row)

# Step 4: Add the two matrices
result = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

# Step 5: Print result matrix
print("\nResultant Matrix after Addition:")
for row in result:
    print(row)


# Q no 10
# Multiply two matrices

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

# Result matrix size = rows(A) x cols(B)  => 2 x 2
result = [[0, 0],
          [0, 0]]

for i in range(len(A)):        # rows of A
    for j in range(len(B[0])): # cols of B
        for k in range(len(B)): # rows of B
            result[i][j] += A[i][k] * B[k][j]

# Print
for row in result:
    print(row)

