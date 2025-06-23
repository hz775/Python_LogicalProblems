f=open(r"C:\Users\akhem\OneDrive\Documents\Fileio.txt","w")   #here r is represnt as raw data so we dont give double slash
f.write("Hemanth\n")
f.write("Rohan\n")
f.write("Sai\n")
f.write("Suryah\n")
f.close()
print("File is closed or not: ",f.closed)


file=open(r"C:\Users\akhem\OneDrive\Documents\Fileio.txt","r")
data=file.read()
print("The file is reading",data)

file=open(r"C:\Users\akhem\OneDrive\Documents\Fileio.txt","a+")
file.write("He is Good Boy\n")
file.close()
print("The file is apended to the extended file")

file=open(r"C:\Users\akhem\OneDrive\Documents\Fileio.txt","r")
data=file.read()
print()