list=[1,2,3,4]
res=[]
for i in range(len(list)):
    total=0
    for j in range(len(list)):
        if i!=j:
            total+=list[j]
    res.append(total)
print(res)


list=[16, 17, 4, 3, 5, 2]
res=[]
max=0
for i in range(len(list)):
    if i==len(list)-1:
        res.append(-1)
    else:
        max=list[i+1]
        for j in range(i+2,len(list)):
            if list[j]>max:
                max=list[j]
        res.append(max)
print(res)
        
arr = [3, 4, 9, 6, 1]
res=[]
for i in range(len(arr)):
    count=0
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            count+=1
    res.append(count)
print(res)
    


