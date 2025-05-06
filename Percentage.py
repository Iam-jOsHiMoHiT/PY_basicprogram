def CALCULATE(X):
    sum=0
    for i in X:
        sum+=i
    per=sum/len(X)
    print("\nTHE TOTAL MARKS ARE: ",sum )
    print("\nTHE PERCENTAGE IS: ",per)
    print("\nTHANK YOU FOR USING THE PERCENTAGE CALCULATOR")    



print("WELCOME TO THE PERCENTAGE CALCULATOR\n")
print("HOW TO USE?\n1. Enter the number of subjects you have.\n2. Enter the marks of each subject one by one." \
"\n3. The program takes MAXIMUM value of marks for each subject as 100.\n4. The program will calculate the total marks and percentage for you.")
NO=int(input("\nEnter the number of subjects: "))
X=[]
while NO >0:
    m=float(input("\nEnter the marks of subject: "))
    X.append(m)
    NO=NO-1
CALCULATE(X)
# This code calculates the percentage of marks obtained in a given number of subjects.
input("\nPress ENTER to exit")