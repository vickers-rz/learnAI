"""
递归查找 - 改进版

递归是一种重要的编程技术，函数直接或间接地调用自身来解决问题。
递归通常用于处理具有自相似结构的问题。
"""

def recursive_search(lst, target, index=0):
    """
    使用递归在列表中查找目标值
    
    参数:
        lst (list): 要搜索的列表
        target: 要查找的目标值
        index (int): 当前搜索的索引位置，默认从0开始
    
    返回:
        int: 目标值的索引，如果未找到则返回-1
    
    递归思路:
        1. 基准情形:
           - 如果索引超出列表范围，返回-1表示未找到
           - 如果当前索引位置的元素等于目标值，返回当前索引
        2. 递归情形:
           - 在下一个位置继续搜索目标值
    """
    
    # 执行过程分解(Debug注释):
    # 第1步: 检查是否已搜索完所有元素(基准情形)
    # print(f"检查索引 {index} 是否超出范围")
    if index == len(lst):
        # print(f"已到达列表末尾，未找到目标值 {target}")
        return -1
    
    # 第2步: 检查当前位置是否为目标值(基准情形)
    # print(f"检查 lst[{index}] = {lst[index]} 是否等于目标值 {target}")
    if lst[index] == target:
        # print(f"在索引 {index} 处找到目标值 {target}")
        return index
    
    # 第3步: 递归在下一个位置搜索(递归情形)
    # print(f"在索引 {index + 1} 处继续搜索")
    return recursive_search(lst, target, index + 1)


def recursive_search_with_debug(lst, target, index=0):
    """
    带调试信息的递归查找，用于理解递归执行过程
    """
    print(f"调用 recursive_search(lst={lst}, target={target}, index={index})")
    
    # 基准情形1: 已经搜索完所有元素
    if index == len(lst):
        print(f"  基准情形触发: index({index}) == len(lst)({len(lst)})")
        print(f"  返回 -1 (未找到目标值)")
        return -1
    
    # 基准情形2: 找到目标值
    if lst[index] == target:
        print(f"  基准情形触发: lst[{index}] == {target}")
        print(f"  返回 {index} (找到目标值)")
        return index
    
    # 递归情形: 在下一个位置继续搜索
    print(f"  递归情形: 在下一个位置(index={index + 1})继续搜索")
    result = recursive_search_with_debug(lst, target, index + 1)
    print(f"  从 recursive_search(lst={lst}, target={target}, index={index + 1}) 返回 {result}")
    return result


# 测试代码
if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5]
    
    print("=== 基本递归查找测试 ===")
    print(f"在列表 {test_list} 中查找 3:")
    result1 = recursive_search(test_list, 3)
    print(f"结果: {result1}\n")
    
    print(f"在列表 {test_list} 中查找 6:")
    result2 = recursive_search(test_list, 6)
    print(f"结果: {result2}\n")
    
    print(f"在列表 {test_list} 中查找 1:")
    result3 = recursive_search(test_list, 1)
    print(f"结果: {result3}\n")
    
    print("=== 带调试信息的递归查找演示 ===")
    print("查找过程分解:")
    recursive_search_with_debug([1, 2, 3], 2)