testdata=int(input("Enter the number to check preseent or not: "))
list=[1, 5, 8, 3]
for num in list:
    if num==testdata:
        print("True")
        break
if testdata not in list:
    print("false")
    