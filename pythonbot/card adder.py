print("Enter a file name you want to add information.")
print("(A new name will be created if the filename you entered is not in the folder.)")
FN=input(">> ")
f=open(FN,"a")

while 1:
    print("enter information or !exit")
    name=input(">> ")
    if name=="!exit":break
    f.write(name+"\n")

f.close()
