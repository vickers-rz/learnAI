# =============================================
# NumPy 维度变换演示：squeeze（降维）与 expand_dims（升维）
# =============================================

import numpy as np

# -----------------------------
# 一、np.squeeze：去除长度为 1 的维度
# -----------------------------

# 创建一个三维数组，形状为 (1, 3, 1)
arr = np.array([[[1], [2], [3]]])
print("=== 原始数组 ===")
print(arr)
print("原始数组形状:", arr.shape)   # (1, 3, 1)

# 1️⃣ 不指定 axis：自动去掉所有长度为 1 的维度
squeezed_all = np.squeeze(arr)
print("\n--- squeeze 无 axis 参数 ---")
print(squeezed_all)
print("形状:", squeezed_all.shape)   # (3,)

# 2️⃣ 指定单个轴：只去掉第 0 维（前面的 1）
squeezed_axis0 = np.squeeze(arr, axis=0)
print("\n--- squeeze axis=0 ---")
print(squeezed_axis0)
print("形状:", squeezed_axis0.shape) # (3, 1)

# 3️⃣ 指定多个轴：去掉第 0 和第 2 维（两边的 1）
squeezed_axis_multi = np.squeeze(arr, axis=(0, 2))
print("\n--- squeeze axis=(0, 2) ---")
print(squeezed_axis_multi)
print("形状:", squeezed_axis_multi.shape) # (3,)

# ✅ 说明：
# - np.squeeze(arr)           → 去掉所有长度为 1 的维度
# - np.squeeze(arr, axis=0)   → 只去掉第 0 个轴
# - np.squeeze(arr, axis=(0,2)) → 同时去掉第 0 和第 2 个轴
# 注意：如果指定的轴不是长度为 1，会报 ValueError


# -----------------------------
# 二、np.expand_dims：增加一个或多个维度
# -----------------------------

# 创建一个二维数组，形状为 (2, 3)
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\n=== 原始数组 ===")
print(arr2)
print("原始数组形状:", arr2.shape)  # (2, 3)

# 1️⃣ 在最前面增加一个维度
expanded_axis0 = np.expand_dims(arr2, axis=0)
print("\n--- expand_dims axis=0 ---")
print(expanded_axis0)
print("形状:", expanded_axis0.shape) # (1, 2, 3)

# 2️⃣ 在中间（第 1 个位置）增加一个维度
expanded_axis1 = np.expand_dims(arr2, axis=1)
print("\n--- expand_dims axis=1 ---")
print(expanded_axis1)
print("形状:", expanded_axis1.shape) # (2, 1, 3)

# 3️⃣ 同时在多个位置增加维度
expanded_axis_multi = np.expand_dims(arr2, axis=(0, 1))
print("\n--- expand_dims axis=(0, 1) ---")
print(expanded_axis_multi)
print("形状:", expanded_axis_multi.shape) # (1, 1, 2, 3)

# ✅ 说明：
# - axis 指定的是「插入后新维度的位置」
# - 可为单个 int 或多个位置的 tuple
# - 新增维度的长度永远为 1
# - axis 的取值范围基于结果数组的维度（可以用负数）


# -----------------------------
# 三、总结对比
# -----------------------------
"""
np.squeeze(arr) 的前提条件：
1. 只能移除长度为1的维度
2. 可以指定特定轴进行移除，但该轴的长度必须为1
3. 不指定轴时，默认移除所有长度为1的维度

np.expand_dims(arr, axis) 的前提条件：
1. 指定的轴位置必须合法（在原数组维度范围内）
2. axis可以指定单个轴或多个轴
3. 在指定位置插入新维度，新增维度的长度始终为1
- 用于显式控制数组形状以适配广播或网络输入
"""
