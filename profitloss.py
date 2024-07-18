cp = float(input("enter the num:-"))
sp =float(input("enter the number:-"))           
if (cp<0):
   print    ("invalid cp")
elif(sp<0):
   print ("invalid sp")
else:
   if(sp>cp):
      print("profit : rs",(sp-cp)) 
   elif(cp>sp):
      print("loss rs",(cp-sp))
   else:
      print("no profit no loss")      



