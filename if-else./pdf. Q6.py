a=int(input("enter a year="))
if a%4==0:
    print("year is leap year")
elif a%100!=0 and a%400==0:
    print("The year is century year")
else:
    print("the year is not a leap year")


# a=int(input("enter a year"))
# if a%4==0:
#     if a%100==0:
#         if a%400==0:
#             print(" this year is leap year")
#         else:
#             print("This is not a leap year")    
# else:
#     print("this year is not a leap year")