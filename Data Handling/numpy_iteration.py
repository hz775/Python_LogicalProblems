import numpy as np

arr=np.array([1,2,3,4,5])
for i in arr:
    print(i)


arr=np.array([[1,2,3],[4,5,6]])
for i in arr:
    print("Row: ",i)

for flat in arr.flat:
    print(flat)

print("Using inbuilt func")
for x in np.nditer(arr):
    print(x)

print("Using index and value")
for idx,value in np.ndenumerate(arr):
    print(f"idx:{idx},value:{value}")


