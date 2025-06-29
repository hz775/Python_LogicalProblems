def countelement(list):
    n=len(list)
    for i in range(len(list)):
        count=0

        for j in range(i+1,len(list)):
            if list[j]==list[i]:
                count+=1

            if count>n//2:
                return list[i]
            
            if 
                
    

print(countelement([3, 3, 4, 2,2,2 ,3,3,2]))


# list=[2,3,4,5,6,7,8]
# even=[]
# odd=[]
# for i in range(len(list)):
#     if list[i]%2==0:
#         even.append(list[i])
#     else:
#         odd.append(list[i])
# print(even)
# print(odd)



def countelement(lst):
    n = len(lst)
    res = []

    for i in range(n):
        count = 1
        for j in range(i + 1, n):
            if lst[j] == lst[i]:
                count += 1

        if count > n // 2 and lst[i] not in res:
            res.append(lst[i])

    if res:
        return res
    else:
        return "No element appears more than n//2 times"

print(countelement([3, 3, 4, 2, 2, 2, 3, 3, 2, 2, 3]))

















