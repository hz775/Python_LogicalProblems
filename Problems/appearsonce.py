list=[2, 3, 2, 4, 4]
res=[]
for i in range(len(list)):
    count=0
    for j in range(len(list)):
        if list[i]==list[j]:
            count+=1
    if count==1:
        print(list[i])