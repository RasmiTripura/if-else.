num=int(input("Enter 1st number="))
num1=int(input("Enter 2nd number="))
num2=int(input("Enter 3rd number="))
if num>num1>num2:
    print(num1,"is mediun")
elif num<num1<num2:
    print(num1,"is mediun")
elif num1>num2>num:
    print(num2,"is mediun")
elif num1<num2<num:
    print(num2,"is mediun")
elif num2>num>num1:
    print(num,"is mediun")
elif num2<num<num1:
    print(num,"is mediun")
else:
    print("none")
    