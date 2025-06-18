arr=[2,3,4,6,7,8]
even_num=0
even_count=0
for i in range(len(arr)):
    if(arr[i]%2==0):
        even_num+=arr[i]
        even_count+=1
if even_count>0:
    avg=even_num/even_count
    print("Average:",round(avg,2))
else:
    print("no even num is present ")

