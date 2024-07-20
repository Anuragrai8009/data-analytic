#In which we are find the memory address
 
a=10,20,30
print(a)
print(id(a))


a= 100,200,300,500
print(a)
print(id(a))


#in which we are conveerting list into set
months =("january","feburary","march","january")
print(months)
months = set(months)
print(len(months))


months ={"january","feburary","march","april","May","june"}
print(months)
months.add("august")
months.update(["july","august","sepetember","oclober"]);
print(months)


months ={"january","feburary","march","april","May","june"}
print(months)
months.discard("august");
months.discard("oct");
print(months)


months ={"feburary","march","april","May","june"}
print(months)
months.remove("april")
# months.remove("january"); #error
print(months)