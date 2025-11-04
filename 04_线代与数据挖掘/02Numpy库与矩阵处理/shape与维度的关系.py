"""
详细解释NumPy数组的shape属性如何反映数组的维度

Shape属性是一个元组(tuple)，其中每个元素表示对应维度的大小。
维度的数量等于shape元组的长度，也就是ndim属性的值。
"""

import numpy as np

# 0维数组（标量） - 零维数组没有形状维度
print("=== 0维数组（标量）===")
arr0 = np.array(42)
print("数组内容:", arr0)
print("数组形状:", arr0.shape)  # 空元组()
print("数组维度数:", arr0.ndim)  # 0
print("解释: 标量没有维度，所以shape是空元组")

# 一维数组 - shape元组只有一个元素
print("\n=== 一维数组 ===")
arr1 = np.array([1, 2, 3, 4, 5])
print("数组内容:", arr1)
print("数组形状:", arr1.shape)  # (5,) 表示有5个元素
print("数组维度数:", arr1.ndim)  # 1
print("解释: 一维数组的shape元组只有一个元素，表示该维度上的元素个数")

# 二维数组 - shape元组有两个元素
print("\n=== 二维数组 ===")
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("数组内容:")
print(arr2)
print("数组形状:", arr2.shape)  # (2, 3) 表示2行3列
print("数组维度数:", arr2.ndim)  # 2
print("解释: 二维数组的shape元组有两个元素，分别表示第0维和第1维的大小")
print("      第0维(行数): 2, 第1维(列数): 3")

# 三维数组 - shape元组有三个元素
print("\n=== 三维数组 ===")
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("数组内容:")
print(arr3)
print("数组形状:", arr3.shape)  # (2, 2, 2) 表示2个2x2的矩阵
print("数组维度数:", arr3.ndim)  # 3
print("解释: 三维数组的shape元组有三个元素，分别表示第0、1、2维的大小")
print("      第0维(层数): 2, 第1维(行数): 2, 第2维(列数): 2")

# 四维数组 - shape元组有四个元素
print("\n=== 四维数组 ===")
arr4 = np.arange(24).reshape(2, 3, 2, 2)
print("数组内容:")
print(arr4)
print("数组形状:", arr4.shape)  # (2, 3, 2, 2)
print("数组维度数:", arr4.ndim)  # 4
print("解释: 四维数组的shape元组有四个元素，分别表示第0、1、2、3维的大小")
print("      第0维: 2, 第1维: 3, 第2维: 2, 第3维: 2")

# 特殊情况：不规则形状的数组（使用object类型）
print("\n=== 特殊情况：不规则数组 ===")
arr5 = np.array([[1, 2, 3], [4, 5]], dtype=object)
print("数组内容:", arr5)
print("数组形状:", arr5.shape)  # (2,) 只能表示外层维度
print("数组维度数:", arr5.ndim)  # 1
print("解释: 对于不规则数组，NumPy会将其视为object数组，shape只能反映外层维度")

# 总结说明
print("\n" + "="*50)
print("总结: shape属性与维度的关系")
print("="*50)
print("1. shape是一个元组，其长度等于数组的维度数(ndim)")
print("2. shape元组中的每个元素表示对应维度的大小")
print("3. 第0维通常表示最外层结构的大小")
print("4. 对于n维数组，shape元组就有n个元素")
print("5. shape元组中第i个元素表示第i维的大小")