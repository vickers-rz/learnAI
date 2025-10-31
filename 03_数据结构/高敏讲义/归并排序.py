
#python归并排序

def merge_sort(arr):
    #停止递归的条件,
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]  #左边的
    #print("left:",left)
    right=arr[mid:]
    #print("right:",right)
    left=merge_sort(left)  #右边的
    right=merge_sort(right)
    return merge(left,right)

def merge(left,right):
    merged=[]
    left_index=0
    right_index=0
    print("left",left)
    print("right",right)
    while left_index<len(left) and right_index<len(right):
        if left[left_index]<right[right_index]:
            merged.append(left[left_index])
            left_index+=1
        else:
            merged.append(right[right_index])
            right_index+=1
        print("merged",merged)
    #合并到结果的数组中
    #merged.extend(left[left_index:])
    #merged.extend(right[right_index:])
    merged+=left[left_index:]
    #print("left***",left[left_index:])
    merged+=right[right_index:]
    #print("right***", right[right_index:])
    #print("merged----", merged)
    return merged

arr=[8,9,1,7,2,3,5,4,6,0]
print(arr)
res=merge_sort(arr)
print(res)