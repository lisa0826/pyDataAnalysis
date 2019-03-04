# -*- coding: utf-8 -*-
import numpy as np
from pandas import Series, DataFrame
import pandas as pd

# 读入tips.csv 数据集
dataTip=pd.read_csv("tips.csv")

# 1. 统计不同time的tip的均值，方差
grouped_time = dataTip.groupby(['time'])

# print(grouped_time.agg('mean')['tip'])
# print(grouped_time.agg(['mean', 'std'])['tip'])


# 2. 将total_bill和tip根据不同的sex进行标准化(原数据减去均值的结果除以标准差)
grouped_sex = dataTip.groupby(['sex'])
means = grouped_sex.mean()
stds = grouped_sex.std() 
# print(means,'\n',stds)


# 3. 计算吸烟者和非吸烟者的小费比例值均值  的差值
dataTip['tip_pct'] = dataTip['tip'] / dataTip['total_bill']
grouped_is_smoker = dataTip.groupby(['smoker'])[['tip_pct']]
result = grouped_is_smoker.mean()
# print(result)

def peak_to_peak(arr):
    return arr.max() - arr.min()

# print(result.agg([peak_to_peak]))


# 4. 对sex与size聚合，统计不同分组的小费比例的标准差、均值，将该标准差与均值添加到原数据中
getData = dataTip.groupby(['sex','size'])['tip_pct'].agg(['mean','std'])
print(dataTip,'/n',getData)
newData = DataFrame({dataTip,gatData})
print(newData)

# 5. 对time和size聚合，画出total_bill 的饼图

