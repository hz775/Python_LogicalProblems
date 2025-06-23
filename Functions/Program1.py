def add(a,b):
    return a+b

print(add(10,20))


def add(*args):
    total=0
    for num in args:
        total+=num
    print(total)

add(1,2,3,4,5)



