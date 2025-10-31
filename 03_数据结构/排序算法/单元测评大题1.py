单元测评大题1.py
"""
假设你有一个整数数组，其中包含大量重复元素，如何对该数组进行高效排序？
请基于希尔排序、快速排序和归并排序的思想，提出改进的算法思路。
"""

def improved_shell_sort(arr):
    """
    改进的希尔排序算法
    
    针对大量重复元素的优化思路：
    1. 使用更高效的间隔序列（如Knuth序列），减少不必要的比较
    2. 结合三路划分思想，在每轮排序中对相等元素进行特殊处理
    3. 对于相等元素较多的子数组，提前终止某些间隔的处理
    """
    n = len(arr)
    if n <= 1:
        return arr
    
    # 使用Knuth序列 (3^k - 1) / 2 作为间隔
    gaps = []
    gap = 1
    while gap < n // 3:
        gaps.append(gap)
        gap = gap * 3 + 1
    gaps.reverse()  # 从大到小排序
    
    for gap in gaps:
        # 对每个间隔进行插入排序，但针对相等元素做优化
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # 优化：跳过相等元素的比较
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    
    return arr


def improved_quick_sort(arr):
    """
    改进的快速排序算法（三路快排）
    
    针对大量重复元素的优化思路：
    1. 使用三路划分（Dutch National Flag）替代传统的二路划分
    2. 将数组划分为三部分：< pivot、= pivot、> pivot
    3. 递归只处理小于和大于pivot的部分，等于pivot的部分已经有序
    4. 对于大量重复元素，可以显著减少递归层数和比较次数
    """
    def quick_sort_3way(arr, low, high):
        if low >= high:
            return
        
        lt = low  # arr[low..lt-1] < pivot
        gt = high  # arr[gt+1..high] > pivot
        i = low + 1  # arr[lt..i-1] == pivot
        
        pivot = arr[low]
        
        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
                # 注意：这里i不增加，因为交换过来的元素还没有检查
            else:
                i += 1
        
        # 递归处理小于pivot和大于pivot的部分
        quick_sort_3way(arr, low, lt - 1)
        quick_sort_3way(arr, gt + 1, high)
    
    if len(arr) <= 1:
        return arr
    
    quick_sort_3way(arr, 0, len(arr) - 1)
    return arr


def improved_merge_sort(arr):
    """
    改进的归并排序算法
    
    针对大量重复元素的优化思路：
    1. 在合并阶段检测是否已经有序（前一部分的最大值 <= 后一部分的最小值）
    2. 对于大量重复元素，在合并时可以批量复制相等元素
    3. 使用哨兵元素简化边界条件判断
    """
    def merge_sort_helper(arr, temp_arr, left, right):
        if left >= right:
            return
        
        mid = (left + right) // 2
        merge_sort_helper(arr, temp_arr, left, mid)
        merge_sort_helper(arr, temp_arr, mid + 1, right)
        
        # 优化：如果已经有序则不需要合并
        if arr[mid] <= arr[mid + 1]:
            return
        
        merge(arr, temp_arr, left, mid, right)
    
    def merge(arr, temp_arr, left, mid, right):
        # 复制到临时数组
        for i in range(left, right + 1):
            temp_arr[i] = arr[i]
        
        i, j, k = left, mid + 1, left
        
        # 合并过程
        while i <= mid and j <= right:
            if temp_arr[i] <= temp_arr[j]:
                arr[k] = temp_arr[i]
                i += 1
            else:
                arr[k] = temp_arr[j]
                j += 1
            k += 1
        
        # 复制左半部分剩余元素
        while i <= mid:
            arr[k] = temp_arr[i]
            i += 1
            k += 1
        
        # 复制右半部分剩余元素
        while j <= right:
            arr[k] = temp_arr[j]
            j += 1
            k += 1
    
    if len(arr) <= 1:
        return arr
    
    temp_arr = [0] * len(arr)
    merge_sort_helper(arr, temp_arr, 0, len(arr) - 1)
    return arr


# 测试用例
if __name__ == "__main__":
    # 测试包含大量重复元素的数组
    test_arrays = [
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        [1, 3, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
    ]
    
    for i, arr in enumerate(test_arrays):
        print(f"测试数组 {i+1}: {arr}")
        
        # 测试改进的希尔排序
        arr1 = arr.copy()
        improved_shell_sort(arr1)
        print(f"改进希尔排序结果: {arr1}")
        
        # 测试改进的快速排序
        arr2 = arr.copy()
        improved_quick_sort(arr2)
        print(f"改进快速排序结果: {arr2}")
        
        # 测试改进的归并排序
        arr3 = arr.copy()
        improved_merge_sort(arr3)
        print(f"改进归并排序结果: {arr3}")
        print("-" * 50)