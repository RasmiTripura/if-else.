a=int(input("Enter side a="))
b=int(input("Enter side b="))
c=int(input("enter side c="))
if a+b>c and a+c>b and b+c>a:
    print("This triangle is valid")
else:
    print("This triangle is not valid")
