# -*- coding: utf-8 -*-
import numpy as np
import os

# 1. 读入ag0613.csv数据集，并计算数据的最大值、最小值、均值、标准差、中位数
ag = np.loadtxt('ag0613.csv',skiprows=1)
	
print(ag)#打印所有取出的值
print("maxAg = ", np.max(ag))#取最大值
print("minAg = ", np.min(ag))#取最小值
print("meanAg = ", np.max(ag)/2+np.min(ag)/2)#取均值


# 2. 矩阵计算


# 3. 随机生成100个标准正态的数据，并计算数据的均值与标准差