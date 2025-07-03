'''Dictionary class for storing and retrieving key-value pairs
dictionary -> { key : value, key2: value2, ... }
key - unique identifier for the value
They are unordered, changeable, and do not allow duplicate keys.
Fast lookups using keys
Mutable, meaning you can add, remove, or change items after creation.
Dictionaries are defined using curly braces {} with key-value pairs separated by colons.
Dictionaries are unordered collections, meaning the order of items is not guaranteed.
#python dictionary -> '' or ""
#json -> ""
'''

A={'name': 'John', 'age': 30, 'city': 'New York'}
print(A)  # This will print the dictionary A
print(type(A))  # This will print the type of variable A, which is a dictionary

print(A['name'])  # This will print the value associated with the key 'name' in the dictionary A
print(A['age'])  # This will print the value associated with the key 'age'
A["name"]="Ritvik"
A['city']="Benganpur"# This will change the value associated with the key 'name' to 'Ritvik'
print(A)  # This will print the dictionary A after changing the value of 'name'

#dictionary inside a dictionary
B = {
    'name': 'Alice',
    'age': 25,
    'address': {
        'street': '123 Main St',
        'city': 'Los Angeles',
        'state': 'CA'
    }
}

print(B)  # This will print the dictionary B
print(B['address']) # This will print the value associated with the key 'address', which is another dictionary
print(B['address']['city'])  # This will print the value associated with the key 'city' inside the 'address' dictionary
print(B['address']['state'])  # This will print the value associated with the key 'state' inside the 'address' dictionary

A.update(B) # This will update the dictionary A with the contents of dictionary B
print(A)  # This will print the dictionary A after updating it with the contents of dictionary B

for i in A.keys():
    print(i)  # This will print all the keys in the dictionary A

for i in A.values():
    print(i)  # This will print all the values in the dictionary A

for key, value in A.items():
    print("key = "+key)  # This will print each key-value pair in the dictionary A
    print("value = "+str(value))  # This will print each value in the dictionary A
    
#multi line strings
A='''This is a multi-line string.
It can span multiple lines and preserve line breaks.
You can use it to write longer text without worrying about line breaks.'''

print(A)  # This will print the multi-line string A
print(type(A))  # This will print the type of variable A, which is a string

B="ABCDEFGHIJKLMNOPQRSTVUWXYZ"
print(B)  # This will print the string B
print(B[0])
print(B[-1])  # This will print the third character of the string B
print(B[0:5])  # This will print the first five characters of the string
print(B[5:10])  # This will print characters from index 5 to 9 of the string B
print(B[9:])  # This will print characters from index 10 to 14 of the string B
print(B[:5])  # This will print the first five characters of the string B
print(B[15:20])  # This will print every second character of the string B