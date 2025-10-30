# 二分查找详细解析版本
# 二分查找是一种在有序数组中查找特定元素的高效算法
# 时间复杂度为 O(log n)，比线性查找的 O(n) 更快

def binary_search(num_list, target_num):
    """
    二分查找函数
    参数:
    num_list: 待查找的数字列表
    target_num: 目标数字
    返回:
    找到目标数字的索引，如果未找到则返回None
    """
    
    # 首先对列表进行排序，因为二分查找只能在有序列表中进行
    # 注意：sort()方法会直接修改原始列表，而sorted()函数会返回新的排序列表而不修改原列表
    print(f"原始列表: {num_list}")
    num_list.sort()  
    print(f"排序后列表: {num_list}")
    
    # 设置搜索范围的边界索引
    low = 0              # 搜索范围的下界（起始索引）
    high = len(num_list) - 1   # 搜索范围的上界（结束索引）
    print(f"初始搜索范围: [{low}, {high}]")
    
    # 当搜索范围有效时继续查找（下界不能超过上界）
    step = 1  # 用于追踪查找步骤
    while low <= high:
        print(f"\n--- 第 {step} 步查找 ---")
        print(f"当前搜索范围索引: [{low}, {high}]")
        
        # 计算中间位置索引（使用整数除法）
        mid = (low + high) // 2
        mid_num = num_list[mid]  # 获取中间位置的值
        
        print(f"中间位置索引: {mid}")
        print(f"中间值: {mid_num}")
        print(f"目标值: {target_num}")
        
        # 比较中间值与目标值
        if mid_num == target_num: 
            # 找到目标值，返回索引
            print(f"成功! 找到目标值 {target_num} 在索引 {mid}")
            return mid
            
        elif mid_num > target_num:
            # 中间值大于目标值，说明目标值在左半部分
            print(f"中间值 {mid_num} > 目标值 {target_num}")
            print("=> 目标值在左半部分")
            high = mid - 1  # 缩小搜索范围至上半部分（不包括中间位置）
            print(f"更新搜索范围为: [{low}, {high}]")
            
        else:
            # 中间值小于目标值，说明目标值在右半部分
            print(f"中间值 {mid_num} < 目标值 {target_num}")
            print("=> 目标值在右半部分")
            low = mid + 1   # 缩小搜索范围至下半部分（不包括中间位置）
            print(f"更新搜索范围为: [{low}, {high}]")
        
        step += 1
    
    # 如果循环结束仍未找到目标值，返回 None
    print("\n搜索完成，未找到目标值")
    return None

# 测试代码
print("=" * 50)
print("二分查找算法演示")
print("=" * 50)

num_list = [6, 4, 7, 8, 1, 3, 8, 9, 10, 11]
target_num = 10

print(f"测试数据: {num_list}")
print(f"查找目标: {target_num}")
print("-" * 30)

# 调用二分查找函数
result = binary_search(num_list.copy(), target_num)  # 使用copy()避免修改原始列表

print("-" * 30)
print("查找结果:")
if result is not None:
    print(f'二分查找成功找到目标值 {target_num} 在索引 {result}')
else:
    print('未找到目标元素！')

"""
算法执行过程总结:
1. 首先对数组进行排序，使其变为有序数组
2. 设置两个指针low和high分别指向数组的开始和结束位置
3. 计算中间位置mid = (low + high) // 2
4. 比较num_list[mid]与目标值:
   - 如果相等，则找到目标，返回索引
   - 如果num_list[mid] > 目标值，则目标在左半部分，更新high = mid - 1
   - 如果num_list[mid] < 目标值，则目标在右半部分，更新low = mid + 1
5. 重复步骤3-4，直到找到目标或low > high
"""