# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 对macrodata.csv数据集
# 1. 画出realgdp列的直方图
# data1=pd.read_csv("macrodata.csv")
# data1x = data1['year']
# data1y = data1['realgdp']

# plt.bar(data1x, data1y, width=0.3, align='center', ecolor='r', color='cyan', label='data1 直方图')
# plt.show()

# 2. 画出realgdp列与realcons列的散点图，初步判断两个变量之间的关系
macro = pd.read_csv('macrodata.csv')
data2 = macro[['realgdp', 'realcons']]
trans_data = np.log(data).diff().dropna()
trans_data[-5:]

plt.figure()
plt.scatter(data2['realgdp'], data2['realcons'])
pd.scatter_matrix(data2, diagonal='kde', color='k', alpha=0.3)
plt.show()

# 对tips数据集
# 3. 画出不同sex与day的交叉表的柱形图

# 4. 画出size的饼图



#备注：代码运行用pythonw ****.py，This happens because python is not installed as a framework.