N=int(input("Enter a number(0 to 30): "))
if N>=0 and N<=30:
    i=0
    while(i<=N):
        print("2^",i,"=",2**i)
        i+=1
else:
    print("enter the number between 0 to 30")


# if N>=0 and N<=10:
#     i=0
#     while(i<=N):
#         print("2*",i,"=",2*i)
#         i+=1
# else:
#     print("Enter number between 0 to 10")


