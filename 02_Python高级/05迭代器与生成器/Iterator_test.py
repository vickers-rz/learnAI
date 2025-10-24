
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

# mr=MyRangeIterator(5)       #创建对象的自动调用__init__方法进行初始化，__iter__方法返回自身
# print(type(mr))
# for i in mr:       #for循环自动调用迭代器 __next__方法
#     print(i)
#
#
# list2=[12,34,56,78]
# mylist=list2.__iter__()
# print(type(mylist))

# 创建一个字典，这是一个内置的可迭代对象
# my_dict = {1: 'one', 2: 'two', 3: 'three'}

# 使用 iter() 函数获取字典的迭代器
# dict_iter = my_dict.__iter__()
# print(type(dict_iter))


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

class FibonacciIterator:  # 创建一个名为FibonacciIterator的类
    def __init__(self,n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            value = self.a
            self.a , self.b = self.b, self.a + self.b
            self.count += 1
            return value
        else:
            raise StopIteration

feibo = FibonacciIterator(5)
for i in feibo:
    print(i)

# while True:
#     try:
#         print(feibo.__next__())
#     except StopIteration:
#         break