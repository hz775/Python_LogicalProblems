# sort using second element
list=[(2, 3), (1, 4), (4, 5)]
sorted=sorted(list,key=lambda x:x[1])
print(sorted)