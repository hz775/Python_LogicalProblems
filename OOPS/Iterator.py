
# for i in x:
#     print(i)
x=[1,2,3,4,5,6,7,8]
y=iter(x)
try:
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
except StopIteration:
    print("This is finished")


# Think of an iterable as a book, 
# and an iterator as a bookmark that tells you where you are as you flip through it page by page.