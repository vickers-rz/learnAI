
# Exercise 1: iter + next
"""
Task / 任务：将一个 list 变成迭代器，用 next() 逐步取值，安全捕获 StopIteration。
Hint / 提示：使用 iter(...)、try/except StopIteration。
"""
list1 = [1, 2, 3, 4, 5]

list1_iterator = list1.__iter__() # 由列表产生一个迭代器
"""
print(list1_iterator.__next__())
print(list1_iterator.__next__())
print(list1_iterator.__next__())
print(list1_iterator.__next__())
print(list1_iterator.__next__())    # 最后一个元素了，如果下面再调用的话就会抛出 StopIteration 异常了。
# print(list1_iterator.__next__()) # StopIteration
"""

# while True:
#     try:
#         print(list1_iterator.__next__())
#     except StopIteration:
#         break

# 直接用 for 遍历“已生成的迭代器”
"""
for 循环会在内部自动处理 StopIteration。
所以完全可以用for循环来“读”已经创建好的 iterator（迭代器），从而避免自己写 try/except。
"""
# list1 = [6, 7, 8, 9]
# it = iter(list1)  # 生成一个 iterator
#
# for x in it:      # for 循环内部相当于不断 next(it)，自动捕获 StopIteration
#     print(x)      # 这个写法会把 it这个迭代器消耗光；之后再对同一个it再次for时将不再有输出。
#

# 最小自定义迭代器
"""
实现一个从 start 数到 end（不含）的计数器。
"""
#
# class Counter:  # 迭代器
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self  # 迭代器返回自身
#
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         value = self.current
#         self.current += 1
#         return value
#
# # print(list(Counter(3, 7)))  # [3, 4, 5, 6]
# for i in Counter(3, 7):
#     print(i)

# 课堂示例代码：

class MyRangeIterator:  # 定义一个名为MyRangeIterator的类
    def __init__(self, end):  # 构造函数，初始化迭代器
        self.end = end  # 设置迭代器的结束值
        self.num = 0  # 设置当前迭代的数值，初始为0

    def __iter__(self):  # 实现__iter__方法，返回迭代器本身
        return self  # 因为我们的迭代器就是实例本身，所以返回self

    def __next__(self):  # 实现__next__方法，返回下一个值
        if self.num < self.end:  # 如果当前数值小于结束值
            value = self.num  # 获取当前数值作为要返回的值
            self.num += 1  # 将当前数值加1，为下一次迭代做准备
            return value  # 返回当前数值
        else:  # 如果当前数值已经达到或超过结束值
            raise StopIteration  # 抛出StopIteration异常，结束迭代
     

#m1=MyRangeIterator(5)
#print(m1)
#print(type(m1))
#print(m1.__next__())




# # 使用MyRangeIterator类创建一个迭代器实例，迭代0到4的整数
# for i in MyRangeIterator(5):  # for循环会自动调用迭代器的__next__方法
#     print(i)  # 打印迭代器返回的每个值

mr=MyRangeIterator(5)       #创建对象的自动调用__init__方法进行初始化，__iter__方法返回自身
print(type(mr))
for i in mr:       #for循环自动调用迭代器 __next__方法
    print(i)


list2=[12,34,56,78]
mylist=list2.__iter__()
print(type(mylist))

# 创建一个字典，这是一个内置的可迭代对象
my_dict = {1: 'one', 2: 'two', 3: 'three'}

# 使用 iter() 函数获取字典的迭代器
dict_iter = my_dict.__iter__()
print(type(dict_iter))


# 使用迭代器的 __next__() 方法来遍历字典
# try:
#     while True:
#         # 获取下一个元素
#         item = dict_iter.__next__()
#         print(item)
# except StopIteration:
#     # 当没有更多元素时，迭代器会抛出 StopIteration 异常
#     print('Iteration is complete')

# 用for循环
# for i in dict_iter:
#     print(i)
# else:
#     print('Iteration is complete')

# 斐波那契数列的实现：

class FeiBo:  # 斐波那契的迭代器
    def __init__(self, n):
        """
        初始化斐波那契迭代器
        :param n: 要生成的斐波那契数列项数
        斐波那契数列的特点是：前两项固定为0和1，从第三项开始，每项都是前两项的和
        """
        self.n = int(n)  # 确保n是整数
        self.count = 0   # 已生成的项数
        self.a = 0       # 前一项
        self.b = 1       # 当前项

    def __iter__(self):
        return self  # 迭代器返回自身

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        
        if self.count == 0:
            self.count += 1
            return self.a
        elif self.count == 1:
            self.count += 1
            return self.b
        else:
            # 计算下一项
            next_value = self.a + self.b
            self.a, self.b = self.b, next_value
            self.count += 1
            return next_value

#
n = input("请输入数列个数：")
if n.isdigit() and int(n) > 0:
    feiBo = FeiBo(n)
    print("斐波那契数列:")
    for i in feiBo:
        print(i, end=' ')
    print()  # 换行
else:
    print("请输入一个正整数")

# 添加一个普通函数来实现类似 __next__ 的功能
def next_value(iterator_state, end_value):
    """
    模拟 __next__ 方法的普通函数
    :param iterator_state: 包含当前状态的字典，必须有 'current' 键
    :param end_value: 结束值
    :return: 下一个值或 None（表示迭代完成）
    """
    if iterator_state['current'] < end_value:
        value = iterator_state['current']
        iterator_state['current'] += 1
        return value
    else:
        return None  # 表示迭代完成

# 使用示例
print("\n使用普通函数模拟迭代器:")
state = {'current': 0}
end = 5
while True:
    val = next_value(state, end)
    if val is None:
        print("迭代完成")
        break
    print(val)
