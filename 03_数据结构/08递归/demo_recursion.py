"""
递归教学演示文件
本文件将通过多个例子帮助你理解递归的概念和应用
"""

# 1. 基础递归概念：计算阶乘
def factorial(n):
    """
    计算 n 的阶乘 (n!)
    
    递归思路：
    - 终止条件：n == 0 或 n == 1 时，返回 1
    - 递归关系：n! = n * (n-1)!
    """
    print(f"  调用 factorial({n})")
    
    # 终止条件
    if n == 0 or n == 1:
        print(f"  factorial({n}) 返回 1")
        return 1
    
    # 递归步骤
    result = n * factorial(n - 1)
    print(f"  factorial({n}) 返回 {n} * factorial({n-1}) = {result}")
    return result


# 2. 递归计算数组元素之和
def sum_array(arr, index=0):
    """
    使用递归计算数组元素之和
    
    递归思路：
    - 终止条件：index 到达数组末尾时，返回 0
    - 递归关系：当前元素 + 剩余元素之和
    """
    print(f"  调用 sum_array({arr}, {index})")
    
    # 终止条件：已遍历完所有元素
    if index == len(arr):
        print(f"  sum_array({arr}, {index}) 返回 0 (到达数组末尾)")
        return 0
    
    # 递归步骤
    result = arr[index] + sum_array(arr, index + 1)
    print(f"  sum_array({arr}, {index}) 返回 {arr[index]} + sum_array({arr}, {index+1}) = {result}")
    return result


# 3. 斐波那契数列（递归实现）
def fibonacci(n):
    """
    计算斐波那契数列第 n 项
    
    递归思路：
    - 终止条件：F(0) = 0, F(1) = 1
    - 递归关系：F(n) = F(n-1) + F(n-2)
    """
    print(f"  调用 fibonacci({n})")
    
    # 终止条件
    if n <= 1:
        print(f"  fibonacci({n}) 返回 {n}")
        return n
    
    # 递归步骤
    result = fibonacci(n - 1) + fibonacci(n - 2)
    print(f"  fibonacci({n}) 返回 fibonacci({n-1}) + fibonacci({n-2}) = {result}")
    return result


# 4. 递归实现幂运算
def power(base, exp):
    """
    使用递归计算 base 的 exp 次方
    
    递归思路：
    - 终止条件：exp == 0 时返回 1
    - 递归关系：base^exp = base * base^(exp-1)
    """
    print(f"  调用 power({base}, {exp})")
    
    # 终止条件
    if exp == 0:
        print(f"  power({base}, {exp}) 返回 1")
        return 1
    
    # 递归步骤
    result = base * power(base, exp - 1)
    print(f"  power({base}, {exp}) 返回 {base} * power({base}, {exp-1}) = {result}")
    return result


if __name__ == "__main__":
    print("=" * 50)
    print("递归教学演示")
    print("=" * 50)
    
    print("\n1. 计算阶乘:")
    print("factorial(5)")
    result1 = factorial(5)
    print(f"最终结果: 5! = {result1}")
    
    print("\n" + "-" * 30)
    print("\n2. 计算数组元素之和:")
    test_arr = [1, 2, 3, 4]
    print(f"sum_array({test_arr})")
    result2 = sum_array(test_arr)
    print(f"最终结果: {test_arr} 的元素之和 = {result2}")
    
    print("\n" + "-" * 30)
    print("\n3. 斐波那契数列:")
    print("fibonacci(5)")
    result3 = fibonacci(5)
    print(f"最终结果: 斐波那契数列第5项 = {result3}")
    
    print("\n" + "-" * 30)
    print("\n4. 幂运算:")
    print("power(2, 3)")
    result4 = power(2, 3)
    print(f"最终结果: 2^3 = {result4}")