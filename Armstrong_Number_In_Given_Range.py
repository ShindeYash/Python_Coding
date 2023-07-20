# Find the Armstrong Numbers between Two Intervals using Python

lower, higher = 150, 500000
Armstrong_Numbers = []

for number in range(lower, higher+1):
    Armstrong_Value = 0
    temp = number

    while(number != 0):
        remainder = number%10
        Armstrong_Value += (remainder**len(str(temp)))
        number = number//10

    if Armstrong_Value == temp:
        Armstrong_Numbers.append(Armstrong_Value)

print("Armstrong Values in the given range are : %d", Armstrong_Numbers)
print(Armstrong_Numbers[::])

   