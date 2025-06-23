def doublenum():  
    for i in list3:
        print(i*i)
list3=[1,2,3,4,5]    
doublenum()

list1=[1,2,3,4,5] 
result=list(map(lambda x:x*x,list1))
reversed=result[::-1]
print(reversed)



squares=[1, 2, 3, 4]
result=map(lambda x:x*x,squares)
print(list(result))


even=[1, 2, 3, 4, 5, 6]
even_num=list(filter(lambda x:x%2==0,even))
print(even_num)

string=["apple", "banana"]
upper=list(map(lambda x:str.upper(x),string))
print(upper)

list1=[(1, 2), (3, 1), (5, 0)]
res=sorted(list1,key=lambda x:x[1])
print(res)

dict=[{"name": "A", "score": 90}, {"name": "B", "score": 80}]
res=max(dict,key=lambda x:x["score"])
print(res)

str=["hi", "hello", "world"] 
res=sorted(str,key=lambda x:len(x))
print(res)

fil=["dog", "deer", "cat", "duck"]
res=list(filter(lambda x:x.startswith('d'),fil))
print(res)