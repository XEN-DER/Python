'''A TUPLE IS A COLLECTION OF ITEMS THAT IS ORDERED AND UNCHANGEABLE.
 TUPLES ALLOW DUPLICATE VALUES.
 A TUPLE IS DEFINED BY A LIST OF VALUES SEPARATED BY COMMAS AND ENCLOSED IN PARENT
 TUPLES ARE USED TO STORE MULTIPLE ITEMS IN A SINGLE VARIABLE.
 TUPLES ARE SIMILAR TO LISTS, BUT THEY ARE IMMUTABLE, MEANING ONCE A TUPLE IS CREATED, YOU CANNOT CHANGE ITS CONTENTS.
 TUPLES CAN CONTAIN ANY TYPE OF DATA, INCLUDING STRINGS, INTEGERS, FLOATS, AND EVEN OTHER TUPLES.
 TUPLES ARE OFTEN USED TO GROUP RELATED DATA TOGETHER, SUCH AS COORDINATES, RGB COLORS, OR DATABASE RECORDS.
 TUPLES CAN BE USED AS KEYS IN DICTIONARIES, WHILE LISTS CANNOT BE USED AS KEYS DUE TO THEIR MUTABILITY.
 TUPLES ARE MORE MEMORY-EFFICIENT THAN LISTS, MAKING THEM A PREFERRED CHOICE FOR STORING FIXED DATA.
 SYMBOL OF TUPLES IS ().'''
 
A=(1,2,3,4,5,6)
print(A)
print(type(A))  # This will print the type of variable A, which is a tuple
print(A[0])  # This will print the first element of the tuple A
print(A[1])  # This will print the second element of the tuple A
  # This will raise an error because tuples are immutable and cannot be changed
print(A)  # This will print the entire tuple A after attempting to modify the second element
#'tuple' object does not support item assignment

a=(1,2,3,4,5)
b=(6,7,8,9,10)

print(a+b)  # This will concatenate the two tuples a and b
print(a*2)  # This will repeat the tuple a two times
print(len(a))  # This will print the length of the tuple a
print(b.count(2))  # This will count the number of occurrences of the element 2 in the tuple b
print(b.index(7))  # This will print the index of the element 7 in the tuple b

c=(1,2,3,4,5,5,6,7,7,7,7,7,8,8,8)
#i have soo many duplicate values in this tuple
print(c.count(7))  # This will count the number of occurrences of the element 7 in the tuple c
print(c.index(8))  # This will print the index of the first occurrence of the element 8 in the tuple c

#why use tuples instead of lists???
# Tuples are used instead of lists when you want to ensure that the data remains constant and cannot be modified.
# They are also used when you want to use the data as keys in dictionaries, as tuples are immutable and can be hashed, while lists cannot.