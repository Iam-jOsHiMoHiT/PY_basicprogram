str1=int(input("enter a no : "))  #its an palindrome for a number
orig=str1
rev=0

while orig>0:
    temp=orig%10
    rev=rev*10+temp
    orig=orig//10

if rev==str1:
    print("The given no. is a palindrome !")
else:
    print("The given no. is not  a palindrome !")


input("Press ENTER to exit")