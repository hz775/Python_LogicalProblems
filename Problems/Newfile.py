def calculate(n):
    rev=n[::-1]
    for i in rev:
        print(i*i+i)

n=[1,2,3,4]
calculate(n)


def cal():
    list1=[1,2,3,4]
    total=24
    mul=[]
    for i in list1:
        res=total//i
        mul.append(res)
        print(res)

cal()
        
def calculate():
    list1=[1,2,3,4]
    total=1
    mul=[]
    for i in list1:
        total=total*i
    for i in list1:
        result=total//i
        mul.append(result)
    print(mul)

calculate()



num=100
while num>1:
    print(num)
    num-=1


num=3
i=1
while i<=10:
    print(f"{i}*3={num*i}")
    i+=1


list=[1,2,3,55,6,7,88,99,100]
l=[]
idx=0
while idx<len(list):
    print(list[idx])
    l.append(list[idx])
    idx+=1



i=0
while i<len(tuple):
    if(tuple[i]==search):
        print("found")
        print(i)
    i+=1

tuple=(1,2,3,55,6,7,88,99,100)
search=100
if search in tuple:
        print("found")



list=[1,2,3,4]
res=[]
for i in range(len(list)):
    product=1
    for j in range(len(list)):
        if i!=j:
            product=product*list[j]
    res.append(product)
print(res)














