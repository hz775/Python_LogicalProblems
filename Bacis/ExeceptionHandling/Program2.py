def calculator(a,b,op):
    try:
        if op=="+":
            print(a+b)
        elif op=="-":
            print(a-b)
        elif op=="*":
            print(a*b)
        elif op=="/":
            print(a/b)
        else:
            print("Invalid Operator")
    
    except ZeroDivisionError as e:
        print("Cannot divide by 0")
    except Exception as e:
        print("Errror:",type(e).__name__)
    finally:
        print("Done")

a=int(input("Enter num: "))
b=int(input("Enter num: "))
op=input("Enter operator (+,-,*,/):")
calculator(a,b,op)