list= [1, 2, 2, 3, 3, 3]
found={}
for i in range(len(list)):
    if list[i] in found:
        found[list[i]]+=1
    else:
        found[list[i]]=1
max_count = max(found.values())
print(max_count)

def removefirstoccur(list):
    res=[]
    seen=[]
    for i in range(len(list)-1,-1,-1):
        if list[i] in res:
            seen.append(list[i])
        else:
            res.append(list[i])
    return res[::-1]

print(removefirstoccur([1,2,3,2,1,4,5]))

def first_non_repeating(lst):
    for i in range(len(lst)):
        count = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                count += 1
        if count == 1:
            return lst[i]
    return None 

            

