# Check Whether a Given Number is an Armstrong Number or Not in Python
# Armstrong Number is nay number which follows the following rule 
# abcd... = a^n + b^n +c^n +d^n + .......
# Where, n is the order(i.e. The lenght of teh number/ number of digits in the number.)

number = int(input("Enter the Number"))
Armstrong_Value = 0
temp = number

while(number != 0):
    remainder = number%10
    Armstrong_Value += (remainder**len(str(temp)))
    number = number//10

if Armstrong_Value == temp:
    print("This number is a armstrong Number")
else:
    print("This number is not armstrong number.")