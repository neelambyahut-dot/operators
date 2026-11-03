n=int(input("enter the units consumed : "))
if n<50:
    amt=n*2.6
    surcharge=25

elif n<=100:
    amt=130+(n-50)*3.25
    surcharge=35

elif n<=200:
    amt= 130+162.50+(n-100)*5.26
    surcharge=45

else:
    amt=130+162.50+526+(n-200)*8.45
    surcharge=75

total=amt+surcharge
print("the bill is",total)