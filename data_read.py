# -*- coding:utf-8 -*
import numpy as np 
import xlrd
import pandas as pd 
import sys
from pandas import Series, DataFrame

#读入课程资源中作业数据的所有数据集
dataAs = pd.read_excel('05/ApplianceShipments.xls') 

list(open('05/creditcard-dataset.txt'))
dataCd = pd.read_table('05/creditcard-dataset.txt',sep='\s+')

print(dataAs)
# print(dataCd)