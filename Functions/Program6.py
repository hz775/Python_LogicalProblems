def maxinlist(lst):
    max=lst[0]
    for i in lst:
        if(i>max):
            max=i    
    return max

print(maxinlist([1,4,5,6,8]))

    