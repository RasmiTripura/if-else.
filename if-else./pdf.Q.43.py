age=int(input("Enter age="))
sex=input("Enter sex=")
day=int(input("Enter day="))
if age>=18 and age<30:
    if sex=="M":
        print("wage=",700*day)
    elif sex=="F":
        print("wage=",750*day)
    else:
        print("Enter appropriate age")
elif age>=30 and age<=40:
    if sex=="M":
        print("Wage=", 800*day)
    elif sex=="F":
        print("Wage=", 850*day)
    else:
        print("Enter appropriate age")
else:
    print("Enter appropriate age")


# if sex=="M" and age>=18 and age<30:
#     print("wage=",700*day)
# elif sex=="F" and age>=18 and age<30:
#     print("wage=",day*750)
# elif sex=="M" and age>=30 and age<=40:
#     print("wage=",day*800)
# elif sex=="F" and age>=30 and age<=40:
#     print("wage=", day*850)
# else:
#     print("Enter appropirate age")

