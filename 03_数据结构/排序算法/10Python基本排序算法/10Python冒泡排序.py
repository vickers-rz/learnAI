# Python实现冒泡排序

def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr =[64, 34, 25, 12, 22, 11, 55]
result = bubble_sort(arr)
print(f'冒泡排序后：{result}')