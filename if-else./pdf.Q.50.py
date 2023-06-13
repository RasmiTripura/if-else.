mon=int(input("Enter month number="))
day=int(input("Enter day in month="))
if mon==1 or mon==2 or mon==12:
    if day>=1 or day<=31:
        print("Season is winter")
    else:
        print("Invalid month")
elif mon==3 or mon==4 or mon==5:
    if day>=1 or day<=31:
        print("Season is spring")
    else:
        print("Invalid day")
elif mon==6 or mon==7 or mon==8:
    if day>=1 or day<=31:
        print("season is summer")
    else:
        print("Invalid number")
elif mon==9 or mon==10 or mon==11:
    if day>=1 or day<=31:
        print("Season is Autumm")
    else:
        print("No month")
else:
    print("None")