'''a=int(input("Enter the number A= "))
b=int(input("Enter the number B= "))
print("The addition is ",(a+b))
print("The subtraction is ",(a-b))
print(f"The multiplication is {(a*b)}")
print(f"The division is ",(a/b))
print(f"The floor division is ",(a//b))
print(f"The modulus is ",(a%b))
print(f"The exponentiation is ",(a**b))'''


#checking if the email give is correct or not
email= input(" Enter your email: ")
if "@" in email and email.endswith(".com"):
    print("The email is correct")
else:
    print("The email is incorrect")