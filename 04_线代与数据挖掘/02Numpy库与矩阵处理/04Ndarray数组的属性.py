# 查看Ndarray数组的形状
import numpy as np

# 一维数组
arr1 = np.array([1, 2, 3, 4, 5])
print("=== 一维数组形状 ===")
print("数组内容:", arr1)
print("数组形状:", arr1.shape)

# 二维数组
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n=== 二维数组形状 ===")
print("数组内容:")
print(arr2)
print("数组形状 (行数, 列数):", arr2.shape)

# 三维数组
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n=== 三维数组形状 ===")
print("数组内容:")
print(arr3)
print("数组形状 (层, 行, 列):", arr3.shape)

# 更高维度数组
arr4 = np.array([1, 2, 3, 4]).reshape(2, 2, 1)
print("\n=== reshape改变形状 ===")
print("原数组: [1, 2, 3, 4]")
print("reshape(2, 2, 1)后的内容:")
print(arr4)
print("数组形状:", arr4.shape)


# 查看Ndarray数组的数据类型

# 默认整型
arr1 = np.array([1, 2, 3])
print("\n\n=== 默认整型数组 ===")
print("数组内容:", arr1)
print("数组数据类型:", arr1.dtype)

# 指定为浮点型
arr2 = np.array([1, 2, 3], dtype=np.float64)
print("\n=== 浮点型数组 ===")
print("数组内容:", arr2)
print("数组数据类型:", arr2.dtype)

# 指定为复数型
arr3 = np.array([1+2j, 3+4j])
print("\n=== 复数型数组 ===")
print("数组内容:", arr3)
print("数组数据类型:", arr3.dtype)

# 指定为布尔型
arr4 = np.array([1, 0, 5, -1], dtype=bool)
print("\n=== 布尔型数组 ===")
print("原数组: [1, 0, 5, -1]")
print("转换为布尔型:", arr4)
print("数组数据类型:", arr4.dtype)

# 创建时指定数据类型
arr5 = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
print("\n=== 创建时指定数据类型 ===")
print("数组内容:")
print(arr5)
print("数组数据类型:", arr5.dtype)


# size:统计数组中有多少个元素

# 一维数组元素个数
arr1 = np.array([1, 2, 3, 4, 5])
print("\n\n=== 一维数组元素个数 ===")
print("数组内容:", arr1)
print("数组形状:", arr1.shape)
print("数组元素总数:", arr1.size)

# 二维数组元素个数
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n=== 二维数组元素个数 ===")
print("数组内容:")
print(arr2)
print("数组形状:", arr2.shape)
print("数组元素总数:", arr2.size)

# 三维数组元素个数
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n=== 三维数组元素个数 ===")
print("数组内容:")
print(arr3)
print("数组形状:", arr3.shape)
print("数组元素总数:", arr3.size)

# 使用arange创建数组并统计元素个数
arr4 = np.arange(1, 13).reshape(3, 4)
print("\n=== arange创建的数组元素个数 ===")
print("使用arange(1, 13).reshape(3, 4)创建数组:")
print(arr4)
print("数组形状:", arr4.shape)
print("数组元素总数:", arr4.size)


# ndim：查看数组的维度

# 0维数组（标量）
arr0 = np.array(42)
print("\n\n=== 0维数组 ===")
print("数组内容:", arr0)
print("数组形状:", arr0.shape)
print("数组维度数:", arr0.ndim)

# 一维数组
arr1 = np.array([1, 2, 3, 4, 5])
print("\n=== 一维数组 ===")
print("数组内容:", arr1)
print("数组形状:", arr1.shape)
print("数组维度数:", arr1.ndim)

# 二维数组
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n=== 二维数组 ===")
print("数组内容:")
print(arr2)
print("数组形状:", arr2.shape)
print("数组维度数:", arr2.ndim)

# 三维数组
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n=== 三维数组 ===")
print("数组内容:")
print(arr3)
print("数组形状:", arr3.shape)
print("数组维度数:", arr3.ndim)

# 四维数组
arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(2, 2, 2, 1)
print("\n=== 四维数组 ===")
print("原数组: [1, 2, 3, 4, 5, 6, 7, 8]")
print("reshape(2, 2, 2, 1)后的内容:")
print(arr4)
print("数组形状:", arr4.shape)
print("数组维度数:", arr4.ndim)