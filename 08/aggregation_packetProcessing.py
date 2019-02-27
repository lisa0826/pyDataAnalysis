# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# 读入tips.csv 数据集
data=pd.read_csv("tips.csv")

dataTip = data['tip']

# 1. 统计不同time的tip的均值，方差
print(np.mean(dataTip))
print(np.var(dataTip))

# 2. 将total_bill和tip根据不同的sex进行标准化(原数据减去均值的结果除以标准差)
dataTip = data['sex']

# 3. 计算吸烟者和非吸烟者的小费比例值均值  的差值

# 4. 对sex与size聚合，统计不同分组的小费比例的标准差、均值，将该标准差与均值添加到原数据中

# 5. 对time和size聚合，画出total_bill 的饼图