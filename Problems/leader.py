list=[16, 17, 4, 3, 5, 2]
res=[]
for i in range(len(list)):
    max=list[i]
    flag=True
    for j in range(i+1,len(list)):
        if list[j]>max:
            max=list[j]
            flag=False
            break
    if flag:
        res.append(list[i])
print(res)
