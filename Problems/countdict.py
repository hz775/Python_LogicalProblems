list=[1,2,3,3,2,1]
count_dict={}
for i in range(len(list)):
    if list[i] in count_dict:
        count_dict[list[i]]+=1
    else:
        count_dict[list[i]]=1

print(count_dict)


n=5
res=[]
for i in range(1,n+1):
    mul=i*i
    res.append(mul)
print(res)

list=[1,2,3,4,5]
res=[]
for i in range(len(list)):
    if list[i]%2==0:
        continue
    print(list[i])

list=[1, 2, 4, 7, 10]
count=0
for i in range(len(list)):
    if list[i]%2==0:
        count+=1
print(count)

list=[1, -2, 3, -4]
res=[]
for i in range(len(list)):
    if list[i]<0:
        res.append(0)
    else:
        res.append(list[i])
print(res)

list=[1, 2, 2, 3, 1]
res=[]
for i in range(len(list)):
    if list[i] not in res:
        res.append(list[i])
print(res)

list=[4, 2, 7, 5]
target=7
for i in range(len(list)):
    if list[i]==target:
        print(i)

list=[10, 20, 30, 40, 50]
res=[]
for i in range(1,len(list)):
    if i%2!=0:
        res.append(list[i])
print(res)


list=[1, 3, 7, 3, 9, 3]
element=3
res=[]
for i in range(len(list)):
    if list[i]==element:
        res.append(i)
print(res)

list=[1, 2, 3, 4]
res=[]
target=5
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]+list[j]==target:
            res.append((list[i],list[j]))
print(res)

nested = [[1, 2], [3, 4], [5]]
flat=[]
for num in nested:
    for item in num:
        flat.append(item)
print(flat)

list=[1, 2, 2, 3, 1, 1, 2]
for i in range(len(list)):
    count=0
    for j in range(len(list)):
        if list[i]==list[j]:
            count+=1
if count==3:
    print(list[i])