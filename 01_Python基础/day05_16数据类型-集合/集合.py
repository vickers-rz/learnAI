

'''
# 集合的定义
# 可变集合定义的格式：集合名字 = {元素1， 元素2}
my_set = {1, 1, 1, 1, 2, 3, 'a', 'b', 'c', (1, 2, 3)}
print(my_set)
'''

'''
# 可变集合的元素添加
my_set = {1, 2, 3, 4, 5}
# add函数：用来向可变集合中添加单个元素
my_set.add('hello world')
print(my_set)

# update函数：用来添加多个元素，要求添加的元素必须是一个序列,
# 并且将序列中的元素拆分成单个元素，并放到集合里
my_set.update('abc')
print(my_set)
'''

'''
# 可变集合元素的删除

# remove函数：删除指定的元素，如果该元素不存在就报错
# my_set = {1, 2, 3, 4, 5}
# my_set.remove(0)
# print(my_set)


# discard函数：与remove函数功能一致，不同的是，如果元素不存在，不会报错
# my_set.discard(0)
# print(my_set)


# pop函数：
my_set = {}
ret = my_set.pop()
print(ret)
'''

'''
# 可变集合元素的查找
my_set = {1, 2, 3, 4, 5}
# in关键字的使用：    要查找的变量 in 集合   会返回一个布尔值
if 1 in my_set:
    print("1在这个集合里")
else:
    print("1不在这个集合里")
'''



'''
# 集合的其他操作
# len函数：统计集合里元素的个数
# my_set = {1, 2, 3, 4, 5}
# print(len(my_set))

# set函数：如果不填参数，会返回一个空集合
# 需要1个参数，但是这个参数必须是一个序列
# my_set = set('abc')
# print(my_set)
# print(type(my_set))

# copy函数：复制集合的作用，浅拷贝
# my_set = {1, 2, 3, 4, 5}
# my_set1 = my_set.copy()
# print('原始的集合：', my_set)
# print('新的集合', my_set1)


# clear函数：清空集合，使集合变成一个空集合
# my_set.clear()
# print(my_set)


# 集合的关系：交集、并集、子级关系和父集关系
my_set1 = {1, 2, 3}
my_set2 = {2, 3, 4}

# 打印两个集合的交集，也可以称作两个集合的共有的部分
print('两个集合的交集为:', my_set1.intersection(my_set2))

# 打印两个集合的并集，也可以理解为将两个集合合并到一起，并去重
print('两个集合的并集为：', my_set1.union(my_set2))


s1 = {1}
s2 = {1, 2, 3}
print(s1.issubset(s2))
print(s1.issuperset(s2))

print(s2.issubset(s1))
print(s2.issuperset(s1))
'''

'''
# 集合的推导式
# 目的：创建一个含有元素1-10的集合
my_set = {x for x in range(1, 11, 1)}
print(my_set)
'''


# 不可变集合的创建
# 使用frozenset函数创建，需要填入一个参数
# 这个参数必须是一个序列
a = frozenset({1, 2, 3})
b = frozenset({1})
print(a.issuperset(b))
print(a.issubset(b))
a.add('hello')
print(a)
