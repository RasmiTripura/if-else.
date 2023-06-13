#Write a python program to input angles of a triangle and check whether triangle is
#valid or not.

a=int(input("Enter 1st angle="))
b=int(input("Enter 2nd angle="))
c=int(input("Enter 3rd angle="))
if a+b+c==180:
    print("This triangle is valid")
else:
    print("This triangle is not valid")