list=[1,2,3,4]
res=[]
for i in range(len(list)):
    total=0
    for j in range(len(list)):
        if i!=j:
            total+=list[j]
    res.append(total)
print(res)

        

arr = [2, 3, -2, 4]
max_product=arr[0]
for i in range(len(arr)):
    product=1
    for j in range(i,len(arr)):
        product*=arr[j]
        if max_product<product:
            max_product=product
print(max_product)
    






    

    




        



    


