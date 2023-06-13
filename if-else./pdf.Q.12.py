#Write a python program to input the month number and print the number of daysin that month.

mon=int(input("Enter a month number="))
if mon==1:
    print("Number of days in this month=", 31)
elif mon==2:
    print("Number of days in this month=", 28)
elif mon==3:
    print("Number of days in this month=", 31)
elif mon==4:
    print("Number of days in this month=", 30)
elif mon==5:
    print("Number of days in this month=", 31)
elif mon==6:
    print("Number of days in this month=", 30)
elif mon==7:
    print("Number of days in this month=", 31)
elif mon==8:
    print("Number of days in this month=", 31)
elif mon==9:
    print("Number of days in this month=", 30)
elif mon==10:
    print("Number of days in this month=", 31)
elif mon==11:
    print("Number of days in this month=", 30)
elif mon==12:
    print("Number of days in this month=", 31)
else:
    print("This is not a month number.")
    