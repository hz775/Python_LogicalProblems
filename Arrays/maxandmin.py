array=[20,30,15,60]
max=array[0]
min=array[0]
for i in range(len(array)):
    if(array[i]>max):
        max=array[i]
    elif(array[i]<min):
        min=array[i]
print("Maximum:",max)
print("Minimum:",min)
