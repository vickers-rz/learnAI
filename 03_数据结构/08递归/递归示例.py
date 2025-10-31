"""
递归教学示例 - 详细注释版
展示递归执行过程，帮助理解递归工作原理
"""

def linear_search_recursive_debug(lst, target, index=0, depth=0):
    """
    带调试信息的递归线性查找，用于理解递归执行过程
    
    参数:
        lst: 要搜索的列表
        target: 目标元素
        index: 当前搜索的索引位置
        depth: 递归深度（用于显示缩进）
    """
    indent = "  " * depth
    print(f"{indent}调用: search({lst}, {target}, index={index})")
    
    # 基准情形1: 已经搜索完所有元素
    if index == len(lst):
        print(f"{indent}基准情形: index({index}) == len(lst)({len(lst)}) => 返回 -1")
        return -1
    
    # 基准情形2: 找到目标元素
    if lst[index] == target:
        print(f"{indent}基准情形: lst[{index}] == {target} => 返回 {index}")
        return index
    
    # 递归情形: 在下一个位置继续搜索
    print(f"{indent}递归情形: 在下一个位置(index={index + 1})继续搜索")
    result = linear_search_recursive_debug(lst, target, index + 1, depth + 1)
    print(f"{indent}从递归调用返回: {result}")
    return result


# 示例执行过程
if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5]
    target = 3
    
    print("=== 递归查找执行过程演示 ===")
    print(f"在列表 {test_list} 中查找元素 {target}")
    print()
    
    result = linear_search_recursive_debug(test_list, target)
    
    print()
    print(f"最终结果: 元素 {target} 在索引 {result} 处")