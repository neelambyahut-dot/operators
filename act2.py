sales_price=int(input("enter sales price : "))
cost_price=int(input("enter cost price : "))
if sales_price>cost_price:
    amount=sales_price-cost_price
    print("the amount is {0}".format(amount))

else:
    print("no profit")