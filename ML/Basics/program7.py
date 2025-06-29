color_list_1 = set(["White", "Black", "Red"])  
color_list_2 = set(["Red", "Green"])

print(color_list_1-color_list_2)


n=int(input("Enter no:"))
for i in range(n):
    for j in range(i+1):
        print(i,end=" ")
    print()


n=int(input("Enter no:"))
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()

n=int(input("Enter no:"))
for i in range(n):
    for j in range(i+1,n):
        print("*",end=" ")
    print()


n=int(input("Enter no:"))
for i in range(n):
    for j in range(i,0,-1):
        print(i+1,end=" ")
    print()