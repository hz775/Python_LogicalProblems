def missing_no(number=[4,3,2,7,8,2,3,1]):
    res=[]
    for i in range(1,len(number)+1):
        if i not in number:
            res.append(i)
    return res

print(missing_no())


def index_find(number,target):
    res=[]
    for i in range(len(number)):
        if number[i]==target:
            res.append(i)
    return res
print(index_find([5,1,2,3,2,4,2],2))



def count_matching_str(strings):
    count=0
    for s in strings:
        if len(s)>=2 and s[0]==s[-1]:
            count+=1
    return count

sample_list=["aba","abc","xyz","121"]
res=count_matching_str(sample_list)
print(res)

list=["1234thomas","13663hema","1635siddu"]
inte=[]
stri=[]
for word in list:
    num=""
    ch=""
    for char in word:
        if char.isdigit():
            num+=char
        else:
            ch+=char
    inte.append(num)
    stri.append(ch)

print(stri)
print(inte)

str1="abcabaca"
my_dict={}
for char in str1:
    if char not in my_dict:
        my_dict[char]=1
    else:
        my_dict[char]+=1
        print(char*my_dict[char])