def linear_search_recursive(lst, target, index=0):
    """
    使用递归在列表中线性查找目标元素
    
    参数:
        lst: 要搜索的列表
        target: 目标元素
        index: 当前搜索的索引位置（默认为0）
    
    返回:
        目标元素的索引，如果未找到则返回-1
    
    递归思路:
        基准情形:
        1. 当索引等于列表长度时，表示已搜索完所有元素，返回-1
        2. 当当前索引位置的元素等于目标元素时，返回当前索引
        
        递归情形:
        在下一个索引位置继续搜索
    """
    # 基准情形1: 已经搜索完所有元素
    if index == len(lst):
        return -1
    
    # 基准情形2: 找到目标元素
    if lst[index] == target:
        return index
    
    # 递归情形: 在下一个位置继续搜索
    return linear_search_recursive(lst, target, index + 1)


# 测试用例
print(linear_search_recursive([1, 2, 3, 4, 5], 3))
print(linear_search_recursive([1, 2, 3, 4, 5], 6))
print(linear_search_recursive([1, 2, 3, 4, 5], 1))
