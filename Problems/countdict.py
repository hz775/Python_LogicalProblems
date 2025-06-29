list=[1,2,3,3,2,1]
count_dict={}
for i in range(len(list)):
    if list[i] in count_dict:
        count_dict[list[i]]+=1
    else:
        count_dict[list[i]]=1

print(count_dict)