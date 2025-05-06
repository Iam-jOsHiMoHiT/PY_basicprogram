str1=input("enter a string:")
length=len(str1)
for a in range(-1,-length-1,-1):
    rev=str1[a]

if str1==rev:
    print(str1, "is a palindrome")
else:
    print(str1," is not a palindrome")

input("Press ENTER to exit")




