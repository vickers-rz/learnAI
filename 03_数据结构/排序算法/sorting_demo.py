# -*- coding: utf-8 -*-
"""
排序算法演示
"""

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

def demo_all_sorting_algorithms():
    """演示所有排序算法"""
    # 测试数据
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9, 3],
        [1, 2, 3, 4, 5],  # 已排序
        [5, 4, 3, 2, 1],  # 逆序
        [1],              # 单元素
        []                # 空数组
    ]
    
    algorithms = [
        ("冒泡排序", bubble_sort),
        ("选择排序", selection_sort),
        ("插入排序", insertion_sort),
        ("归并排序", merge_sort),
        ("快速排序", quick_sort)
    ]
    
    for arr in test_arrays:
        print("=" * 50)
        print(f"原始数组: {arr}")
        print("=" * 50)
        
        for name, sort_func in algorithms:
            # 为每个算法创建独立的数组副本
            test_arr = arr.copy()
            print(f"\n{name}演示:")
            print("-" * 30)
            
            # 执行排序
            sorted_arr = sort_func(test_arr)
            
            print(f"排序结果: {sorted_arr}")
            print()

if __name__ == "__main__":
    demo_all_sorting_algorithms()