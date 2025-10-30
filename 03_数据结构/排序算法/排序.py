# -*- coding: utf-8 -*-
"""
排序算法实现
==============

本文件包含五种常用的排序算法实现：
1. 冒泡排序 (Bubble Sort)
2. 选择排序 (Selection Sort)
3. 插入排序 (Insertion Sort)
4. 归并排序 (Merge Sort)
5. 快速排序 (Quick Sort)
"""

### 1. 冒泡排序 (Bubble Sort)
### ------------------------------------------------------------------------

def bubble_sort(arr):
    """
    冒泡排序
    
    原理：通过两两比较相邻的元素，将较大的元素"冒泡"到数组的末尾。
    它会重复比较并交换，直到整个数组有序。
    
    Args:
        arr: 待排序的列表
        
    Returns:
        排序后的列表
    """
    # 获取数组的长度
    n = len(arr)

    # 外层循环控制进行多少轮比较，每一轮都会让一个最大元素浮动到数组的末尾
    for i in range(n):
        # 设置一个标志变量，用来检查是否有发生交换操作
        swapped = False

        # 内层循环进行相邻元素的比较
        # 内层循环长度逐渐缩小，因为每次外层循环后最大的元素已经"冒泡"到最后
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，则交换它们
            if arr[j] > arr[j + 1]:
                # 交换操作，Python中的交换方式
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # 如果发生了交换，标记为True

        # 如果没有发生交换，说明数组已经是有序的，提前退出循环
        if not swapped:
            break

    # 返回排序后的数组
    return arr

"""
解释：

1. 外层循环：for i in range(n)
   控制排序的轮数。每完成一轮，最值会被放到末尾，
   下一轮只需要对前面未排序的部分进行排序。
   
2. 内层循环：for j in range(0, n - i - 1)
   比较相邻的元素。随着每轮外层循环的结束，i的增大，
   内层循环的范围逐渐减小。
   
3. 交换：
   如果发现相邻元素不符合顺序（例如 arr[j] > arr[j + 1]），
   则交换它们的位置。
   
4. 提前退出：
   如果某一轮没有发生任何交换，说明数组已经排好序，
   可以提前退出循环。
"""


### 2. 选择排序 (Selection Sort)
### ------------------------------------------------------------------------

def selection_sort(arr):
    """
    选择排序
    
    原理：每次从未排序的部分中选择最小的元素，
    放到已排序部分的末尾。通过逐步减少未排序部分来进行排序。
    
    Args:
        arr: 待排序的列表
        
    Returns:
        排序后的列表
    """
    # 外层循环：从头到尾遍历整个数组，每次找最小值
    for i in range(len(arr)):
        # 假设当前位置的元素是未排序部分中的最小元素
        min_idx = i

        # 内层循环：从i后面的位置开始找最小的元素
        for j in range(i + 1, len(arr)):
            # 如果找到了比当前最小值还小的元素，就更新最小元素的位置
            if arr[j] < arr[min_idx]:
                min_idx = j

        # 交换当前元素与找到的最小元素
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

"""
解释：

1. 外层循环：for i in range(len(arr))
   依次遍历数组的每一个位置，将未排序部分的最小值放到当前位置。
   
2. 内层循环：for j in range(i + 1, len(arr))
   从当前位置后面开始找比当前元素更小的值。
   
3. 最小值更新：if arr[j] < arr[min_idx]
   如果找到了一个更小的元素，就记录它的位置。
   
4. 交换：arr[i], arr[min_idx] = arr[min_idx], arr[i]
   将最小值和当前元素交换。
"""


### 3. 插入排序 (Insertion Sort)
### ------------------------------------------------------------------------

def insertion_sort(arr):
    """
    插入排序
    
    原理：将未排序的元素逐个插入到已排序部分，
    保证已排序部分始终是有序的。
    
    Args:
        arr: 待排序的列表
        
    Returns:
        排序后的列表
    """
    # 从第二个元素开始，因为第一个元素默认是已经排序的
    for i in range(1, len(arr)):
        # 当前要插入的元素
        key = arr[i]
        # j是用来遍历已排序部分的指针
        j = i - 1

        # 将已排序部分大于key的元素都向后移动一位
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # 将元素移到后面
            j -= 1  # 向前查找

        # 找到合适的位置，把key插入进去
        arr[j + 1] = key

    return arr

"""
解释：

1. 外层循环：for i in range(1, len(arr))
   从第二个元素开始，假设第一个元素已经排序好。
   
2. 插入过程：key = arr[i]
   当前要插入的元素。然后通过内层 while 循环，
   将已排序部分大于 key 的元素向右移动一位。
   
3. 插入位置：arr[j + 1] = key
   在合适的位置插入 key。
"""


### 4. 归并排序 (Merge Sort)
### ------------------------------------------------------------------------

def merge_sort(arr):
    """
    归并排序
    
    原理：一种分治法排序。首先将数组分成两半，
    然后分别递归排序，再将两部分合并成一个有序的数组。
    
    Args:
        arr: 待排序的列表
        
    Returns:
        排序后的列表
    """
    # 如果数组长度大于1，则进行分割和排序
    if len(arr) > 1:
        # 找到中间点，分割数组
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 递归排序左右两部分
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # 合并两个已经排序的部分
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 如果左边部分还有剩余，继续填充
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # 如果右边部分还有剩余，继续填充
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

"""
解释：

1. 递归分割：merge_sort(left_half) 和 merge_sort(right_half)
   递归地将数组分成两部分，直到每部分只有一个元素。
   
2. 合并操作：
   通过比较两个已排序部分的元素，将它们合并成一个更大的已排序部分。
"""


### 5. 快速排序 (Quick Sort)
### ------------------------------------------------------------------------

def quick_sort(arr):
    """
    快速排序
    
    原理：一种分治法排序，通过选择一个基准元素，
    将数组分成两部分，递归排序后合并。
    
    Args:
        arr: 待排序的列表
        
    Returns:
        排序后的列表
    """
    # 递归出口：如果数组为空或只有一个元素，则直接返回
    if len(arr) <= 1:
        return arr

    # 选择基准元素，这里选择中间的元素
    pivot = arr[len(arr) // 2]

    # 将数组分成三部分：小于基准、等于基准、大于基准
    left = [x for x in arr if x < pivot]    # 小于基准
    middle = [x for x in arr if x == pivot] # 等于基准
    right = [x for x in arr if x > pivot]   # 大于基准

    # 递归对左边和右边部分进行排序
    return quick_sort(left) + middle + quick_sort(right)

"""
解释：

1. 基准元素选择：pivot = arr[len(arr) // 2]
   选择数组的中间元素作为基准。
   
2. 三部分划分：
   通过列表推导式，将数组分成小于基准、等于基准和大于基准的三部分。
   
3. 递归排序：
   对左右部分分别进行递归排序，再将三部分合并。
"""


### 总结
### ------------------------------------------------------------------------

"""
每种排序算法的核心思想和步骤都不同，但本质上都是通过不断比较和交换或分割来将数组排序。
你可以根据数据的大小、排列顺序和内存限制来选择合适的排序算法。

时间复杂度比较：
- 冒泡排序：O(n²)
- 选择排序：O(n²)
- 插入排序：O(n²)
- 归并排序：O(n log n)
- 快速排序：平均 O(n log n)，最坏 O(n²)

空间复杂度比较：
- 冒泡排序：O(1)
- 选择排序：O(1)
- 插入排序：O(1)
- 归并排序：O(n)
- 快速排序：平均 O(log n)，最坏 O(n)
"""