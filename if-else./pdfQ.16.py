a=int(input("Enter 1st value="))
b=int(input("Enter 2nd value="))
c=int(input("Enter 3rd value="))
if a==b==c:
    print("This is an equilateral triangle")
elif a==b!=c or a!=c==b or b!=a==c:
    print("This is an isosceles triangle")
else:
    print("This is an scalene triangle")