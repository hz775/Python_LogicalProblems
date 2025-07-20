import numpy as np

a=np.array([1,3,5])
b=np.array([2,4,6])

print(a+b)
print(a-b)
print(a/b)
print(b//a)         #int value
print(a*b)
print(b%a)
print(a**2)

arr=np.array([1,2,3])
pow=np.power(arr,2)
print(pow)

arr=np.array([1,2,3])
sqrt=np.sqrt(arr)
print(sqrt)

arr=np.array([1,100,10])
log=np.log10(arr)
print(log)

arr=np.array([1,2,3])
exp=np.exp(arr)
print(exp)

arr=np.array([1.3,2.5,3])
floor=np.floor(arr)
print(floor)


arr=np.array([1.3,2.5,3])
round=np.round(arr)
print(round)

arr=np.array([0,30,90])
sin=np.sin(arr)
print(sin)


arr=np.array([10,20,30,40,50])
index=arr[::-1]
print(index)

arr=np.array([10,20,30,40,50])
print(arr[::2])


matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix[0:2,:])

matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix[1:,1:])


arr=np.array([10,20,30,40,50])
index=[0,2]
mat=np.take(arr,index)
print(mat)









