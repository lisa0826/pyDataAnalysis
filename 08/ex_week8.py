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
# print(grouped.mean())

means1 = df['data1'].groupby([df['key1'], df['key2']]).mean()
means2 = df['data1'].groupby(df['key2']).mean()
# print(means1)
# print(means2)
# print(means1.unstack())

states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
df['data1'].groupby([states, years]).mean()

# print(df.groupby('key1').mean())
# print(df.groupby(['key1', 'key2']).mean())
# print(df.groupby(['key1', 'key2']).size())

def peak_to_peak(arr):
    return arr.max() - arr.min()
grouped.agg(peak_to_peak)

# ### 面向列的多函数应用
tips = pd.read_csv('tips.csv')

tips['tip_pct'] = tips['tip'] / tips['total_bill']
tips[:6]

grouped = tips.groupby(['sex', 'smoker'])
grouped_pct = grouped['tip_pct']
# print(grouped_pct.agg('mean'))

# print(grouped_pct.agg(['mean', 'std', peak_to_peak]))

# print(grouped_pct.agg([('foo', 'mean'), ('bar', np.std)]))

functions = ['count', 'mean', 'max']
result = grouped['tip_pct', 'total_bill'].agg(functions)
# print(result)

result['tip_pct']

ftuples = [('Durchschnitt', 'mean'), ('Abweichung', np.var)]
grouped['tip_pct', 'total_bill'].agg(ftuples)

grouped.agg({'tip' : np.max, 'size' : 'sum'})

grouped.agg({'tip_pct' : ['min', 'max', 'mean', 'std'],
             'size' : 'sum'})

# ##数据聚合
df

grouped1 = df.groupby('key1')
grouped1['data1']

def peak_to_peak(arr):
    return arr.max() - arr.min()
grouped1.agg(peak_to_peak)
print(grouped1.describe())