list1=["John","Jai","Hemanth","Jaivel","Sai","Rohan"]
list=[]
for i in list1:
    if 'J' in i:
        list.append(i)
print(list)

list2=[name for name in list1 if 'J' in name ]
print(list2)