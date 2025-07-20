import numpy as np

arr=np.array([1,2,3,4])
print(arr)
print(arr.ndim)          #ndim is a inbuilt func  to calculate the dimension of array [] is 1 and [[]] is 2 
print(arr.shape)         # shape is ntg but saying no of rpows and no of columns 4 elements in the array with 1 row

range1=np.arange(1,10)
range2=np.arange(1,10,2)
range3=np.linspace(0,1,5)
print(range1)
print(range2)
print(range3)

arr=np.zeros((2,2),dtype=int)
arr1=np.ones((5,),dtype=int)
print(arr)
print(arr1)

arr=np.array([1,2,3,4,5,6,7,8,9])
reshaped=arr.reshape((3,3))
print(reshaped)

arr=np.array([1,2,3,4,5])
mean=np.mean(arr)
print(mean)

arr=np.array([1,2,3,4,5,6])
print(np.sum(arr))

arr=np.array([1,2,3,4,5,6,7])
print(np.max(arr))
print(np.min(arr))

# np.logspace(start, stop, num=50, base=10.0)

arr=np.logspace(1,3,num=5)
print(arr)

arr=np.full([2,4],7)     #	Initializes all values to a specific value       
arr1=np.full(10,2)
print(arr)
print(arr1)

arr=np.empty([2,2],dtype=int)           #Creates an array with uninitialized garbage values
print(arr)

arr=np.random.rand(2,3)
print(arr)

arr=np.random.randn(0,1)                #float values from 0
print(arr)

arr=np.random.randint(10,100)
print(arr)

arr=np.random.randint(10,100,size=(2,3))
print(arr)