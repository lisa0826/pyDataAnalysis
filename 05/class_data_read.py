# -*- coding:utf-8 -*
import pandas as pd 

# resultTxt = pd.read_table('creditcard-dataset.txt',sep='\s+')
# # print(resultTxt)

# resultCsv= pd.read_csv('DressSales.csv',sep='\s+')
# # print(resultCsv)

# import csv
# f = open('DressSales.csv')
# reader = csv.reader(f)

# 	for line in reader:
# 		# print(line)

#使用数据库
# from pandas import Series, DataFrame
# import sqlite3

# query = """
# CREATE TABLE test
# (a VARCHAR(20), b VARCHAR(20),
#  c REAL,        d INTEGER
# );"""

# con = sqlite3.connect(':memory:')
# con.execute(query)
# con.commit()

# data = [('Atlanta', 'Georgia', 1.25, 6),
#         ('Tallahassee', 'Florida', 2.6, 3),
#         ('Sacramento', 'California', 1.7, 5)]
# stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

# con.executemany(stmt, data)
# con.commit()

# cursor = con.execute('select * from test')
# rows = cursor.fetchall()
# rows

# cursor.description

# DataFrame(rows, columns=list(zip(*cursor.description)[0]))

import pandas.io.sql as sql
print(sql.read_sql('select * from test', con))

