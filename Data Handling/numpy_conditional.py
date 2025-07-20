import numpy as np

arr=np.array([1,2,3,4,5])
print(np.where(arr<3,"low","high"))

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.argwhere(arr>5))

arr=np.array([10,24,55,60,30])
mask=np.logical_and(arr>20,arr<60)
print(mask)

arr=np.array([10,24,55,60,30])
mask=np.logical_and(arr>20,arr<60)
print(arr[mask])


# broadcasting
image=np.array([[100,50],[20,30]])
brightness=image+50
print(brightness)

a=np.array([[1,2,3],[5,6,7]])
b=np.array([10,20,30])
print(a+b)

# vecorization

def square(x):
    return x*x

res=np.vectorize(square)
arr=[1,2,3,4,5]
print(res(arr))


arr = np.array([1, 2, np.nan, 4, 5])
print(arr)
print(np.isnan(arr))

# removing missing value
cleaned = arr[~np.isnan(arr)]
print(cleaned)

arr_filled = np.nan_to_num(arr, nan=0)
print(arr_filled)


