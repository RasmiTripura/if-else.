amount=int(input("Enter a amount="))
if amount>=5:
    a=amount//2000
    b=amount%2000
    c=b//500
    d=b%500
    e=d//200
    f=d%200
    g=f//100
    h=f%100
    i=h//50
    j=h%50
    k=j//20
    l=j%20
    m=l//10
    n=l%10
    o=n//5
    print("note of 2000=",a,"Note of 500=",c,"Note of 200=",e,"Note of 100=",g,"Note of 50=",i,"Note of 20=",k,"Note of 10=",m,"Note of 5=",o,)
else:
    print("No note is there")