# 插入排序
def insertion_sort(arr):
    # 遍历从1到len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # 将arr[0..i-1]中比key大的元素后移
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# 测试排序函数
arr = [64, 34, 25, 12, 22, 11, 55]
arr_insertion_sort = insertion_sort(arr)
print(f"插入排序后的数组:{arr_insertion_sort}")