def sumofeven(lst):
    total=0
    for i in lst:
        if i%2==0:
            total=total+i
    return total

print((sumofeven([2,4,5,6,7,8])))