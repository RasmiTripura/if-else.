a=int(input("Enter number of days="))
if a>=1 and a<=5:
    print(a*2,"charge")
elif a>=6 and a<=10:
    print(a*3,"charge")
elif a>10 and a<=15:
    print(a*4,"charge")
elif a>15:
    print(a*5,"charge")
else:
    print("No charge")

    