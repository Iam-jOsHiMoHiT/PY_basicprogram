orig = input("enter a string")
l1 = orig.split(sep=" ")
new=""
for i in l1:
    i = i[0].upper() + i[1 : -1] +i[-1].upper()
    new=new+i
print(new)
input("Press ENTER to exit")