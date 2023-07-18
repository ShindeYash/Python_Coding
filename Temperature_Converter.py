# Write a Python program that converts temperature in Celsius to Fahrenheit and vice versa. Implement the requirements using functions.
# Hint: 0C= (0F-32)*(5/9)

print("--------------------Welcome to Temperature Converter-----------------")

def Celsius_To_Fahrenheit(Celsius):
     Fahrenheit = (Celsius*(9/5)) + 32
     return Fahrenheit
     
Fahrenheit = Celsius_To_Fahrenheit(78)
print(Fahrenheit)