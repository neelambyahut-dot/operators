amount=int(input("enter amount:"))
n1=(amount//100)
n2=(amount%100)//50
n3=((amount%100)%50)//10
print("100 rs note",n1)
print("50 rs note",n2)
print("10 rs note",n3)
