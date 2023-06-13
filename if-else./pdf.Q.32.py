unit=int(input("Enter unit="))
if unit<=100:
    print("No charge")
elif unit>100 and unit<=200:
    a=(unit-100)*5
    print("Total bill=",a)
elif unit>200:
    b=(100*5)+(unit-200)*10
    print("Total bill=",b)
else:
    print("No bill")
    