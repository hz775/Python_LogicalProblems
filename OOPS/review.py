# Write a function that accepts two pairs of numbers [ a, b ] and [ c, d ] where
# each pair represents the range a to b and c to d respectively. The function
# upon execution returns another pair [ x, y ] which is the intersection of the
# above two pairs.
def twopairs(list1,list2):
    
    a,b=list1
    c,d=list2

    x=max(a,c)
    y=min(b,d)

    if x<y:
        return  [x,y]


print(twopairs([1,4],[3,5]))


    

    
    


    


    



    

