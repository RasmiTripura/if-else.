a=int(input("Enter 1st age="))
b=int(input("enter 2nd age="))
c=int(input("Enter 3rd age="))
d=int(input("Enter 4th age="))
if a>b and a>c and a>d:
    print(a,"is oldest")
elif b>a and b>c and b>d:
    print(b,"is oldest")
elif c>a and c>b and c>d:
    print(c,"Is oldest")
elif d>b and d>a and d>c:
    print(d,"Is oldest")
else:
    print("None")