t = (1, 3, 7, 3, 9, 3)
value=3
for i in range(len(t)):
    if t[i]==value:
        print(i)


t1 = (1, 2, 3)
t2 = (4, 5, 6)
for i in range(len(t1)):
    for j in range(len(t2)):
        if t1[i]!=t2[j]:
            flag=True
            break
        if not flag:
            break
if flag:
    print(t1+t2)

# first element even
list=[(2, 3), (1, 4), (4, 5)]
res=[]
for i in range(len(list)):
    if list[i][0]%2==0:
        res.append(list[i])
print(res)



        