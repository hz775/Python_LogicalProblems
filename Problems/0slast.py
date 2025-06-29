list=[0, 1, 0, 3, 12]
mul=[]
for i in range(len(list)):
    if list[i]==0:
        pass
    else:
        mul.append(list[i])
for i in range(len(list)):
    if list[i]==0:
        mul.append(list[i])
print(mul)

list=[0, 1, 0, 3, 12]
for i in range(len(list)):
    if list[i]==0:
        list.remove(0)
        list.append(0)
print(list)
