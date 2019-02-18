# -*- coding:utf-8 -*

###读入课程资源中作业数据的所有数据集
#读取excel
import xlrd
from os.path import  join,abspath,dirname

fname = join(dirname(dirname(abspath(__file__))),'05/ApplianceShipments.xls')
bk = xlrd.open_workbook(fname, encoding_override="utf-8")
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("Data")
    # 获取行数
    nrows = sh.nrows
    # 获取列数
    ncols = sh.ncols
    print("nrows %d, ncols %d" % (nrows, ncols))
    # 获取第一行第一列数据
    cell_value = sh.cell_value(1, 1)
    # print(cell_value)

    row_list = []
    # 获取各行数据
    for i in range(0, nrows):
        row_data = sh.row_values(i)
        row_list.append(row_data)

    print(row_list)
except:
    print("no sheet in %s named Sheet1" % fname)

#读取txt
dataCd = open('../05/creditcard-dataset.txt',encoding="utf-8").read()
dataCd = pd.read_table('../05/creditcard-dataset.txt')
print(dataCd)

#读取csv
import pandas as pd 

dataDs = pd.read_csv('../05/DressSales.csv')
print(dataDs)


#思考：
#1、是否应该写多个function，一次性批量读取所有数据

