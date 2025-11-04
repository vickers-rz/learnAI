import numpy as np

# ==========================================
# 演示目的：比较 numpy 中 flatten() 和 ravel() 方法的区别
# ==========================================

# 创建一个连续的C-style数组（行优先存储）
# order='C' 表示按照C语言的风格存储数组元素（行优先）
arr_c = np.array([[1, 2, 3], [4, 5, 6]], order='C')

# 创建一个非连续的Fortran-style数组（列优先存储）
# order='F' 表示按照Fortran语言的风格存储数组元素（列优先）
arr_f = np.array([[1, 2, 3], [4, 5, 6]], order='F')

print("=== 原始数组信息 ===")
print("C-style数组 (行优先):")
print(arr_c)
print("Fortran-style数组 (列优先):")
print(arr_f)

# 演示 flatten 方法 - 总是返回一个副本（copy）
# flatten() 方法不管原始数组的存储方式如何，都会创建一个新的数组
flatten_c = arr_c.flatten()  # 对C-style数组使用flatten
flatten_f = arr_f.flatten()  # 对Fortran-style数组使用flatten

# 演示 ravel 方法 - 尽可能返回一个视图（view）
# ravel() 方法会尽可能返回原始数组的视图，只有在必要时才创建副本
ravel_c = arr_c.ravel()  # 对C-style数组使用ravel
ravel_f = arr_f.ravel()  # 对Fortran-style数组使用ravel

print("\n=== flatten() 和 ravel() 返回结果 ===")
print("C-style数组flatten结果:")
print(flatten_c)
print("C-style数组ravel结果:")
print(ravel_c)
print("Fortran-style数组flatten结果:")
print(flatten_f)
print("Fortran-style数组ravel结果:")
print(ravel_f)

# 检查内存共享情况
print("\n=== 内存共享检查 ===")
print("flatten_c 与 arr_c 是否共享内存:", np.shares_memory(flatten_c, arr_c))
print("ravel_c 与 arr_c 是否共享内存:", np.shares_memory(ravel_c, arr_c))
print("flatten_f 与 arr_f 是否共享内存:", np.shares_memory(flatten_f, arr_f))
print("ravel_f 与 arr_f 是否共享内存:", np.shares_memory(ravel_f, arr_f))

# 修改数组，观察是否影响原数组
print("\n=== 修改返回数组后观察对原数组的影响 ===")

# 修改flatten返回的数组，不会影响原始数组，因为flatten返回的是副本
print("修改flatten_c[0]前的arr_c[0, 0]:", arr_c[0, 0])
flatten_c[0] = 999  # 修改 flatten 返回的副本
print("修改flatten_c[0]后的arr_c[0, 0]:", arr_c[0, 0])

# 修改ravel返回的数组，可能会影响原始数组，因为ravel可能返回视图
print("修改ravel_c[0]前的arr_c[0, 0]:", arr_c[0, 0])
ravel_c[0] = 999  # 修改 ravel 返回的视图
print("修改ravel_c[0]后的arr_c[0, 0]:", arr_c[0, 0])

# 输出结果
print("\n=== 最终结果 ===")
print("Original C-style array:", arr_c)
print("Flatten C:", flatten_c)
print("Ravel C:", ravel_c)
print("Original Fortran-style array:", arr_f)
print("Flatten F:", flatten_f)
print("Ravel F:", ravel_f)

# 额外演示：对数组进行切片后再使用ravel
print("\n=== 额外演示：切片后的ravel行为 ===")
arr_slice = arr_c[:, 1:]  # 取每行的后两列
print("切片数组:")
print(arr_slice)

# 检查切片数组与原数组的内存共享情况
print("切片数组与原数组是否共享内存:", np.shares_memory(arr_slice, arr_c))

# 切片后的数组使用ravel
ravel_slice = arr_slice.ravel()
print("切片数组ravel结果:")
print(ravel_slice)

# 检查切片ravel结果与原数组的内存共享情况
print("切片ravel结果与原数组是否共享内存:", np.shares_memory(ravel_slice, arr_c))

# 修改切片ravel结果
print("修改ravel_slice前的arr_slice[0, 0]:", arr_slice[0, 0])
print("修改ravel_slice前的arr_c[0, 1]:", arr_c[0, 1])
ravel_slice[0] = 888
print("修改ravel_slice后的arr_slice[0, 0]:", arr_slice[0, 0])
print("修改ravel_slice后的arr_c[0, 1]:", arr_c[0, 1])

# ==========================================
# 总结：flatten() 与 ravel() 的主要区别
# ==========================================
"""
主要区别总结：

1. 返回类型：
   - flatten() 总是返回一个副本（copy）
   - ravel() 尽可能返回一个视图（view），只有在必要时才返回副本

2. 内存效率：
   - flatten() 总是创建新的内存空间，占用更多内存
   - ravel() 尽可能与原数组共享内存，更节省内存

3. 性能：
   - flatten() 由于需要复制数据，性能相对较低
   - ravel() 由于尽可能避免复制数据，性能相对较高

4. 数据安全性：
   - flatten() 返回的副本与原数组完全独立，修改不会影响原数组
   - ravel() 返回的视图与原数组共享数据，修改可能会影响原数组

5. 使用场景：
   - 如果需要确保修改返回的数组不影响原数组，使用 flatten()
   - 如果关注性能且可以接受数据关联，使用 ravel()
   - 可以使用 np.shares_memory() 函数检查两个数组是否共享内存

==========================================
关于本代码的详细解释：
==========================================

该代码主要演示了NumPy中两个用于将多维数组展平为一维数组的函数的区别：flatten()和ravel()。

主要区别：

1. 返回类型不同：
   - flatten()总是返回一个副本（copy）
   - ravel()尽可能返回一个视图（view），只有在必要时才返回副本

2. 内存使用差异：
   - flatten()总是创建新的内存空间
   - ravel()尽可能与原数组共享内存空间

3. 性能差异：
   - flatten()由于需要复制数据，性能相对较低
   - ravel()由于尽可能避免复制数据，性能相对较高

4. 数据安全性：
   - flatten()返回的副本与原数组完全独立，修改不会影响原数组
   - ravel()返回的视图与原数组共享数据，修改可能会影响原数组

代码中添加的详细说明：

1. 添加了详细的中文注释，解释了每个代码段的功能
2. 增加了内存共享检查，使用np.shares_memory()函数来检测数组之间是否共享内存
3. 添加了对切片数组使用ravel的示例，展示更复杂的情况
4. 在文件末尾添加了总结性注释，详细解释了两个函数的主要区别和使用场景

代码运行结果说明：

通过代码可以观察到：
- 修改flatten()返回的数组不会影响原始数组
- 修改ravel()返回的数组可能会影响原始数组（取决于是否返回视图）
- 通过np.shares_memory()可以准确判断两个数组是否共享内存

使用建议：

- 如果需要确保修改返回的数组不影响原数组，使用flatten()
- 如果关注性能且可以接受数据关联，使用ravel()
- 可以使用np.shares_memory()函数检查两个数组是否共享内存
"""