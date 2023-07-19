# Find the Prime Numbers in a Given Range in Python
'''
Given two integer as Limits, low and high, the objective is to write a code to in Python Find Prime Numbers in a Given Range in Python Language. To do so we will use nested loops to check for the Prime while Iterating through the range.
'''

low, high = 2, 10
prime_Numbers = []
for i in range(low, high):
    flag = 0
    for j in range(2,i):
        if i%j == 0:
            flag += 1
            break
    if flag == 0:
        prime_Numbers.append(i)

print(prime_Numbers)
print(len(prime_Numbers))
    
