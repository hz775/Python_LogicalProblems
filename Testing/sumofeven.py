a=[1,2,3,4,5,6]
sum_of_even=sum([num for num in a if num%2==0])
print(sum_of_even)

from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

result = reduce(lambda x, y: x + y, [x for x in nums if x % 2 == 0])
print(result)   

pairs = [(1, 2), (3, 4), (5, 6)]
swap=[(b,a) for a,b in pairs]
print(swap)

nums = [1, 2, 3, 4]
pairs = [(i, j) for i in nums for j in nums if i < j]
print(pairs)