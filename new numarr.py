import numpy as np
arr = np.random.randint(0,100,12)
print(arr)


print("<--------------------------------------->")
##The respae function in numpy allows you to change the shape of an array without changing its data.
arr=np.random.randint(0,100,12)
print(arr)
arr=arr.reshape(4,3)
print(arr)
print("Array vaues is",arr[0][1])
print("Array vaues is",arr[1][0])
print(arr.shape)
arr=arr.reshape(-1,4)
print(arr)
arr=arr.reshape(2,-1)
print(arr)

print("<--------------------------------------->")
np.random.seed(145)
arr = np.random.randint(0,500,30)
arr= arr.reshape(6,5)
print(arr)

print("<--------------------------------------->")
print(arr[2:,2:])
print(arr[3:5,2:4])

print("<--------------------------------------->")

ar = np.array([1,20,5,9,3,4,8,5,6,2,25,2,2265,3,33])
slicing =ar[4:9]
print("new slicing",slicing)
print("new array",ar)
print(type(slicing))
print(type(ar))
slicing[:]= 0
print("old slicing",slicing)
print("old array",ar)

print("<--------------------------------------->")
ar1 =np. arange(1,15)
print(ar1)
print(ar1%2 == 0)
print(ar1%2 != 0)
print(ar1[ar1>8])
ar1[ar1%2==0]=0
print(ar1)

print("<--------------------------------------->")
ar1 =np.arange(1,8)
print(ar1+2)
print(ar1*2)
print(ar1**2)

print("<--------------------------------------->")
arrr=np.array([10,20,30,25,6,2])
print(np.min(arrr))
print(np.max(arrr))
print(np.argmin(arrr))
print(np.argmax(arrr))
print(np.sqrt(arrr))
print(np.sin(arrr))
print(np.cos(arrr))




