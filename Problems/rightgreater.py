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