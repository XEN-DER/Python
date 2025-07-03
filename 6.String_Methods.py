A="A B C D E F G H I J K L A B C M N O P Q R S T V U W X Y Z"
B="ABC"

print(A.upper())  # This will convert the string A to uppercase
print(A.lower())  # This will convert the string A to lowercase
print(A.strip()+B)  # This will remove any leading or trailing whitespace from the string A
print(A.replace("A", "X"))  # This will replace all occurrences of 'A' in the string A with 'X'
print(A.replace("ABC","123"))  # This will split the string A into a list of substrings using 'C' as the delimiter


#converting a string to a list
print(list(A))  # This will convert the string A to a list of characters
C=A.split()  # This will split the string A into a list of substrings using whitespace as the delimiter
C=A.split(" ")
print(C)  # This will print the list of substrings obtained from splitting the string A

print(" * ".join(C))  # This will join the elements of the list C into a single string, with ' * ' as the separator

D=A+B
print(D.count("ABC"))  # This will count the number of occurrences of 'A' in the string D
print(D.startswith("A B C"))  # This will check if the string D starts with 'A' and print True or False
print(D.endswith("ABC"))  # This will check if the string D ends with 'Z' and print True or False
print(D*3) # This will repeat the string D three times
print("A" in D)  # This will check if 'A' is present in the string D and print True or False

