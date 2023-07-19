# Check Whether a Number is a Prime or Not in Python

number = int(input("Please Enter a Number: "))
flag = 0

'''
for i in range(1,number):
    if number%i==0:
        flag += 1
if flag == 1:
    print("This is a Prime Number")
elif flag == 0:
    print("This number is 0")
else:
    print("This is not a Prime Number.")
'''

# More Optimized Code 
for i in range(2,number):
    if number%i == 0:
        flag += 1
        break
if flag == 1:
    print("This is Not Prime Number.")
else:
    print("This is a Prime Number")


