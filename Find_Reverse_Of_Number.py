# Python Program to find the Reverse of a given number​
'''
Find the Reverse of a Number in Python
Given an integer input the objective is to reverse the given integer number using loops and slicing. Therefore, we will write a program to Find the Reverse of a Number in Python Language.
'''


# String Reverse Method
'''
number = input("Enter the Number: ")
print(number[::-1])
'''

# Number Modulus Method
number = int(input("Enter the Number: "))
reverse_number = 0

while(number != 0):
    Unit_Place = number%10
    number = number//10
    reverse_number = (reverse_number*10) + Unit_Place

print(reverse_number)
