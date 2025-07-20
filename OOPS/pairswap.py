def pairswap(list=[1,2,3,4,5]):
    i=0
    while i<len(list)-1:
        list[i],list[i+1]=list[i+1],list[i]
        i+=2
    return list

print(pairswap())

