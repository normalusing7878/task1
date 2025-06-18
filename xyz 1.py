
n1=input('Enter the first number: ')
n2=input('Enter the second number: ')

n1=int(n1)
n2=int(n2)

add=n1+n2
subtraction=n1-n2
multiplication=n1*n2
division=n1/n2
print('addition: ',add)
print('subtraction: ',subtraction)
print('multiplication: ',multiplication)
print('division: ',division)


first_name=input('Enter your first name: ')
last_name=input('Enter your second name: ')

full_name= first_name + " "+last_name

print(f"hellow, {full_name} welcome to python program")



n1=input('Enter the first number: ')
n2=input('Enter the second number: ')

n1=int(n1)
n2=int(n2)

add=n1+n2
subtraction=n1-n2
multiplication=n1*n2
division=n1/n2
print('addition: ',add)
print('subtraction: ',subtraction)
print('multiplication: ',multiplication)
print('division: ',division)


number=int(input('Enter a numer: '))
if number % 2 == 0:
    print(f"({number} is an even number. ")
else:
    print(f"{number} is an odd numeber. ")



total_sum = 0
for i in range(1, 51):
    total_sum += i

# Step 3: Display the final sum
print(f"The sum of numbers from 1 to 50 is: {total_sum}")

#task-1
def factorial(n):
    if n == 1:
        return 1
    else:return n*factorial(n-1)
num=int(input('Enter a number: '))
result=factorial(num)
print(f'The factorial of {num} is {result}')

# Task 2: Using Math Module

import math

num = float(input("Enter a number: "))

square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

print(f"Square root of {num} is: {square_root}")
print(f"Natural log (base e) of {num} is: {natural_log}")
print(f"Sine of {num} radians is: {sine_value}")