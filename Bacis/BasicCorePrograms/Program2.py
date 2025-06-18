import random

n=int(input("Enter how  many times have to flip:"))
heads=0
tails=0
for i in range(n):
    if random.random()<0.5:
        tails=+1
    else:
        heads=+1

tail_percent=((tails/n)*100)
head_percent=((heads/n)*100)

print("Tails: ",round(tail_percent,2),"%")
print("Heads: ",round(head_percent,2),"%")