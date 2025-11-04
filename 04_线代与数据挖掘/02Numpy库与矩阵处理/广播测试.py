import numpy as np

def explain_right_alignment(shape1, shape2):
    """
    解释"向右对齐"的概念
    """
    print(f"\n--- '向右对齐'演示 ---")
    print(f"数组A的形状: {shape1}")
    print(f"数组B的形状: {shape2}")
    
    max_len = max(len(shape1), len(shape2))
    
    # 向右对齐显示
    print("\n向右对齐的形状比较:")
    padded_shape1 = (None,) * (max_len - len(shape1)) + shape1
    padded_shape2 = (None,) * (max_len - len(shape2)) + shape2
    
    print("数组A: ", end="")
    for dim in padded_shape1:
        if dim is None:
            print("(补1) ", end="")
        else:
            print(f"{dim:4} ", end="")
    print()
    
    print("数组B: ", end="")
    for dim in padded_shape2:
        if dim is None:
            print("(补1) ", end="")
        else:
            print(f"{dim:4} ", end="")
    print()
    
    # 检查是否可以广播
    print("\n广播兼容性检查:")
    compatible = True
    for i, (dim1, dim2) in enumerate(zip(padded_shape1, padded_shape2)):
        d1 = 1 if dim1 is None else dim1
        d2 = 1 if dim2 is None else dim2
        if d1 == d2 or d1 == 1 or d2 == 1:
            print(f"  轴{i}: {d1} 和 {d2} -> 兼容")
        else:
            print(f"  轴{i}: {d1} 和 {d2} -> 不兼容!")
            compatible = False
    
    if compatible:
        result_shape = tuple(
            max(1 if d1 is None else d1, 1 if d2 is None else d2) 
            for d1, d2 in zip(padded_shape1, padded_shape2)
        )
        print(f"广播结果形状: {result_shape}")
    else:
        print("无法广播!")
    
    return compatible

print("NumPy广播机制 - '向右对齐'详解")
print("=" * 40)

# 示例1: 标量与一维数组
print("\n【示例1】标量 (形状 ()) 与 一维数组 (形状 (3,))")
a = 5  # 标量，形状 ()
b = np.array([1, 2, 3])  # 一维数组，形状 (3,)

print("理解'向右对齐':")
print("想象两个形状从右边开始对齐:")
print("  标量形状:      ()")
print("  一维数组形状:     (3,)")
print("           -----> 对齐方向")
print("为了便于比较，我们在形状较短的一方左边补1:")
print("  标量形状补1后:   (1,)")
print("  一维数组形状:    (3,)")

explain_right_alignment((), (3,))

# 示例2: 一维数组与二维数组
print("\n\n【示例2】一维数组 (形状 (3,)) 与 二维数组 (形状 (2, 3))")
c = np.array([1, 2, 3])        # 一维数组，形状 (3,)
d = np.array([[1, 2, 3], 
              [4, 5, 6]])      # 二维数组，形状 (2, 3)

print("理解'向右对齐':")
print("想象两个形状从右边开始对齐:")
print("  一维数组形状:     (3,)")
print("  二维数组形状:  (2, 3)")
print("             -----> 对齐方向")
print("为了便于比较，我们在形状较短的一方左边补1:")
print("  一维数组形状补1后:(1, 3)")
print("  二维数组形状:   (2, 3)")

explain_right_alignment((3,), (2, 3))

# 示例3: 二维数组与三维数组
print("\n\n【示例3】二维数组 (形状 (1, 4)) 与 三维数组 (形状 (2, 3, 4))")
e = np.array([[1, 2, 3, 4]])     # 二维数组，形状 (1, 4)
f = np.arange(24).reshape(2, 3, 4)  # 三维数组，形状 (2, 3, 4)

print("理解'向右对齐':")
print("想象两个形状从右边开始对齐:")
print("  二维数组形状:     (1, 4)")
print("  三维数组形状:  (2, 3, 4)")
print("                -----> 对齐方向")
print("为了便于比较，我们在形状较短的一方左边补1:")
print("  二维数组形状补1后:(1, 1, 4)")
print("  三维数组形状:   (2, 3, 4)")

explain_right_alignment((1, 4), (2, 3, 4))

# 总结说明
print("\n" + "=" * 50)
print("关键概念总结:")
print("1. 向右对齐: 比较两个数组形状时，从最右边的维度开始对齐")
print("2. 补1规则: 形状较短的数组，在左边（前面）补1直到维度数相同")
print("3. 兼容性检查: 对应位置的维度大小必须相等，或者其中一个为1")
print("4. 结果形状: 每个维度取对应维度的最大值")
print("\n为什么叫'向右对齐'?")
print("- 就像我们写字一样，从左到右书写，但比较时从右到左对齐")
print("- 这样设计使得(3,)可以与(2,3)兼容，因为3对齐了")
print("- 如果是向左对齐，(3,)和(2,3)就无法兼容了")


"""
广播过程：
在示例1中，标量b(形状())先被广播为形状(1,)，然后进一步广播为(3,)
在示例2中，一维数组d(形状(3,))先被广播为形状(1, 3)，然后进一步广播为(2, 3)
在示例3中，二维数组f(形状(1, 4))先被广播为形状(1, 1, 4)，然后进一步广播为(2, 3, 4)
"""