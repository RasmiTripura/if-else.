num1=int(input("Enter 1st number="))
num2=int(input("enter 2nd number="))
num3=int(input("Enter 3rd number="))
if num1>num2>num3:
    print(num1,"is grater and",num3,"is smaller")
elif num1>num3>num2:
    print(num1,"is grater and",num2,"is smaller")
elif num2>num1>num3:
    print(num2,"is grater and",num3,"is smaller")
elif num2>num3>num1:
    print(num2,"is grater and",num1,"is smaller")
elif num3>num2>num1:
    print(num3,"is grater and",num1,"is smaller")
elif num3>num1>num2:
    print(num3,"is grater and",num2,"is smaller")
else:
    print("none")
    
