array=[1,2,3,45,60]
target=45
found=False
for num in range(len(array)):
    if(target==array[num]):
        print("found at index: ",num)
        found=True
        break
if not found:
    print("Number is not present")
