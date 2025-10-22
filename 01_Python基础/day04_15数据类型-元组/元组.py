
'''
# 元组的定义
# 元组名字 = (元素1, 元素2, ..., 元素n)
# 元组也可以存放不同类型的数据
my_tuple = (1, 1.1, True, 1+2j, 'asd', [1, 2, 3], (1, 2, 3))
print(my_tuple)
'''

'''
# 元组的下标访问
my_tuple = (1, 2, 3, 4, 5)
# 访问时，使用 变量名 + 方括号
# 比如 my_tuple[0]
# 顺序访问
print(my_tuple[0])
# 逆序访问
print(my_tuple[-1])
# 越界访问会报错
# print(my_tuple[10])
'''
'''
# 元组的切片访问
my_tuple = (1, 2, 3, 4, 5)
# 从元组的起始值开始访问，访问到下标为4的元素，且步长为1，此处省略掉了
print(my_tuple[:4])
# 从元组的下标为2的元素开始访问，访问到最后一个元素，且步长为1
print(my_tuple[2:])
# 从元组的下标为1的元素开始访问，访问到最后一个元素，且步长为2
print(my_tuple[1::2])
# 从元组的下标为-3的元素开始访问，访问到最后一个元素，且步长为1
print(my_tuple[-3:-1])
# 从元组的下标为-1的元素开始访问，访问到下标为-3的元素，且步长为-1，起到了一个逆序的作用
print(my_tuple[-1:-3:-1])
# 元组的快速逆序
print(my_tuple[::-1])
'''


'''
# 元组的加法和乘法
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)
print(tuple1 * 2)
'''
'''
# 元组的常用操作
tupl1 = (1, 2, 3, 4, 5)
# 求元组中的元素的个数
print(len(tupl1))
# 求元组中元素的最大值
print(max(tupl1))
# 求元组中元素的最小值
print(min(tupl1))

# 判断某元素是否在元组里，如果在就执行if语句里的子代码块
if 1 in tupl1:
    print("1 在元组里")
# del关键字，用来删除元组
del tupl1
print(tupl1)
'''

# 元组的推导式的使用
tp1 = (x for x in range(10))
for i in tp1:
    print(i)


