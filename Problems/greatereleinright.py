arr = [3, 4, 9, 6, 1]
res=[]
for i in range(len(arr)):
    count=0
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            count+=1
    res.append(count)
print(res)