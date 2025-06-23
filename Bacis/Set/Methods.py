set={"Hemanth","Sai","Pranav","Rohan",3,5,6,7}
set.add("Suryah")
print(set)
set.update(["Govinda"])
print(set)
set.remove("Govinda")        #in remove if element is not present it will give error
print(set)
set.discard("Hem")           #discard is to remove the element is present or it will print as it is
print(set)
set.pop()                    #SET pop takes no arg it will remove randomly
print(set)
set.clear()
print(set)

set1={"a","b","c","d","e"}
set2={1,2,3,4,"a","b"}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.copy())
