
'''
# 列表的定义
my_list = [1, 1.1, True, 1+2j, 'hello', [1, 2, 3]]
print(my_list)
'''

'''
# 列表的下标访问
my_list = [1, 2, 3, 4, 5]
print(my_list[0])
print(my_list[-1])
print(my_list[4])
# print(my_list[10])

# 列表的切片访问
print(my_list[0:3:1])
print(my_list[0:3:2])
print(my_list[:3:1])
print(my_list[::])
print(my_list[:3])
print(my_list[-4:-1])
print(my_list[-4:])
print(my_list[::-1])
'''

'''
# 列表的加法和乘法
ls1 = [1, 2, 3]
ls2 = [4, 5, 6]
print(ls2 + ls1)
print(ls1 * 2)
'''


'''
# 列表的增加元素
my_list = [1, 2, 3]

# append的使用
# my_list.append([1, 2, 3])

# insert的使用
# my_list.insert(2, 4)
my_list2 = [1, 3, 5]

# extend类似与列表的加法操作，括号里的列表相当于加法后的列表
# 它会被拼接到原始列表的后面
my_list.extend(my_list2)
print(my_list)
'''


'''
# 列表元素的删除
my_list = [1, 2, 3]

# remove：用于删除指定的元素
# my_list.remove(4)

# pop:将列表中的某个元素弹出来，可以使用变量去接收，并且可以自定义要弹出的下标
# num = my_list.pop(0)
# print(my_list)
# print(num)


# clear:删除列表中的所有元素，使列表成为空列表
# my_list.clear()
# print(my_list)

# del:是一个关键字，当指定下标时，删除对应的元素，不指定下标时，删除整个列表
del my_list
print(my_list)

'''

'''
# 列表元素的修改
my_list = [1, 2 ,3]

# 下标修改
# my_list[0] = 0
# print(my_list)

# 切片修改
# 当等号右边使用列表时，可以跨数量修改
# my_list[0:2] = [3, 4, 5]
# print(my_list)


# 当等号右边不适用列表时，不可以跨数量修改，赋值的数量必须和要修改的数量一致
# 多个赋值时，每个值之间需要使用逗号隔开
my_list[0:2] = 5, 6
print(my_list)
'''


'''
# 列表元素的查找
my_list = [1, 2, 3]

# count函数：用来统计某元素在列表中的个数
# print(my_list.count(5))


# in关键字的用法：  元素 in 变量名
# in关键字的返回值是： True 或 False
if 0 in my_list:
    print("1 在列表中")
'''

# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))

# 列表的反转操作，不需要参数，直接调用即可
# my_list.reverse()
# print(my_list)


# 列表的排序操作
# my_list = [6, 46, 32, 1, 10]

# sort函数的参数 reverse：默认为False，按照从小到大的顺序排序
# 如果为True，按照从大到小的顺序排序
# key参数：可以指定排序所参照的属性，比如传入len函数，会按照元素的个数进行排序
# my_list = ['abcd', 'ef', 'ghc']
# my_list.sort(reverse=True, key=len)
# print(my_list)


# 列表的嵌套
# 访问方式： 如果想要访问到具体的元素的话，嵌套多少层列表，就需要指定多少层索引
# my_list = [[1, 2, 3], [4, 5, 6]]
# print(my_list[0][1])

# 列表的浅拷贝
# l1 = [1, 2, 3, 'abcd']
# l2 = l1.copy()
#
# print(l1)
# print(l2)
#
# # 修改l1列表里的元素
# l1[0] = 10
# print(l1)
# print(l2)


'''
# 列表的深拷贝
l1 = [[1, 2, 3], 4, 5, 6]

# 定义一个浅拷贝列表
l2 = l1.copy()

# 定义一个深拷贝列表
import copy
l3 = copy.deepcopy(l1)

print('修改前的l1列表：', l1)
print('修改前的l2列表：', l2)
print('修改前的l3列表：', l3)

l1[0][1] = 10
print('修改后的l1列表：', l1)
print('修改后的l2列表：', l2)
print('修改后的l3列表：', l3)
'''


# 列表推导式
# 原始列表
# ls1 = [1, 2, 3, 4, 5]

# 目标：生成一个新列表，要求新列表里的元素是原始列表中的每个元素的平方值
# [1, 4, 9, 16, 25]
# for i in range(len(ls1)):
#     ls1[i] = ls1[i] ** 2
# print(ls1)

# 执行逻辑：首先从ls1里拿出元素赋值给x，然后执行x<3这个判断语句
# 如果判断语句返回的值是True，则执行表达式x ** 2
# 如果判断语句返回的值是False，则不执行表达式
# squared_list = [x ** 2 for x in ls1 if x < 3]
# print(squared_list)

# 列表推导式的嵌套使用
# 原始列表
ls1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 目标：将这个嵌套的列表，拆为普通的列表
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 使用for循环
# 使用第一层循环，访问到内层的列表
# new_list = []
# for i in range(len(ls1)):
#     for j in range(len(ls1[i])):
#         print(ls1[i][j])
#         new_list.append(ls1[i][j])
# print(new_list)

# 执行逻辑：首先需要从嵌套列表里得到小的列表，所以首先执行的是for x in ls1
# 此时x就分别代表了这三个小列表
# 接着执行for y in x, 从x这个列表里拿到具体的y的值
# 然后直接放到新列表里
new_list = [y for x in ls1 for y in x]
print(new_list)