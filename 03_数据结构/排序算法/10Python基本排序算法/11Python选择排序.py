# 选择排序
def selection_sort(arr):
    # 遍历所有数组元素
    for i in range(len(arr)):
        # 找到最小元素的索引
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # 将找到的最小元素与第一个元素交换
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# 测试排序函数
arr = [64, 34, 43, 12, 22, 11, 55]
arr_selection_sort = selection_sort(arr)
print(f"选择排序后的数组:{arr_selection_sort}")
