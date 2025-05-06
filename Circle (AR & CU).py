print("WELCOME !..... TO OUR WEBPAGE:")
pass
radius=float(input("enter the radius? "))
pass
print("what do you want to calculate:"
      "1.Area\n"
      "2.circumference")
choice = int(input("Choose 1 or 2"))
pass
if choice==1:
    Area=3.14*radius**2
    pass
    print("the area of the circle is ",Area)
if choice==2:
    circumference=2*3.14*radius
    pass
    print("The circumference of the circle is ",circumference)

if choice!=1 and 2:
    pass
    print("CHOOSE VALID OPTION")

input("Press ENTER to exit")