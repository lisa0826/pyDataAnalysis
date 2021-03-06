# -*- coding: utf-8 -*-
import numpy as np

# 1. 读入ag0613.csv数据集，并计算数据的最大值、最小值、均值、标准差、中位数
ag = np.loadtxt('ag0613.csv',skiprows=1)
	
print(ag)#打印所有取出的值
print("maxAg = ", np.max(ag))#取最大值
print("minAg = ", np.min(ag))#取最小值
print("meanAg = ", np.max(ag)/2+np.min(ag)/2)#取均值
print("stdAg = ", np.std(ag))#取标准差，axis=0计算每一列的标准差
print("medianAg = ", np.median(ag))#取中位数


# 2. 矩阵计算
a = [[1,2],[3,4]]
b = [[2,5],[1,3]]
c = np.multiply(a, b)
print(c)

# 3. 随机生成100个标准正态的数据，并计算数据的均值与标准差
import matplotlib  
matplotlib.use('TkAgg')   
import matplotlib.pyplot as plt

mu = 1  #期望为1
sigma = 3  #标准差为3
num = 100  #个数为10000

rand_data = np.random.normal(mu, sigma, num)

print("mean =", np.mean(rand_data))
print("standard error =", np.std(rand_data))

#RuntimeError: Python is not installed as a framework. The Mac OS X backend will not be able to function correctly if Python is not installed as a framework. See the Python documentation for more information on installing Python as a framework on Mac OS X. Please either reinstall Python as a framework, or try one of the other backends.
#以上报错的解决办法地址https://github.com/tensorflow/tensorflow/issues/2375
#解决代码：
#import matplotlib  
#matplotlib.use('TkAgg')   
#import matplotlib.pyplot as plt
