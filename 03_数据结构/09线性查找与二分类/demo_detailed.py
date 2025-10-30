# 二分查找详细演示

def binary_search_demo():
    # 原始列表
    original_list = [6, 4, 7, 8, 1, 3, 8, 9, 10, 11]
    target = 10
    
    print("二分查找详细执行过程演示")
    print("=" * 40)
    print(f"原始列表: {original_list}")
    print(f"查找目标: {target}")
    
    # 排序列表
    sorted_list = sorted(original_list)  # 使用sorted避免修改原列表
    print(f"排序后列表: {sorted_list}")
    print()
    
    # 初始化变量
    low = 0
    high = len(sorted_list) - 1
    step = 1
    
    print("开始二分查找过程:")
    print("-" * 30)
    
    while low <= high:
        print(f"第 {step} 轮查找:")
        print(f"  搜索范围: 索引 {low} 到 {high}")
        print(f"  搜索内容: {sorted_list[low:high+1]}")
        
        # 计算中间位置
        mid = (low + high) // 2
        mid_value = sorted_list[mid]
        
        print(f"  中间位置: 索引 {mid}")
        print(f"  中间值: {mid_value}")
        print(f"  目标值: {target}")
        
        if mid_value == target:
            print(f"  结果: 找到了! 位置在索引 {mid}")
            return mid
        elif mid_value > target:
            print(f"  操作: {mid_value} > {target}, 目标在左半部分")
            high = mid - 1
            print(f"  更新范围: low={low}, high={high}")
        else:
            print(f"  操作: {mid_value} < {target}, 目标在右半部分")
            low = mid + 1
            print(f"  更新范围: low={low}, high={high}")
        
        step += 1
        print()
    
    print("查找结束: 未找到目标元素")
    return None

# 运行演示
if __name__ == "__main__":
    result = binary_search_demo()
    print("=" * 40)
    if result is not None:
        print(f"最终结果: 找到目标，位于索引 {result}")
    else:
        print("最终结果: 未找到目标")