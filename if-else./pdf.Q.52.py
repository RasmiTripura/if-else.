year=int(input("Enter a year="))
month=int(input("Enter a month="))
date=int(input("Enter a date="))
if year>=2000 or year<=2022 and month>=1 or month<=12 and date>=1 or date<=31:
    print(year,"-",month,"-",date+1)
else:
    print("Error")