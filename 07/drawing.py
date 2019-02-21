# -*- coding:utf-8 -*-
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 对macrodata.csv数据集
# 1. 画出realgdp列的直方图
data1=pd.read_csv("macrodata.csv")
data1x = data1['year']
data1y = data1['realgdp']

plt.bar(data1x, data1y, width=0.3, align='center', ecolor='r', color='cyan', label='data1 直方图')
plt.show()

# 2. 画出realgdp列与realcons列的散点图，初步判断两个变量之间的关系
macro = pd.read_csv('macrodata.csv')
data2 = macro[['realgdp', 'realcons']]
trans_data = np.log(data2).diff().dropna()
trans_data[-5:]

plt.figure()
plt.scatter(trans_data['realgdp'], trans_data['realcons'])
pd.plotting.scatter_matrix(trans_data, diagonal='kde', color='k', alpha=0.3)
plt.show()

# 对tips数据集
# 3. 画出不同sex与day的交叉表的柱形图
data3 = pd.read_csv("tips.csv")
d_sd = pd.crosstab(data3['sex'], data3['day'])
d_sd.plot(kind="bar",stacked = False, alpha=0.7)
plt.show()

# 4. 画出size的饼图
data4 = pd.read_csv("tips.csv")
plt.figure(1, figsize=(8, 8))
ax = plt.axes([0.1, 0.1, 0.8, 0.8])
labels='1','2','3','4','5','6'
values=[]
for i in range(6):
	values.append(sum(data4['size']==i+1))
explode =[0.1, 0.1, 0.1, 0.1,0.1,0.1]
plt.pie(values, explode=explode, labels=labels,
 autopct='%1.1f%%', startangle=67)
plt.title('pie of size')
plt.show()


#备注：
#1、代码需分别注释运行，同事运行可能会出现图像重叠，影响看图
#2、代码运行用pythonw ****.py，This happens because python is not installed as a framework.