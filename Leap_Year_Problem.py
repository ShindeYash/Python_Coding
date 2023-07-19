#  Check if a Year is a Leap Year or Not in Python

year = int(input("Enter the year : "))
'''
if year%4==0 and year%100!=0:
    print("This is a Leap Year")
elif year%400==0:
    print("This is a Leap Year")
else:
    print("This is not a Leap Year")
'''

# Optimized code above

if (year%400==0) or (year%4==0 and year%100!=0):
    print("This is Leap Year")
else:
    print("This is not a Leap Year")