arr=[1,2,3,2,2,3]
count=0
target=2
for num in range(len(arr)):
    if(arr[num]==target):
        count+=1
if count>0:
     print(f"{target} occured {count} times")
else:
    print("no occurences")
