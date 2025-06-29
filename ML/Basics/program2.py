# str=input("enter the num: ")
# input=str.split(",")
# item_tuple=tuple(input)
# print("List:",input)
# print("Tuple: ",item_tuple)



str=input("enter the num: ")
list=[]
for i in range(len(str)):
    if str[i]!=",":
        list.append(str[i])
print(list)
tupleas=tuple(list)
print(tupleas)
