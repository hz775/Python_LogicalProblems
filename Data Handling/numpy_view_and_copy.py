import numpy as np

# view and copies

a=np.array([1,2,3,4,5])
b=a.view()

b[0]=100

print("Original: ",a)
print("New: ",b)

b = a.view()
print(b.base is a)


a=np.array([1,2,3,4,5])
b=a.copy()

b[0]=100

print("Original: ",a)
print("New: ",b)

c = a.copy()
print(c.base is a)

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.transpose())

a=np.array([1,2,3])
b=np.array([4,5,6])
combine=np.concatenate((a,b))
print(combine)


arr1=np.array([[1,2],[3,4]])
arr2=np.array([[4,5],[7,8]])
print(np.vstack((arr1,arr2)))


arr1=np.array([[1,2],[3,4]])
arr2=np.array([[4,5],[7,8]])
print(np.hstack((arr1,arr2)))


arr1=np.array([[1,2],[3,4]])
arr2=np.array([[4,5],[7,8]])
print(np.stack((arr1,arr2),axis=0))

arr1=np.array([[1,2],[3,4]])
arr2=np.array([[4,5],[7,8]])
print(np.stack((arr1,arr2),axis=1))


arr=np.array([1,2,3,4])
split=np.split(arr,2)
print(split)

arr=np.array([1,2,3,4])
split=np.hsplit(arr,2)
print(split)

arr=np.array([1,2,3,4])
rep=np.repeat(arr,2)
print(rep)

arr=np.array([1,2,3,4])
rep=np.tile(arr,2)
print(rep)


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.sum(arr,axis=1))

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.sum(arr,axis=0))

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.sum(arr,axis=(0,1)))

arr=np.array([10,2,3])
print(np.cumsum(arr))
print(np.cumprod(arr))




