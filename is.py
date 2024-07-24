x =["apple","banana"]
y = ["apple","banana"]
z =x
print(x is z)
print(x is y)



print("<------------------------------------------------------------>")
str = "Anurag"
print(str.center(20,"*"))

print("<------------------------------------------------------------>")

str ="second a start index and third"
oc =str.count("a")
print (oc)

str ="second a start index and third"
oc =str.count("a",3,8)
# in which we are finding number of occurence
print (oc)   


print("<------------------------------------------------------------>")

str ="second a start index and third"
oc =str.endswith("and")
print (oc)


str ="second a start index and third"
oc =str.endswith("nd",0,6)
print (oc)



print("<------------------------------------------------------------>")
str = "welcome to python class"
str2 = str.find("t")
print(str2)


print("<------------------------------------------------------------>")

str = "welcome232efj"
a = str.isalnum()
print(a)


str = "welcome232efj"
a = str.isalpha()
print(a)

str = "welcome232efj"
a = str.isnumeric()
print(a)

str = "welcomeefj"
a = str.islower()
print(a)


str = "welcomeefj"
a = str.isupper()
print(a)



str = "welcomeefj"
a = str.upper()
print(a)



str = "welcomeefj"
a = str.lower()
print(a)

str = "           welcomeefj"
a = str.lstrip()
print(a)

str = "welcomeefj                "
a = str.rstrip()
print(a)


str = "      welcomeefj"
a = str.strip()
print(a)


str = "welcome to python class  python"
str2 = str.replace("python","c",1)
print(str2)


str = "welcome to python class  python"
str2 = str.replace("python","c",2)
print(str2)


