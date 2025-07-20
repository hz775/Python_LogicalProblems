import numpy as np

arr=np.array([1,2,3,4])
print(arr.dtype)

arr=np.array([1,2,3,4.4,5])
print(arr.dtype)

arr=np.array(['string','2','3','4','5'])
print(arr.dtype)

arr=np.array([1,2,3,4],dtype=np.int32)
print(arr.dtype)

arr=np.array([1,2,3,4.4,5],dtype=np.float32)
print(arr.dtype)

arr=np.array([1.2,2.1,3.4,4.4,5.1],dtype=np.int64)
print(arr.dtype)
print(arr)


# type casting is done using -astype()

arr=np.array([1,2,3,4])
new_arr=arr.astype(np.float64)
print(new_arr)

arr=np.array([1.2,2.1,3.4,4.5])
new_arr=arr.astype(np.int64)
print(new_arr)

arr = np.array([10, 20, 30])
str_arr = arr.astype(str)
print(str_arr)

arr=np.array([10,1,0,1,0],dtype=bool)
print(arr)


arr=np.array([[1,2,3],
              [5,6,7]])
print(arr.shape)
print(arr.size)
print(arr.ndim)
print(arr.itemsize)


# reshape(ravel,flatten,resize)

arr=np.array([1,2,3,4,5,6])
reshape=arr.reshape(2,3)
print(reshape)

reshape1=reshape.reshape(3,2)
print(reshape1)


arr = np.arange(12)             #2 blocks 2 rows 3 col
reshaped = arr.reshape((2, 2, 3))
print(reshaped)

ravel=reshape1.ravel()          #[1 2 3 4 5 6]
print(ravel)

ravel[0]=100                    
print(ravel)                    #[100   2   3   4   5   6]
print(reshape1)                 #[[100   2][3,4][5,6]]

flat=reshape1.flatten()         #[100   2   3   4   5   6]
print(flat)

flat[0]=1                       #[1 2 3 4 5 6]
print(flat)

print(reshape1)                #[[100   2][3,4][5,6]]


arr = np.array([1, 2, 3])
resized = np.resize(arr, (2, 4))

print(resized)

arr = np.array([10, 20, 30, 40, 50])
resized = np.resize(arr, (2, 2))

print(resized)

arr = np.array([1, 2, 3])
arr.resize((2, 3))  
print(arr)





