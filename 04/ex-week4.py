# -*- coding: utf-8 -*-
from __future__ import division
from numpy.random import randn
import numpy as np 

##通用函数
arr = np.arange(10)
# print(arr)
# print(np.sqrt(arr))
# print(np.exp(arr))

x = randn(5)
y = randn(5)
# print(x)
# print(y)
# print(np.maximum(x,y))

##利用数组进行数据处理
#向量化
points = np.arange(-5,5,0.01)
# print(points)
xs,ys = np.meshgrid(points,points)
# print(xs,ys)

import matplotlib.pyplot as plt 
z = np.sqrt(xs ** 2 + ys ** 2)
# print(z)
# plt.imshow(z, cmap=plt.cm.gray)
# plt.colorbar()
# plt.draw()




