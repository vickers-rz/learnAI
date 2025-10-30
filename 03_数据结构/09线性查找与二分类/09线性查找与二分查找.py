# 线性查找

def linear_search(num_list, target_num):
    for i in range(len(num_list)):
        if num_list[i] == target_num:
            return i
    return -1

num_list = [1, 2, 3, 4, 5, 6, 7]
target_num = 10
result = linear_search(num_list, target_num)
if result != -1:
    print(f'找到目标值{target_num}在索引{result}')
else:
    print(f'没有找到目标值！')


# 二分查找

def binary_search(num_list, target_num):
    num_list.sort()  # sort()将列表进行排序，从小到大顺序，会改变原始列表，sorted()函数不会改变原始列表
    # 索引值
    low = 0
    hight = len(num_list) - 1

    while low <= hight:
        mid = (low + hight) // 2
        mid_num = num_list[mid]
        if mid_num == target_num:
            return mid
        elif mid_num > target_num:
            hight = mid - 1
        else:
            low = mid + 1
    return None

num_list = [6, 4, 7, 8, 1, 3, 8]
target_num = 10
result = binary_search(num_list, target_num)
print(f'排序后的列表：{num_list}')
if result != None:
    print(f'二分查找找到目标值{target_num}在索引{result}')
else:
    print('未找到元素！')


# 递归版二分查找

def binary_search_recursive(num_list, target_num, low, high):
    if low > high:
        return None  # 终止条件：没有找到目标值
    
    mid = (low + high) // 2
    mid_num = num_list[mid]

    if mid_num == target_num:
        return mid  # 找到目标值，返回索引
    elif mid_num > target_num:
        return binary_search_recursive(num_list, target_num, low, mid - 1)  # 递归查找左半部分
    else:
        return binary_search_recursive(num_list, target_num, mid + 1, high)  # 递归查找右半部分

def binary_search(num_list, target_num):
    num_list = sorted(num_list)  # 排序列表，避免修改原始数据
    return binary_search_recursive(num_list, target_num, 0, len(num_list) - 1)


num_list = [6, 4, 7, 8, 1, 3, 8]
target_num = 10
result = binary_search(num_list, target_num)

print(f'排序后的列表：{num_list}')
if result is not None:
    print(f'二分查找找到目标值{target_num}在索引{result}')
else:
    print('未找到元素！')











