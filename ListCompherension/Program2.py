numbers=[1,2,3,-2,0,-6,4,-5,8,9]
positive_num=[num for num in numbers if num>0]
negative_num=[num for num in numbers if num<0]
divisiblebytwo=[num for num in numbers if num%2==0]
divisibleby3=[num for num in numbers if num%3==0]

print(positive_num)
print(negative_num)
print(divisibleby3)
print(divisiblebytwo)