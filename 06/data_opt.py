# -*- coding: utf-8 -*-

#1. 读入  肝气郁结证型系数.xls  数据集，将数据集按照等距、小组等量 两种方式 分别分为5组数据，分别计算5组数据的中位数与标准差
import pandas as pd

df1=pd.read_excel('肝气郁结证型系数.xls',header=None,skiprows=1)
df1.columns=['New_Values']

df1['new_dl']=pd.cut(df1['New_Values'],5,precision=2)
df1['new_dj']=pd.qcut(df1['New_Values'], 5, precision=2)
new_dl=df1['New_Values'].groupby(df1['new_dl'])
new_dj=df1['New_Values'].groupby(df1['new_dj'])
 
print(new_dl.median())  #等距方式求中位数
print(new_dl.std())  #等距方式求标准差
print(new_dj.median())  #等距等量求中位数
print(new_dj.std())  #等距等量求标准差

#2. 读入BHP1.csv，使用适当的方法填补缺失值


#3. 读入BHP2.xlsx，与BHP1数据集合并为BHP数据集

#4. 将BHP数据集中的成交量（volume）替换为 high、median、low 三种水平（区间自行定义）