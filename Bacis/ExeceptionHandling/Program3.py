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

try:
    a=int(input("Enter the num: "))
    b=int(input("Enter the num: "))
    result=a/b
except Exception as e:
    print("Error:",type(e).__name__)
else:
    print("result is:",result)
finally:
    print("Execution is done")

