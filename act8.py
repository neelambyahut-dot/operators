n=input("enter medical cause : ").strip().upper()
if n=="Y":
    print("you are elegible ")

else:
   m=int(input("enter attendance: "))
   if m>75:
       print("you are elegible")

   else :
       print("not elegible")
