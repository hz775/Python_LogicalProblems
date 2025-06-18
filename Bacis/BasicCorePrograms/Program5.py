N=int(input("Enter a number: "))
if N>0:
    i=1
    harmonic=0
    for i in range(1,N+1):
        harmonic+=1/i
        i+=1
    rounded_harmonic=round(harmonic,4)
    print("THE",N,"Harmonic value is: ",rounded_harmonic)
else:
    print("enter the num greater than 0")
    