# write numpy program to create an arrayof 10 zeros 10 ones 10 fives
import numpy as np


zeros = np.zeros(10)
ones = np.ones(10)
fives = np.full(10,5.)


print(zeros)
print(ones)
print(fives)

# numpy program to create 3x3 with values range from 2to 10

array= np.arange(2, 11).reshape(3, 3)

print(array)
