def binary_search_visual():
    """可视化二分查找过程"""
    # 原始数据
    original_list = [6, 4, 7, 8, 1, 3, 8, 9, 10, 11]
    target = 10
    
    print("二分查找可视化演示")
    print("=" * 50)
    print(f"原始列表: {original_list}")
    print(f"查找目标: {target}")
    print()
    
    # 排序
    sorted_list = sorted(original_list)
    print(f"排序后:   {sorted_list}")
    print("索引:     ", end="")
    for i in range(len(sorted_list)):
        print(f"{i:2d}", end=" ")
    print("\n")
    
    # 二分查找过程
    low = 0
    high = len(sorted_list) - 1
    step = 1
    
    while low <= high:
        print(f"第 {step} 轮查找:")
        mid = (low + high) // 2
        
        # 可视化当前搜索范围
        line1 = [" "] * len(sorted_list)
        line2 = [" "] * len(sorted_list)
        line3 = [" "] * len(sorted_list)
        
        # 标记搜索范围
        for i in range(low, high + 1):
            line1[i] = "-" 
        line1[low] = "<"
        line1[high] = ">"
        
        # 标记中间位置
        line2[mid] = "^"
        
        # 标记数值
        for i in range(len(sorted_list)):
            line3[i] = f"{sorted_list[i]:2d}"
        
        print("          " + "".join([f"{x:2s}" for x in line1]))
        print("          " + "".join([f"{x:2s}" for x in line2]))
        print("          " + "".join([f"{x:2s}" for x in line3]))
        print(f"          中间索引: {mid}, 中间值: {sorted_list[mid]}")
        
        if sorted_list[mid] == target:
            print(f"          找到目标值 {target}!")
            return mid
        elif sorted_list[mid] > target:
            print(f"          {sorted_list[mid]} > {target}, 查找左半部分")
            high = mid - 1
        else:
            print(f"          {sorted_list[mid]} < {target}, 查找右半部分")
            low = mid + 1
            
        print()
        step += 1
    
    return None

# 运行可视化演示
binary_search_visual()