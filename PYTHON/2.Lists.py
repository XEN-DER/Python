[1,"a,b,c",3.14,True] # This is a list containing different data types

#List
#Supports didferent data types
my_list = [1, "a,b,c", 3.14, True]
#ordered -> accesses them via index (0,1,2,...)
#mutable -> can change the values in the list
#allow duplicate values [0,1,2,3,1,2,3,0,4,5,6,7,8,9,10]
print(my_list)  # This will print the entire list
print(my_list[0])  # This will print the first element of the list



a=10
b="string"
c=True
d=3.14

print(type(a))  # This will print the type of variable a
print(type(b))  # This will print the type of variable b
print(type(c))  # This will print the type of variable c
print(type(d))  # This will print the type of variable d

#Symbol of Lists is []
#Symbol of Sets is {}
#Symbol of Tuples is ()

A=[1,2,3,"abc",True,3.14]  # This is a list containing different data types
print(type(A))  # This will print the type of variable A
print(A)  # This will print the entire list A
print(A[0])  # This will print the first element of the list A
print(A[1])  # This will print the second element of the list A
print(A[2])  # This will print the third element of the list A
print(A[3])  # This will print the fourth element of the list A
print(A[4])  # This will print the fifth element of the list A
A[2]="two"
print(A)  # This will print the entire list A after modifying the third element
print(A[-1])# This will print the last element of the list A
print(A[-2])# This will print the second last element of the list A

A.append(100)  # This will append a new element to the end of the list A
print(A)  # This will print the entire list A after appending a new element

print(A.index(100))  # This will print the index of the element 100 in the list A
#if we print something which is not present in the list it will show an error
#NAME of the element -- is not present in the list
f=[5,6,7,8,9]
A.extend(f)
print(A)  # This will print the entire list A after extending it with another list

A.remove(100)  # This will remove the element 100 from the list A
print(A)  # This will print the entire list A after removing the element 100

A.pop()  # This will remove the last element from the list A
print(A)  # This will print the entire list A after popping the last element

A.pop(1)  # This will remove the second element from the list A
print(A)  # This will print the entire list A after popping the second element

A.clear()  # This will clear the entire list A
print(A)  # This will print the entire list A after clearing it
A=[1,2,3,"abc",True,3.14]
print(A[2:5])  # This will print the elements from index 2 to 4 (5 is not included) of the list A
print(A[2:])  # This will print the elements from index 2 to the end of the list A
print(A[:5])  # This will print the elements from the start of the list A to index 4 (5 is not included)

print(A[4:])
A.reverse()  # This will reverse the entire list A
print(A)  # This will print the entire list A after reversing it

f.sort()  # This will sort the list A in ascending order
print(f)  # This will print the entire list A after sorting it
#'<' not supported between instances of 'str' and 'bool'

e=[1,2,3,4,5,6,7,8,9,10]
f=e.copy()  # This will create a copy of the list e and assign it to f
f.pop()
print(f)  # This will print the entire list f after popping the last element
print(e)  # This will print the entire list e to show that it remains unchanged

A.insert(1,5)  # This will insert the element 5 at index 1 in the list 
print(A)  # This will print the entire list A after inserting the element 5 at index 1