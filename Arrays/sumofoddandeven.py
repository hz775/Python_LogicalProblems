array=[2,4,6,8,3,5]
even_sum=0
odd_sum=0
for i in range(len(array)):
    if(array[i]%2==0):
        even_sum+=array[i]
        print("even: ",array[i])
    else:
        odd_sum+=array[i]
        print("odd: ",array[i])
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)