cost=int(input("Enter cost price of bike="))
if cost>=100000:
    a=cost*15/100
    print(a,"tax to be paid")
elif cost>50000 and cost<=100000:
    b=cost*10/100
    print(b,"tax to be paid")
elif cost<=50000:
    c=cost*5/100
    print(c,"tax to be paid")
else:
    print("No tax to be paid")
