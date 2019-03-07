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

import matplotlib
matplotlib.use("TkAgg")  #这段代码修复报错：unrecognized selector sent to instance 0x7fb989f482a0
import matplotlib.pyplot as plt 

# fig = plt.figure()
# z = np.sqrt(xs ** 2 + ys ** 2)
# ax = fig.add_subplot(221)   #第一个子图
# ax.imshow(z)	#默认配置
# ax = fig.add_subplot(222)	#第一个子图
# ax.imshow(z,cmap = plt.cm.gray)		#第二个子图,使用自定义的colormap（灰度图）
# ax = fig.add_subplot(223)	#第一个子图
# ax.imshow(z,cmap=plt.cm.cool)	#第二个子图,使用自定义的colormap
# ax = fig.add_subplot(224)	#第一个子图
# ax.imshow(z,cmap=plt.cm.hot)	#第二个子图,使用自定义的colormap
# plt.show()	#显示图像

#将条件逻辑表达为数组运算
# xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
# yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
# cond = np.array([True, False, True, True, False])

# result = [(x if c else y)
#           for x, y, c in zip(xarr, yarr, cond)]
# result = np.where(cond, xarr, yarr)
# print(result)

##数学与统计方法
arr = np.random.randn(5,4)
# print(arr)

# #以下两个结果一样
# print(arr.mean())
# print(np.mean(arr))

# print(arr.sum())

# print(arr.mean(axis=1))
# print(arr.sum(0))

# arr = np.array([[0,1,2],[3,4,5],[6,7,8]])
# print(arr.cumsum(0))
# print(arr.cumprod(1))

#用于布尔型数组的方法
arr = randn(100)
(arr > 0).sum() # 正值的数量

bools = np.array([False, False, True, False])
# print(bools.any())
# print(bools.all())

#排序
# arr = randn(8)
# print(arr)
# arr.sort()
# print(arr)

# arr = randn(5, 3)
# print(arr)
# arr.sort(1)
# print(arr)

#唯一化以及其他的集合逻辑
# names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# print(np.unique(names))
# ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
# print(np.unique(ints))

# print(sorted(set(names)))

values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))








