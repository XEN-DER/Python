import numpy as np

# 3D array creation
a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # shape = (2, 2, 2)
print("3D Array:\n", a)
print("Dimensions:", a.ndim)
print("Shape:", a.shape)
print("Data Type:", a.dtype)

# Zeros array
b = np.zeros((3, 5))
print("\nZeros Array (3x5):\n", b)

# Ones array
c = np.ones((1, 5))
print("\nOnes Array (1x5):\n", c)

# Identity matrix
d = np.eye(5)
print("\nIdentity Matrix (5x5):\n", d)

# Arange
e = np.arange(7, 77, 7)
print("\nArange from 7 to 77 with step 7:\n", e)

# Linspace
f = np.linspace(0, 10, 5)
print("\nLinspace from 0 to 10 (5 points):\n", f)

# 2D array operations
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr)
print("Element at [1,2]:", arr[1, 2])
print("First row:", arr[0, :])
print("Shape:", arr.shape)
print("Reshaped (3x2):\n", arr.reshape(3, 2))
print("Flattened:\n", arr.flatten())

# Element-wise operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("\nAddition:", a + b)
print("a * 3:", a * 3)

# Broadcasting example
c = np.array([[1], [2], [3]])  # shape (3,1)
d = np.array([10, 20, 30])     # shape (3,)
print("Broadcasted Addition:\n", c + d)

# Statistical operations
arr = np.array([[1, 2], [3, 4]])
print("\nSum:", arr.sum())
print("Mean:", arr.mean())
print("Max (axis=0):", arr.max(axis=0))  # column-wise
print("Max (axis=1):", arr.max(axis=1))  # row-wise
print("Median:", np.median(arr))

# Boolean Masking
a = np.array([1, 2, 3, 4, 5])
mask = a > 3
print("\nValues > 3:", a[mask])
