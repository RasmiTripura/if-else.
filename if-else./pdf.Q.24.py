age1=int(input("Enter 1st age="))
age2=int(input("Enter 2nd age="))
age3=int(input("Enter 3rd age="))
if age1>age2 and age1<age3 and age2>age3:
    print("1st person is youngest and 2nd person is oldest")
elif age1>age2 and age1>age3 and age2<age3:
    print("1st is oldest and 2nd youngest")
elif age2<age1 and age2<age3 and age1<age3:
    print("2nd person is youngest and 3rd is oldest")
elif age2>age1 and age2>age3 and age1>age3:
    print("2nd person is oldest and 3rd is youngest")
elif age3<age1 and age3<age2 and age1>age2:
    print("3rd person is youngest and 1st is oldest")
elif age3>age1 and age3>age2 and age1<age2:
    print("3rd person is oldest and 1st is youngest")
else:
    print("3 persons are in same age")
