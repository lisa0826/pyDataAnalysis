# -*- coding:utf-8 -*-
#向量相加-Python
def pythonsum(n):
    a = list(range(n))
    b = list(range(n))
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c

#向量相加-Numpy
import numpy as np 

def numpysum(n):
	a = np.arange(n) ** 2
	b = np.arange(n) ** 3
	c = a + b
	return c

#效率比较
from datetime import datetime

size = 1000

# start = datetime.now()
# c = pythonsum(size)
# delta = datetime.now() - start
# print("The last 2 elements of the sum", c[-2:])
# print("PythonSum elapsed time in microseconds", delta.microseconds)


# start = datetime.now()
# c = numpysum(size)
# delta = datetime.now() - start
# print("The last 2 elements of the sum", c[-2:])
# print("NumPySum elapsed time in microseconds", delta.microseconds)

#numpy数组
# a = np.arange(5)
# print(a.dtype)
# print(a.shape)
# print(a)

# #创建多维数组
# m = np.array([np.arange(2),np.arange(2)])
# print(m.dtype)
# print(m.shape)
# print(m)


#选取数组元素
a = np.array([[1,2],[3,4]])

print(a)
print(a[0,0])
print(a[0,1])
print(a[1,0])
print(a[1,1])






