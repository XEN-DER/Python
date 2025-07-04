'''
NumPy (Numerical Python) is a powerful Python library used for numerical computations. 
It provides support for multi-dimensional arrays and matrices, 
along with a large collection of high-level mathematical functions to operate on these arrays efficiently.
'''
import numpy as np

a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) #create numpy array
print(a)
print(a.ndim) #ndim -> number of dimension
print(a.shape) #shape -> rows*columns
print(a.dtype)
b=np.zeros((3,5))# -> creates an array of zeros with the give dimension
print (b)
c=np.ones((1,5))# -> creates an array of ones with given demension
print(c)
d=np.eye(5) #create identity matrix
print(d)
e=np.arange(7,77,7)#arange->(start,stop,step)
print(e)
f=np.linspace(0,10,5)#linespace ->(start,stop,CountOfSplit)
print(f)

arr=np.array([[1,2,3],[4,5,6]])
#              0 1 2   0 1 2
print(arr)
print(arr[1,2])#indexing
print(arr[0,:])#slicing
print(arr.shape)
print(arr)
print(arr.reshape(3,2))#rehape the array
print(arr.flatten())#flattens to one dimension'''
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a*3)
c=np.array([[1],[2],[3]])#3*1
d=np.array([10,20,30])#1*3
print(c+d)

arr=np.array([[1,2],[3,4]])
print(arr.sum())
print(arr.mean())
print(arr.max(axis=0))
print(arr.max(axis=1))
print(np.median(arr))