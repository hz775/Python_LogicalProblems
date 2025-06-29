list= [1, 2, 2, 3, 3, 3]
found={}
for i in range(len(list)):
    if list[i] in found:
        found[list[i]]+=1
    else:
        found[list[i]]=1
max_count = max(found.values())
print(max_count)