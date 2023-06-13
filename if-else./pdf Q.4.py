#Write a python program to check whether a number is divisible by 5 and 11 or
#not.
a=int(input("enter a number="))
if a%5==0:
    print("The number is devisible by 5")
elif a%11==0:
    print("The number is devisible by 11")
else:
    print("Number is not devisible by 5 or 11")
