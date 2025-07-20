import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])
swapped = np.swapaxes(arr, 0, 1)
print(swapped)

arr=np.arange(2,11).reshape(3,3)
print(arr)


arr=np.zeros(10)
arr[6]=11
print(arr)

arr=np.array([12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37])
print(arr[::-1])

arr=np.ones((5,5))
arr[1:-1,1:-1]=0
print(arr)


ones=np.ones((3,3))
arr=np.zeros((5,5))
arr[1:-1,1:-1]=ones
print(arr)


checkerboard = np.zeros((8, 8), dtype=int)
checkerboard[1::2, ::2] = 1  
checkerboard[::2, 1::2] = 1  
print(checkerboard)

lis=np.array([1,2,3,4,5,6,7,8])
print(np.reshape(lis,(2,4)))

tupl=np.array(((8, 4, 6), (1, 2, 3)))
print(tupl)

arr = np.array([10, 20, 30])
append=[40, 50, 60, 70, 80, 90]
res=np.append(arr,append)
print(res)

arr=np.array([1 + 0j, 0.70710678 + 0.70710678j])
print(np.real(arr))
print(np.imag(arr))

arr = np.array([1, 2, 3], dtype=np.int64)
print(arr.size)
print(arr.shape)
print(arr.nbytes)
print(arr.ndim)


arr1=np.array([10,20,30,0,40])
arr2=np.array([10,90,40])
print(np.intersect1d(arr1,arr2))


array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40, 50, 70, 90])
print(np.setdiff1d(array1,array2))

array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40, 50, 70])
print(np.setxor1d(array1,array2))


a=np.array([1,2])
b=np.array([4,5])
mask1=np.where(a>b,"True","False")
mask2=np.where(a >= b,"True","False")
mask3=np.where(a < b,"True","False")
mask4=np.where(a <= b,"True","False")
print(mask1)
print(mask2)
print(mask3)
print(mask4)


arr=np.array([[10,20,30],[20,40,50]])
print(arr.flatten())

arr=np.array([[ 2,4,6],[6,8,10]],dtype=np.int32)
print(arr)

# np.eye(N, M=None, k=0, dtype=float)

arr=np.eye(3)
print(arr)

arr=np.zeros((4,3))
arr[1, 0] = 1
arr[2, 0] = 1
arr[2, 1] = 1
arr[3, 0] = 1
arr[3, 1] = 1
arr[3, 2] = 1
print(arr)

arr1 = np.array([[0, 1, 3], [5, 7, 9]])
arr2 = np.array([[0, 2, 4], [6, 8, 10]])

res=np.concatenate((arr1,arr2),axis=1)
print(res)

original_array = np.arange(12).reshape(3, 4)
new_arr=original_array*3
print(new_arr)



arr = np.array([[[0, 1],
                 [2, 3],
                 [4, 5]]])  

arr_list = arr.tolist()
print(arr_list)


arrays = np.array([0.26153123, 0.52760141, 0.5718299, 0.5927067, 0.7831874,
                0.69746349, 0.35399976, 0.99469633, 0.0694458, 0.54711478])

np.set_printoptions(precision=3, suppress=True)
print(arrays)

arr = np.array([[10, 20, 30],
                [40, 50, 60]])
extra=([100],[200])
print(np.concatenate((arr,extra),axis=1))


arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
indixes=[0,3,4]
new_arr=np.delete(arr,indixes)
print(new_arr)
