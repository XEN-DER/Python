import pandas as pd
import numpy as np

'''# Creating Series
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
print(s[s>10])'''

# Create Series with a NaN and a string
s = pd.Series([10, "Nope", 30, np.nan])

# Check for null and non-null values
print("Is Null:\n", s.isnull())
print("\nIs Not Null:\n", s.notnull())

# Fill NaN with 0 (returns a new Series)
s_filled = s.fillna(0)
print("\nAfter fillna:\n", s_filled)

# Drop NaN values (returns a new Series)
s_dropped = s.dropna()
print("\nAfter dropna:\n", s_dropped)

s=pd.Series([10,20,30,40,50])
print(s.sum())
print(s.mean())
print(s.min(),s.max())
print(s.std())
print(s.describe())

s=pd.Series([30,10,40,20],index=['d','b','a','c'])
print(s.sort_values())
print(s.sort_index())
print(s.rank())

names=pd.Series(["Alice","bob","charlie","dave"])
print(names.str.upper())
print(names.str.lower())
print(names.str.capitalize())
print(names.str.contains("a"))

s1=pd.Series([10,20,30],index=['a','b','c'])
s2=pd.Series([5,10,15], index=['b''c','d'])
print(s1+s2)
