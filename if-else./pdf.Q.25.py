clas=int(input("Enter total class held="))
attend=int(input("Enter total attended="))
percentage=(attend/clas)*100
if percentage>=75:
    print("Allowed to sit in exam")
else:
    print("Not allowed to sit in exam")