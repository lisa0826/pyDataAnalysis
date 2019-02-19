# -*- coding: utf-8 -*-

#1. 读入  肝气郁结证型系数.xls  数据集，将数据集按照等距、小组等量 两种方式 分别分为5组数据，分别计算5组数据的中位数与标准差
import pandas as pd

df1=pd.read_excel('肝气郁结证型系数.xls',header=None,skiprows=1)
df1.columns=['New_Values']

df1['new_dl']=pd.cut(df1['New_Values'],5,precision=2)
df1['new_dj']=pd.qcut(df1['New_Values'], 5, precision=2)
new_dl=df1['New_Values'].groupby(df1['new_dl'])
new_dj=df1['New_Values'].groupby(df1['new_dj'])
 
# print(new_dl.median())  #等距方式求中位数
# print(new_dl.std())  #等距方式求标准差
# print(new_dj.median())  #等距等量求中位数
# print(new_dj.std())  #等距等量求标准差

import pandas as pd

#1. 读入  肝气郁结证型系数.xls  数据集，将数据集按照等距、小组等量 两种方式 分别分为5组数据，分别计算5组数据的中位数与标准差
inputFile1 = '肝气郁结证型系数.xls'
data1 = pd.read_excel(inputfile1)

#2. 读入BHP1.csv，使用适当的方法填补缺失值
from scipy.interpolate import lagrange
###缺失值处理——拉格朗日插值法
inputfile = 'BHP1.csv' 
outputfile = 'NEWBHP1.csv' 

data = pd.read_csv(inputfile) 

def ployinterp_column(s, n, k=10):
  y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))] 
  y = y[y.notnull()]
  return lagrange(y.index, list(y))(n)

for i in data.columns:
  for j in range(len(data)):
    if (data[i].isnull())[j]: 
      data[i][j] = ployinterp_column(data[i], j)

# data.to_csv(outputfile)


#3. 读入BHP2.xlsx，与BHP1数据集合并为BHP数据集
df3_BHP1=pd.read_csv('BHP1.csv')
df3_BHP2=pd.read_excel('BHP2.xlsx')

df3_BHP=pd.merge(df3_BHP1, df3_BHP2, how='outer')

# print(df3_BHP)


#4. 将BHP数据集中的成交量（volume）替换为 high、median、low 三种水平（区间自行定义）

volume = df3_BHP['volume']
 
idx = 0
for i in volume:
    if i >= 2000000 and i < 3000000:
        df3_BHP['volume'][idx] = "median"
    elif i >= 3000000 :
        df3_BHP['volume'][idx] = "high"
    else: 
        df3_BHP['volume'][idx] = "low "
    idx+=1
    
print(df3_BHP)

