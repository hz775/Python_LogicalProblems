a=["Apple","Mango","Sai","Hemanth",4,5,6]
a.append("Kiwi")
print(a)

b=["Apple","Mango","Sai","Hemanth",4,5,6]
b.insert(2,"Rohan")
print(b)

c=["Apple","Mango","Sai","Hemanth",4,5,6]
print(c.index("Apple"))

d=["Apple","Mango","Sai","Hemanth",4,5,6]
e=["Pranav","Suryah"]
d.extend(e)
print(d)

f=["Apple","Mango","Sai","Hemanth",4,5,6]
if "Sai" in f:
  f.remove("Sai")  
print(f)

g=["Apple","Mango","Sai","Hemanth",4,5,6]
print(g.pop(1))

h=["Apple","Mango","Sai","Hemanth",4,5,6]
print(h.count(4))

i=["Apple","Mango","Sai","Hemanth"]
i.sort()
print(i)