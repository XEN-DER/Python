print("hello world")


#Function calling
def Ritvik():
    print("I am learning python")  # line 3 and 4 are function definition
    
Ritvik() # calling the function so that it executes the code inside the function

def Ritvik(a):
    print("I am "+a)  # line 3 and 4 are function definition
    
Ritvik("Ritvik_Vedangi") # calling the function so that it executes the code inside the function

def add (a,b):
    print(a+b)

add(5,6)

def subtract (a,b):
    print(a-b)

subtract(10,5)

def multiply (a,b):
    print(a*b)
    
multiply(10,5)

def divide (a,b):
    print(a/b)
    
divide(10,5)
#this is the returning function
def addition(a,b,c):
    return(a+b+c)

print(addition(1,2,3))  # This will print the result of the addition function

def subtraction(a,b,c):
    return(a-b-c)
print(subtraction(10,5,3))  # This will print the result of the subtraction

def multiplication(a,b,c):
    return(a*b*c)
print(multiplication(2,3,4))  # This will print the result of the multiplication

def division(a,b,c):
    return(a/b/c)   
print(division(100,5,2))  # This will print the result of the division

#why are we using this returning function?
def add(a,b):
    return a+b

print(add(5,6)+add(10,20))  # This will print the sum of two addition function calls

name= "Ritvik Vedangi" # name is a global variable hear cause it is outside the funcyion
def greet(name):
    return "Hello, " + name
print(greet(name))  # This will print the greeting message with the name


x = "5"
y = 3
print(x * y)
