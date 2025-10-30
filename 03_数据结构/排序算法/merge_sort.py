# -*- coding: utf-8 -*-
"""
归并排序 (Merge Sort)
"""

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
    print(f"分解数组: {arr}")
    # 如果数组长度大于1，则进行分割和排序
    if len(arr) > 1:
        # 找到中间点，分割数组
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        print(f"  分割为: 左半部分 {left_half}, 右半部分 {right_half}")

        # 递归排序左右两部分
        print(f"  递归排序左半部分:")
        left_half = merge_sort(left_half)
        print(f"  递归排序右半部分:")
        right_half = merge_sort(right_half)

        # 合并两个已经排序的部分
        i = j = k = 0
        print(f"  合并 {left_half} 和 {right_half}")
        
        # 比较两个已排序部分的元素，将较小的元素放入原数组
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                print(f"    选择左半部分元素 {left_half[i]}")
                i += 1
            else:
                arr[k] = right_half[j]
                print(f"    选择右半部分元素 {right_half[j]}")
                j += 1
            k += 1

        # 如果左边部分还有剩余，继续填充
        while i < len(left_half):
            arr[k] = left_half[i]
            print(f"    填充左半部分剩余元素 {left_half[i]}")
            i += 1
            k += 1

        # 如果右边部分还有剩余，继续填充
        while j < len(right_half):
            arr[k] = right_half[j]
            print(f"    填充右半部分剩余元素 {right_half[j]}")
            j += 1
            k += 1
            
        print(f"  合并结果: {arr}")

    return arr

"""
解释：

1. 递归分割：merge_sort(left_half) 和 merge_sort(right_half)
   递归地将数组分成两部分，直到每部分只有一个元素。
   
2. 合并操作：
   通过比较两个已排序部分的元素，将它们合并成一个更大的已排序部分。

复杂度分析：
- 时间复杂度：
  - 最坏情况：O(n log n)
  - 最好情况：O(n log n)
  - 平均情况：O(n log n)
- 空间复杂度：O(n) - 需要额外的数组来存储临时数据

适用场景：
- 数据量较大的情况
- 对稳定性有要求的场景（归并排序是稳定的）
- 对时间复杂度有稳定要求的场景（任何情况下都是O(n log n)）
- 外部排序（如处理大文件）
- 链表排序的理想选择

案例演示：
假设我们要对数组 [64, 34, 25, 12, 22, 11, 90] 进行排序：

分解过程：
[64, 34, 25, 12, 22, 11, 90]
├── [64, 34, 25, 12]
│   ├── [64, 34]
│   │   ├── [64]
│   │   └── [34]
│   │   └── 合并为 [34, 64]
│   └── [25, 12]
│       ├── [25]
│       └── [12]
│       └── 合并为 [12, 25]
│   └── 合并为 [12, 25, 34, 64]
└── [22, 11, 90]
    ├── [22, 11]
    │   ├── [22]
    │   └── [11]
    │   └── 合并为 [11, 22]
    └── [90]
    └── 合并为 [11, 22, 90]
└── 最终合并为 [11, 12, 22, 25, 34, 64, 90]

思路解析：
归并排序采用分治思想，将问题分解为更小的子问题，然后合并子问题的解得到原问题的解。
分解过程递归进行，直到每个子数组只有一个元素（自然有序）。
合并过程中通过比较两个已排序数组的元素，依次选择较小的元素放入结果数组。
由于总是选择较小元素，归并排序是稳定的排序算法。
"""