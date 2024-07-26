import numpy as np

a= np.array(42)
b = np.array([2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6],[7,8,9],[3,6,7]]])


print("a array",a)
print("b array",b)
print("c array",c)
print("d array",d)
print("array dimension",a.ndim)
print("array dimension",b.ndim)
print("array dimension",c.ndim)
print("array dimension",d.ndim)

print("<------------------------------------------------------------------------------>")

'''arr =np.array[1,2,3,4,5,6]
arr2=arr[1:5:2]
print(arr2)
'''
print("<-------------------------------------------------------------->")

arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0]=42
print(arr)
print(x)

print("<-------------------------------------------------------------->")
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0]=42
print(arr)
print(x)


print("<-------------------------------------------------------------->")

i= ([10,30,25,45,78])
print(arr)


print("<-------------------------------------------------------------->")
arr = np.array([10,30,78,11,12])
print(arr)
print("<-------------------------------------------------------------->")

print("<-------------------------------------------------------------->")
a=np.zeros((6,), dtype=int)




print("<-------------------------------------------------------------->")
a=np.zeros((6,2))



print("<-------------------------------------------------------------->")
arr = np.array([[1,2,3],[4,5,6],[4,5,6]])
print(np.diag(arr))
 

print("<-------------------------------------------------------------->")
np.random.seed(122)
mat =np.random.randint(1,21,9).reshape(3,3)
print(mat)
print(np.sum(mat))
print(np.cumsum(mat))
print(np.min(mat))
print(np.max(mat))
print("<-------------------------------------------------------------->")
print(np.sum(mat,axis=0))
print(np.min(mat,axis=0))
print(np.max(mat,axis=0))
print(np.cumsum(mat,axis=0))



