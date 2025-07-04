import pandas as pd

# Creating Series
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
s3 = pd.Series({'x': 5, 'y': 10, 'z': 15})

# Display dictionary-based Series
print("s3:\n", s3)

# Properties of s1
print("\ns1.index:", s1.index)
print("s1.values:", s1.values)
print("s1.dtype:", s1.dtype)
print("s1.size:", s1.size)
print("s1.shape:", s1.shape)

# Accessing elements in s2
print("\ns2['b']:", s2['b'])     # Access by label
print("s2[1]:", s2[1])           # Access by position
print("s2[0:2]:\n", s2[0:2])     # Slice

# Modifying values
s2['b'] = 250     # Modify existing index
s2['d'] = 400     # Add new index-value pair

# Dropping an index
s2.drop('a', inplace=True)

# Final s2
print("\nModified s2:\n", s2)

s=pd.Series([1,2,3])
print(s+2)
print(s*10)
print(s**2)

s=pd.Series([5,10,15,20])
print(s[s>10])