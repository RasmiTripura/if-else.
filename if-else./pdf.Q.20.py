# Q.Write a python program to input electricity unit charges and calculate total
# electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

unit=int(input("Enter the unit charge="))
if unit<=50:
    a=unit*0.50+20/100
    print("total bill=",a)
elif unit>=51 and unit<=150:
    b=(50*0.50)+(unit-50)*0.75+20/100
    print("total bill=",b)
elif unit>=151 and unit<=250:
    c=(50*0.50)+(100*0.75)+(unit-150)*1.20+20/100
    print("totl bill=",c)
elif unit>250:
    d=(50*0.50)+(100*0.75)+(100*1.20)+(unit-250)*1.50+20/100
    print("total bill=",d) 
else:
    print("No bill")



  