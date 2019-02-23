# -*- coding:utf-8 -*-
import numpy as np
from pandas import Series, DataFrame
import pandas as pd

### GroupBy 技术
df = DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                'key2' : ['one', 'two', 'one', 'two', 'one'],
                'data1' : np.random.randn(5),
                'data2' : np.random.randn(5)})
# print(df)

grouped = df['data1'].groupby(df['key1'])
print(grouped.mean())