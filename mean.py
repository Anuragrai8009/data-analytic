# find the mean 
import numpy as np
arr =np.array([1,2,3,4,5])
mean_value =np.mean(arr)
print(mean_value)



print("<-------------------------------------------------------------->")
arr1 =np.array([1,2,3,4,5,6])
a =np.split(arr1, 3)
for b in a:
 print(b)

print("<-------------------------------------------------------------->")
#  
ar =np.sort([3,1,2,4,5])
sorted_arr =np.sort(ar)
print(sorted_arr)
sorted_arr_decen = np.sort(ar)[::-1]
print(sorted_arr_decen)

print("<-------------------------------------------------------------->")


#Test scores of 30 students 
test_scores = np.array([65, 75, 80, 85, 90, 92, 94, 95, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138]) 
median = np.percentile(test_scores, 50) 
print("Median (50th Percentile):",median)

print("<-------------------------------------------------------------->")
matrix =np.array([[3,1,2],[6,5,4]])
sorted_matrix =np.sort(matrix,axis =1)
print("sorted matrix(ascending along rows)")
print(sorted_matrix)

print("<-------------------------------------------------------------->")
# concatnate the array
a = np.array([[1,2],[3,4]])
b= np.array([[5,6],[7,8]])
result = np.concatenate( (a,b),axis = 1)
print(result)

print("<-------------------------------------------------------------->")
# create horizontal stack 
ar1 =np.array([1,2,3])
ar2 =np.array([4,5,6])
result= np.hstack((ar1,ar2))
print(result)
print("<-------------------------------------------------------------->")

# create vertical stack 

ar1 =np.array([1,2,3])
ar2 =np.array([4,5,6])
result= np.vstack((ar1,ar2))
print(result)

print("<-------------------------------------------------------------->")



classB= np.array([70,80,85,95,100])
classB_mean = np.mean(classB)
print("classB score average",classB_mean)
var = np.var(classB)
print("classB  variance",var)
std = np.std(classB)
print("class B variance is" ,std)


print("<-------------------------------------------------------------->")
scores =np.array([85,92,78,88,95,72,89])
np.save("student_score.npy",scores)
loaded_score =np.load("student_score.npy")
print("original scores", scores)
print("loaded score", loaded_score)