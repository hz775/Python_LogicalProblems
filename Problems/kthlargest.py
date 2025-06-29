def kth_largest(lst, k):
    for i in lst:
        count = 0
        for j in lst:
            if j > i:
                count += 1
        if count == k - 1:
            return i

# res=kth_largest([1,2,3,4,5],2)
res=kth_largest([1,2,3,4,5],4)
print(res)
