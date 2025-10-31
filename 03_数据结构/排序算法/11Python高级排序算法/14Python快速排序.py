# Python实现快速排序

def quick_sort(arr):
    # 终止递归的条件
    if len(arr) <= 1:
        return arr

    # 选择基准值
    pivot = arr[0]
    # left = []
    # for x in arr:
    #     if x < pivot:
    #         left.append(x)

    # 列表推导式
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# 测试
arr = [8, 9, 1, 7, 2, 3, 5, 4, 6, 0]
result = quick_sort(arr)
print(f'快速排序后的列表：{result}')