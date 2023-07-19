# Find the sum of the Digits of a Number in Python
'''
Given an input the objective to find the Sum of Digits of a Number in Python. To do so we will first extract the last element of the number and then keep shortening the number itself.
'''

number = int(input("Enter the Number : "))
sum = 0
while(number != 0):
    Unit_Place = number%10
    number = number//10
    sum += Unit_Place

print("Sum of Digits of the Given Number is ",sum)