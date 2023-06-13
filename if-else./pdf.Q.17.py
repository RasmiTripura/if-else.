#price1=int(input("Enter cost price="))
#price2=int(input("Enter selling price="))
#if price2>price1:
    #print("profit")
#else:
    #print("loss")

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# e=int(input())
# if a>=b and a>=c and a>=d and a>=e:
#     print(a,"grater")
# elif b>=a and b>=c and b>=d and b>=e:
#     print(b,"grater")
# elif c>=a and c>=b and c>=d and c>=e:
#     print(c,"grater")
# elif d>=a and d>=b and d>=c and d>=e:
#     print(d,"grater")
# elif e>=a and e>=b and e>=c and e>=d :
#     print(e, "is grater")
# else:
#     print("equal")

a1=int(input())
a2=int(input())
a3=int(input())
if a1+a2+a3==180:
    print(" Triangle is valid")
    if a1==a2==a3:
        print("Triangle is equiangular")
        if a1==90 or a2==90 or a3==90:
            print("right angled")
            if a1>90 or a2>90 or a3>90:
                print("obtus_angled")
                if a1<90 and a2<90 and a3<90:
                    print("acute_angled")
                else:
                    print("Not an acute angled")
            else:
                print("Not a obtus_angled")
        else:
            print("Not a right angled triangle")
    else:
        print("Triangle is not an equiangular")
else:
    print("Triangle is not valid")

