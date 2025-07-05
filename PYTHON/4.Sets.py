'''Sets are unordered collections of unique elements. 
They are partially mutable, meaning you can add or remove elements, but they do not allow duplicate values. 
Sets are useful for membership testing and eliminating duplicate entries from a collection.
Sets are defined using curly braces {} or the set() constructor.
Sets are commonly used in scenarios where you need to perform mathematical operations like union, intersection, and difference.
'''

# Example of creating a set
A={1,2,3,4,5,6}
B={1,1,2,2,3,3,3,4,4,4,5,5,5,5,6,6,6,6,7,8,9,10}  # This set will only keep unique values
print(A)  # This will print the set A
print(type(A))  # This will print the type of variable A, which is a set
print(B)
#since there is no index in sets, we cannot access elements by index
# print(A[0])  # This will raise an error because sets do not support indexing

# Adding elements to a set
A.add(7)  # This will add the element 7 to the set A
print(A)  # This will print the set A after adding the element 7

A.remove(7)  # This will remove the element 7 from the set A
print(A)  # This will print the set A after removing the element 7

emset = set()  # This will create an empty set
print(emset)  # This will print the empty set
print(B)
#how are discard and remove different ?
B.discard(10)  # This will remove the element 10 from the set B if it exists, without raising an error if it does not
print(B)  # This will print the set B after discarding the element 10

print(20 in B)  # This will check if the element 20 is in the set B, and print True or False
print(5 in B)  # This will check if the element 5 is in the set B, and print True or False

C={1,2,3,4,5,6,7,8,9,0}

C.update({10,11,12})  # This will add multiple elements to the set C
print(C)  # This will print the set C after updating it with new elements   

C.remove(12)  # This will remove the element 12 from the set C
print(C)  # This will print the set C after removing the element 12

C.pop()  # This will remove and return an arbitrary element from the set C
print(C)  # This will print the set C after popping an element

D=C.copy()  # This will create a shallow copy of the set C
print(D)  # This will print the set C after copying it

D.remove(11)  # This will remove the element 11 from the set D
print(D)  # This will print the set D after removing the element 11

C.clear()  # This will remove all elements from the set C
print(C)  # This will print the empty set C after clearing it

E={1,2,3}
F={3,4,5}

# Union of two sets
print(E.union(F))  # This will print the union of sets E and F, which combines all unique elements from both sets

# Intersection of two sets
print(E.intersection(F))  # This will print the intersection of sets E and F, which includes only elements present in both sets

#difference of two sets
print(E.difference(F))  # This will print the difference of sets E and F, which includes elements in E that are not in F
print(E-F)  # This is another way to compute the difference of sets E and F, which includes elements in E that are not in F
print(F.difference(E))  # This will print the difference of sets F and E, which includes elements in F that are not in E
print(F-E)  # This is another way to compute the difference of sets F and E, which includes elements in F that are not in E

# Symmetric difference of two sets
print(E.symmetric_difference(F))  # This will print the symmetric difference of sets E and F, which includes elements that are in either set but not in both
print(E^F)  # This is another way to compute the symmetric difference of sets E and F, which includes elements that are in either set but not in both

#Frozen sets
# A frozenset is an immutable version of a set, meaning once created, its elements cannot be changed.
# It is useful when you need a set that should not be modified, such as when using it as a key in a dictionary or storing it in another set.
G=frozenset([1,2,3,4,5,6])  # This will create a frozenset with the specified elements
print(G)  # This will print the frozenset G

# Attempting to add or remove elements from a frozenset will raise an error
G.add(7)  # This will raise an error because frozensets are immutable
G.remove(1)  # This will also raise an error because frozensets are immutable
print(G)  # This will print the frozenset G after attempting to modify it, but it will not change
# Attempting to pop an element from a frozenset will also raise an error