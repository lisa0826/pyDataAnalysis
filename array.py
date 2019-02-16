# -*- coding: utf-8 -*-
import numpy as np

#1、创建一个2*2的数组，计算对角线上元素的和:
m = np.array([np.arange(2), np.arange(2)])

print(m)
print(m.shape)
print(m.dtype)

#2. 创建一个长度为9的一维数据，数组元素0到8。将它重新变为3*3的二维数组
a = np.arange(9).reshape(3,3)
print(a)

#3. 创建两个3*3的数组，分别将它们合并为3*6、6*3的数组后，拆分为3个数组（维数不限定）
b = 2 * a
#合并为3*6的两种方式
print(np.hstack((a,b)))
print(np.concatenate((a,b),axis=1))
c = np.hstack((a,b))
#合并为6*3的两种方式
print(np.vstack((a,b)))
print(np.concatenate((a,b),axis=0))
d = np.vstack((a,b))
#拆分为3个数组
print(np.hsplit(c,3))
print(np.split(d,3,axis=1))