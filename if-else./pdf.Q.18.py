sub1=int(input("Entere mark of Physics="))
sub2=int(input("Enter mark of Chemistry="))
sub3=int(input("Enter mark of Biology="))
sub4=int(input("Enter mark of Mathematics="))
sub5=int(input("Enter mark of Computer="))
total=(sub1+sub2+sub3+sub4+sub5)
avg=(total/500)*100
if avg>=90 and avg<=100:
    print("Grade A")
elif avg>=80:
    print("Grade B")
elif avg>=70:
    print("Grade C")
elif avg>=60:
    print("Grade D")
elif avg>=40:
    print("Grade E")
else:
    print("Grade F")


