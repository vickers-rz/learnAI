import pandas as pd
import numpy as np


arrays = [
          np.array(['two', 'two', 'two', 'one',
              'one', 'one', 'two', 'one']),
          np.array(['qux', 'qux', 'foo', 'foo',
              'baz', 'baz', 'bar', 'bar']),
]

s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=arrays)
print(s)
# print(s.shape)
res = s.sort_index(level=0, ascending=True, sort_remaining=True, ignore_index=False)
# res = s.sort_index(level=2, ascending=True, sort_remaining=True, ignore_index=False)
"""
你的 arrays 创建了一个二级索引（MultiIndex）
但是 level 参数是从 0 开始计数的
对于二级索引，有效的 level 值只能是 0 或 1
"""
print(res)