multiply=lambda x,y:x*y
res=multiply(12,33)
print(res)


power=lambda x,y:x**y
resl=power(2,3)
print(resl)


add=[2,4,6,8]
result=map(lambda x:x+x,add)
print(list(result))

data=[111,222,333,23,13,45,66]
sorted=map(lambda x:x,sorted(data))
print(list(sorted))


