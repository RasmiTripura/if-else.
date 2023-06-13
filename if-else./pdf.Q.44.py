a=int(input("Enter 1st number="))
b=int(input("Enter 2nd number="))
c=int(input("Enter 3rd number="))
if a>b>c or c>b>a:
    print(b,"is second largest")
elif b>a>c or c>a>b:
    print(a,"is second largest")
elif a>c>b or b>c>a:
    print(c,"Is seconnd largest")
else:
    print("No second largest number")