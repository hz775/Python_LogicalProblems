list=[4,3,2,7,8,2,3,1]
new_list=[]
for i in range(len(list)):
    count=0
    for j in range(i+1,len(list)):
        if list[i]==list[j]:
            count+=1
            if count>1:
                new_list.append(list[i])
print(new_list)
