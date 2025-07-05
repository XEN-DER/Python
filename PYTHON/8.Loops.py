for i in range(1, 11):
    print(i)  # This will print numbers from 1 to 10
    
for i in range(7,76):
    print(i)  # This will print numbers from 7 to 75

for i in range(6, 66):
    print(i)  # This will print numbers from 6 to 65
for i in range(3,151):
    print(i)  # This will print numbers from 3 to 150
    
#while loop

while True:
    x=int(input("Enter a number to print : "))
    if x==0:
        break  # This will break the loop if the user enters 0
    print(x)  # This will print the number entered by the user
    print("Enter 0 to break the loop")  # This will print a message to the user to enter 0 to break the loop  
    
    for i in range(1, 100):
        if (i%2!=0):
            continue  # This will skip the iteration when i is 4
        print(i)
        
for i in range(1, 100):
    if (i % 2 == 0):
       pass # This will do nothing for even numbers
    print(i)  # This will print even numbers from 1 to 99

#Modules
import math
print(math.sqrt(16))  # This will print the square root of 16
print(math.floor(4.7))  # This will print the floor value of 4.7
print(math.ceil(4.3))  # This will print the ceiling value of 4.3
print(math.pi)  # This will print the value of pi
print(math.e)  # This will print the value of e (Euler's number)
print(math.pow(2, 3))  # This will print 2 raised to the power of 3
print(math.factorial(5))  # This will print the factorial of 5

import random
print(random.randint(1, 10))  # This will print a random integer between 1 and 10
print(random.randrange(1, 11))  # This will print a random number between 1 and 10

import Calculator

print(Calculator.add(5, 6))  # This will print the result of the addition function from the Calculator module
print(Calculator.subtract(10, 5))  # This will print the result of the subtraction function from the Calculator module
print(Calculator.multiply(10, 5))  # This will print the result of the multiplication function from the Calculator module
print(Calculator.divide(10, 5))  # This will print the result of the division function from the Calculator module0.

