import numpy as np

print("=== 什么是视图(View)和副本(Copy) ===\n")

# 创建一个原始数组
original = np.array([[1, 2, 3], 
                     [4, 5, 6]])
print("1. 原始数组:")
print("original =", original)
print("original 的内存地址:", original.ctypes.data)
print()

# 创建视图 (View) - 与原数组共享内存
view_array = original.view()
print("2. 创建视图 (view):")
print("view_array =", view_array)
print("view_array 的内存地址:", view_array.ctypes.data)
print("是否共享内存:", np.shares_memory(original, view_array))
print()

# 修改视图
view_array[0, 0] = 999
print("3. 修改视图的第一个元素为 999 后:")
print("view_array =", view_array)
print("original =", original)  # 原数组也被修改了！
print()

# 创建副本 (Copy) - 独立的数组
original2 = np.array([[1, 2, 3], 
                      [4, 5, 6]])
copy_array = original2.copy()
print("4. 创建副本 (copy):")
print("original2 =", original2)
print("copy_array =", copy_array)
print("original2 的内存地址:", original2.ctypes.data)
print("copy_array 的内存地址:", copy_array.ctypes.data)
print("是否共享内存:", np.shares_memory(original2, copy_array))
print()

# 修改副本
copy_array[0, 0] = 888
print("5. 修改副本的第一个元素为 888 后:")
print("copy_array =", copy_array)
print("original2 =", original2)  # 原数组没有被修改
print()

# 演示 flatten 和 ravel 的区别
print("=" * 50)
print("6. flatten vs ravel 的视图/副本区别:\n")

arr = np.array([[1, 2], [3, 4]])
print("原始数组 arr:")
print(arr)
print()

# flatten 总是返回副本
flattened = arr.flatten()
print("flattened = arr.flatten() 的结果:")
print("flattened =", flattened)
print("是否共享内存:", np.shares_memory(arr, flattened))  # False
print()

# ravel 返回视图（如果可能）
raveled = arr.ravel()
print("raveled = arr.ravel() 的结果:")
print("raveled =", raveled)
print("是否共享内存:", np.shares_memory(arr, raveled))    # True
print()

# 修改 ravel 返回的结果
raveled[0] = 777
print("修改 raveled[0] = 777 后:")
print("raveled =", raveled)
print("arr =", arr)  # 原数组也被修改了！
print()

"""
关于视图(View)和副本(Copy)的详细解释:

什么是视图(View)?
----------------
视图是原始数据的一个"窗口"，它不拥有自己的数据，而是与原始数组共享同一块内存。
- 修改视图会影响原始数组
- 视图操作速度快，内存占用少
- 使用 np.shares_memory() 可以检查两个数组是否共享内存

什么是副本(Copy)?
----------------
副本是原始数据的一个完整拷贝，它拥有独立的数据存储空间。
- 修改副本不会影响原始数组
- 副本操作速度相对较慢，需要额外内存
- 副本与原始数组完全独立

视图和副本的比喻:
---------------
可以把原始数组想象成一张纸上的内容：

视图就像是在这张纸上放了一块透明的玻璃，你在玻璃上看到的内容和纸上的内容是一样的。
如果你在玻璃上做标记，纸上的内容并不会改变，但如果你移动玻璃的位置或者改变玻璃的形状
（比如旋转、翻转），你看到的纸上的内容也会相应改变。

副本就像是用另一张纸把原始内容完整地抄写了一遍。这两张纸是完全独立的，修改其中一张
不会影响另一张。

在 flatten 和 ravel 中的应用:
--------------------------
flatten() 方法总是创建副本，就像把内容抄写到新纸上一样，安全但耗费资源。

ravel() 方法尽可能创建视图，就像放一块透明玻璃一样，高效但需要注意会相互影响。

什么时候返回视图，什么时候返回副本?
-----------------------------
ravel() 尽可能返回视图，但在以下情况会返回副本：
1. 数组在内存中不连续
2. 数组经过复杂的切片操作
3. 数组的数据类型需要转换

实际应用建议:
-----------
1. 如果需要确保不影响原始数据，使用 copy() 或 flatten()
2. 如果关注性能且可以接受数据关联，使用 view() 或 ravel()
3. 使用 np.shares_memory() 检查两个数组是否共享内存

视图概念详细解释:
---------------

正如我们在上面的代码示例中看到的，当你创建一个视图时，实际上并没有创建新的数据存储空间。
相反，视图只是提供了对现有数据的不同"看法"。这有几个重要含义：

1. 内存效率：视图不需要额外的内存来存储数据，因为它们与原始数组共享内存。

2. 性能优势：创建视图非常快，因为它只需要创建一个新的数组头部信息，而不是复制所有数据。

3. 数据同步：由于视图和原始数组共享相同的数据，对其中一个的任何修改都会反映在另一个上。

4. 独立元数据：虽然视图共享数据，但它们有自己的形状(shape)、步长(strides)等元数据信息。

这与副本形成鲜明对比，副本会创建完整的数据副本，完全独立于原始数组。

视图的实际应用场景:
------------------
1. 数组切片：当你对数组进行切片操作时，通常会得到一个视图而不是副本
2. 数据重塑：某些重塑操作可能会返回视图以提高效率
3. 数据类型转换：在某些情况下，类型转换也可能产生视图
4. 转置操作：数组的转置通常返回视图

理解视图和副本之间的区别对于编写高效且无错误的NumPy代码至关重要。
"""