sex=input("Enter sex=")
age=int(input("Enter age="))
status=input("Enter marital status=")
if sex=="Female" and age>=20 and age<=60:
    if status=="Y" or status=="N":
        print("She will work in urban areas")
    else:
        print("not appropriate age")    
elif sex=="Male" and age>=20 or age<=40:
    if status=="Y" or status=="N":
        print("He can work in anyplace")
    else:
        print("none")
elif sex=="Male" and age>40 and age<=60:
    if status=="Y" or status=="N":
        print("He will work in urban area")
    else:
        print("none")
else:
    print("Error")


