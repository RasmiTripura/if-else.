a=int(input("Take a number between 1500 and 2700="))
if a>=1500 and a<=2700:
    if a%5==0 and a%7==0:
        print("a is divsible by 7 and multiple by 5")
    else:
        print("not multiple not divisible")
else:
    print("number is not between 1500 to 2700")
