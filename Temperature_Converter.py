# Write a Python program that converts temperature in Celsius to Fahrenheit and vice versa. Implement the requirements using functions.
# Hint: 0C= (0F-32)*(5/9)

print("--------------------Welcome to Temperature Converter-----------------")

'''
if required_temp == '1':
     Celcius = int(input("Enter the Temperature In degree Celcius: "))
     def Celsius_To_Fahrenheit(Celsius):
          Fahrenheit = (Celsius*(9/5)) + 32
          return Fahrenheit
else:
     Fahrenheit = int(input("Enter the Temperature In degree Fahrenheit: "))

     def Fahrenheit_To_Celsius(Fahrenheit):
          Celcius = (Fahrenheit - 32)*(5/9)
          return Celcius
'''

def temperture_converter(choice, temperature):
     if choice == '1':
          Fahrenheit = (temperature*(9/5)) + 32
          return Fahrenheit
     else:
          Celcius = (temperature - 32)*(5/9)
          return Celcius

required_choice = input("Please Enter 1 If you want to convert from Celcius to Fahranite \n Please Enter 2 if you want to convert form Fahranite to Celcius \n Input Your Choice: ")
temperature = int(input("Please Enter the temperature :"))
Converted_Temp = temperture_converter(required_choice, temperature)
print("Your Converted Temperature is ",Converted_Temp)
