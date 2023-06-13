num1=int(input("Enter 1st number="))
num2=int(input("Enter 2nd number="))
op=input("Enter a operator")
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
elif op=="//":
    print(num1//num2)
elif op=="%":
    print(num1%num2)
elif op=="**":
    print(num1**num2)
else:
    print("none")  