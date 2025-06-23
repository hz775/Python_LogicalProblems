arr=[1,-2,3,4,5,-3]
curr_max=arr[0]
max_sofar=arr[0]
for i in arr:
    curr_max=max(i,curr_max+i)
    max_sofar=max(max_sofar,curr_max)
print(max_sofar)