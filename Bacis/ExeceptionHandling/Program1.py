try:
    a=int(input())
    b=int(input())
    print(a+b)
    c=input()
    d=c/a
    print(d)
except ValueError as v:
    print("ValueError",v)
except TypeError as e:
    print("TypeEror",e)
