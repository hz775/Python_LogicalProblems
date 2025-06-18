arr=[1,12,30,15,20]
largest=secondlargest=float('-inf')

for num in arr:
    if num>largest:
        secondlargest=largest
        largest=num
    elif num>secondlargest and num!=largest:
        secondlargest=num
print("secondlargest: ",secondlargest)
