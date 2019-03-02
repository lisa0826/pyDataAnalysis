# -*- coding: utf-8 -*-
import numpy as np
from pandas import Series, DataFrame
import pandas as pd

# 读入tips.csv 数据集
dataTip=pd.read_csv("tips.csv")

# 1. 统计不同time的tip的均值，方差
grouped_time = dataTip.groupby(['time'])

def peak_to_peak(arr):
    return arr.max() - arr.min()
grouped_time.agg(peak_to_peak)

# print(grouped_time.agg('mean')['tip'])
print(grouped_time.agg(['mean', 'std'])['tip'])

# 2. 将total_bill和tip根据不同的sex进行标准化(原数据减去均值的结果除以标准差)
dataTip['tip_pct'] = dataTip['tip'] / dataTip['total_bill']
dataTip[:6]
grouped = dataTip.groupby(['sex'])
grouped_pct = grouped['tip_pct']
# print(grouped_pct.agg('mean'))

# 3. 计算吸烟者和非吸烟者的小费比例值均值  的差值

# 4. 对sex与size聚合，统计不同分组的小费比例的标准差、均值，将该标准差与均值添加到原数据中

# 5. 对time和size聚合，画出total_bill 的饼图