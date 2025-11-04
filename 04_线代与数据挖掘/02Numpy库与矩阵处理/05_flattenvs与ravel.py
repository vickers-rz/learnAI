import numpy as np

print("=== 演示 flatten 和 ravel 的区别 ===")

# 创建一个二维数组
arr = np.array([[1, 2, 3], 
                [4, 5, 6]])

print("原始数组:")
print(arr)
print()

# 使用 flatten 方法
flattened = arr.flatten()
print("使用 flatten() 方法返回的数组:")
print(flattened)
print()

# 修改 flatten 返回的数组
flattened[0] = 999
print("修改 flatten 返回的数组后:")
print("flatten 返回的数组:", flattened)
print("原始数组:", arr)
print("可以看到，原始数组没有受到影响")
print()

# 重新创建数组进行 ravel 测试
arr2 = np.array([[1, 2, 3], 
                 [4, 5, 6]])
print("=" * 40)
print("使用 ravel() 方法:")
raveled = arr2.ravel()
print("ravel 返回的数组:", raveled)
print()

# 修改 ravel 返回的数组
raveled[0] = 888
print("修改 ravel 返回的数组后:")
print("ravel 返回的数组:", raveled)
print("原始数组:", arr2)
print("可以看到，原始数组也被修改了，因为 ravel 返回的是视图")
print()

# 检查数组是否共享内存
print("=" * 40)
print("验证内存共享:")

arr3 = np.array([[1, 2, 3], 
                 [4, 5, 6]])

flatten_copy = arr3.flatten()
ravel_view = arr3.ravel()

print("flatten 返回的数组与原数组是否共享内存:", np.shares_memory(arr3, flatten_copy))  # False
print("ravel 返回的数组与原数组是否共享内存:", np.shares_memory(arr3, ravel_view))      # True
print()

# 展示不同 order 参数的影响
print("=" * 40)
print("ravel 不同 order 参数的效果:")

arr4 = np.array([[1, 2, 3], 
                 [4, 5, 6]])

print("原数组:")
print(arr4)
print("默认顺序 (C-order):", arr4.ravel())
print("Fortran顺序 (F-order):", arr4.ravel(order='F'))
print("保持原数组顺序 (A-order):", arr4.ravel(order='A'))
print("按内存顺序 (K-order):", arr4.ravel(order='K'))

"""
详细解释和总结:

flatten vs ravel 方法详解
=========================

这两个方法都可以将多维数组展平为一维数组，但它们在行为上有一个关键区别：内存管理方式。

主要区别
--------

1. **flatten()** 总是返回原数组的一个**副本**
2. **ravel()** 尽可能返回原数组的一个**视图**

flatten() 方法
-------------

- 总是创建一个新的数组（副本）
- 新数组与原数组在内存中完全独立
- 修改新数组不会影响原数组
- 内存开销较大，因为需要复制所有数据

ravel() 方法
------------

- 尽可能返回原数组的视图（view）
- 视图与原数组共享内存
- 修改视图会直接影响原数组
- 更节省内存，效率更高
- 只有在必要时才创建副本

ravel() 的 order 参数
-------------------

ravel() 方法支持不同的内存布局参数：
- `order='C'`: C风格（行优先）排序
- `order='F'`: Fortran风格（列优先）排序
- `order='A'`: 如果数组在内存中是Fortran连续的，则使用列优先，否则使用行优先
- `order='K'`: 按照元素在内存中的实际存储顺序排列

实际应用建议
----------

1. 如果需要确保不影响原数组，使用 `flatten()`
2. 如果关注性能且不需要保留原数组不变，使用 `ravel()`
3. 当处理大型数组时，`ravel()` 更节省内存
4. 在需要特定内存布局时，使用 `ravel()` 的 order 参数

这种设计体现了NumPy在性能和安全性之间的平衡考虑：`flatten()` 提供安全的副本操作，
而 `ravel()` 提供高效的视图操作。
"""