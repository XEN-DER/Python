
try:
    print(1/0)
    print(int("Hello"))
except ZeroDivisionError:
    print("we cannot divide by zero, try another number")
except ValueError:
    print("cannot convert the string to an integer")
print("rest of the program")

# why do we even use exception handeling?
'''Error Management
   Code Clarity
   Specificity
   Resource Management
   Easier Debugging
   Control Flow
   User Experience
   Maintainability
   Scalability'''
   
#Else Block

try:
    result = 10/2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result is:", result)
    
#Finally Block
try:
    result = 10/2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result is:", result)
finally:
    print("This block always executes, regardless of exceptions")
    
#Raising Exceptions
age=int(input("Enter your age: "))
if age < 18:
    raise ValueError("Age must be at least 18")
else:
    print("You are eligible to vote")
    
