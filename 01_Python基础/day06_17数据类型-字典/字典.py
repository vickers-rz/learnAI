
'''
# 字典的定义
# 格式：  名字 = {键1:值1，键2:值2}
# my_dict = {1: 1, 'zhangsan': 18, (1, 2, 3): [1, 2, 3]}
# print(my_dict)

# dict.fromkeys(iterable, value)
# 作用：在创建字典的时候，能一次性创建多个键值对
# 有两个参数:
# iterable:序列，里面存放着键值对的键，注意里面的元素必须要是数字、字符串以及元组中的任意一种(也就是要符合字典对“键”的数据类型要求)
# value:默认为None
# my_dict = dict.fromkeys([1, 'abc', (1, 2, 3)])
# print(my_dict)
'''


'''
# 字典的访问
my_dict = dict.fromkeys(['key1', 'key2', 'key3'])
print(my_dict)
print(my_dict['key4'])
'''

'''
# 键值对的添加
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# 直接添加
# 格式： 字典名字[新的键名] = 新的值
my_dict['key4'] = 'value4'
print(my_dict)


# update:合并两个字典
my_dict1 = {1: 1, 2: 2}
my_dict.update(my_dict1)
print(my_dict)
'''

'''
# 键值对的删除
# pop函数：删除一个指定的键和其对应的值，且该值可以被接收
# 如果指定的键不存在，就会报错
# my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# ret = my_dict.pop('key4')
# print(my_dict)
# print(ret)


# clear函数：
# my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# my_dict.clear()
# print(my_dict)

# popitem():不需要参数，随机弹出一个键值对，在Python3.7版本之后
# 用来弹出最后一个添加的键值对
# 弹出的键值对可以被接收，并且会转换成一个元组，其中键是第一个元素，值是第二个元素
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
ret = my_dict.popitem()
print(my_dict)
print(ret)
print(type(ret))

# del关键字:如果不指定要删除的键值对的话，就会删除掉整个字典，包括字典对象
# 相当于字典没有定义
# 如果指定要删除的键值对，就会删除掉该键值对
del my_dict['key1']
print(my_dict)
'''


'''
# 键值对的修改
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# 修改单个键值对，直接修改
# 格式为： 变量名[要修改的键名] = 新的值
my_dict['key1'] = 1
print(my_dict)


# 修改多个键值对，使用update函数
# update函数：用来修改多个键值对
# 格式为：  update({要修改的键值对})
my_dict.update({'key2': 2, 'key3': 3})
print(my_dict)
'''


'''
# 键值对的查找
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# 使用直接查找的方式
# print(my_dict['key4'])

# 使用get函数
# get函数：可以指定当键不存在时的提示词，如果不指定，就会返回None
print(my_dict.get('key5'))

# 使用in关键字查询字典里是否有某键值对
if 'key1' in my_dict:
    print(my_dict['key1'])


# 使用setdefault函数
# setdefalut函数：查询指定的键值对，如果不存在该键值对，就创建该键值对
# 需要两个参数，第一个是要查询的键，第二个是键不存在时创建键值对时键所对应的值
my_dict.setdefault('key4', 1)
print(my_dict)
'''



# 字典的其他操作
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# len函数：获取键值对的个数
print(len(my_dict))

# copy函数：对字典的浅拷贝
my_dict1 = my_dict.copy()
print(my_dict1)

# keys:返回字典中所有的键值对的键
print(my_dict.keys())

# values:返回字典中所有的键值对的值
print(my_dict.values())

# items:返回字典中所有的键值对
print(my_dict.items())



"""
# 字典推导式
# 要求：创建一个以1-10为键的字典，且值是键的平方
my_dict = {x: x * x for x in range(1, 11, 1)}
print(my_dict)
"""
