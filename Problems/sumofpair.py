list=[1, 5, 7, -1, 5]
sum=6
found=[]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]+list[j]==sum:
            pair=[list[i],list[j]]
            if pair not in found:
                found.append(pair)
                print(pair)