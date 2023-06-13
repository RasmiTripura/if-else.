quantity=int(input("Enter the quantity="))
purchase_cost=quantity*100
if purchase_cost>=1000:
    discount=purchase_cost*0.1
    total_cost=purchase_cost-discount
    print(total_cost)
else:
    print("no discount")