# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import sys
from pandas import Series, DataFrame


###pandas
#Series
obj = Series([4, 7, -5, 3])
# print(obj)
# print(obj.values)
# print(obj.index)

obj2 = Series([4,7,-5,3],index=['d','b','a','c'])
# print(obj2)
# print(obj2.index)
# print(obj2['a'])
# obj2['d'] = 6
# print(obj2[['c','a','d']])
# print(obj2[obj2 > 0])
# print(obj2 * 2)
# print(np.exp(obj2))
# print('b' in obj2)
# print('e' in obj2)

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
# print(obj3)

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
# print(obj4)

#dataframe
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
# print(frame)

frame2 = DataFrame(data,columns = ['year','state','pop','debt'],index = ['one','two','three','four','five'])
print(frame2)