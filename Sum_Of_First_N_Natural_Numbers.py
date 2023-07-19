# Problem Statement
# Sum of First N Natural Numbers

# Method 1:- Loop

num = int(input("Please Enter the value of N: "))
'''
sum = 0
for i in range(1,num+1):
    sum += i
print("Sum of the first %d Naturel numbers is %d."%(num, sum))
'''

# Method 2:- Formula

sum = num*(num+1)/2
print("Sum of the first %d Naturel numbers is %d."%(num, sum))
