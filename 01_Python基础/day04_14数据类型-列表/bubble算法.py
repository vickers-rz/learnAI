# 待排序列表
arr = [5, 2, 9, 1, 5, 6]

n = len(arr)
for i in range(n - 1):                 # 第 i 趟：把当前最大值“冒”到右侧
    swapped = False                    # 标记这一趟是否发生过交换（可提前结束）
    for j in range(n - i - 1):         # 相邻比较到已排好部分的前一个
        if arr[j] > arr[j + 1]:
            # 用临时变量交换（更易懂）
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
            swapped = True
    if not swapped:                    # 这一趟没交换，说明已经有序
        break

print(arr)  # [1, 2, 5, 5, 6, 9]
