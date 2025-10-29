class Deque:
    def __init__(self):
        self.__list = []  # 使用列表来存储队列元素

    # 判断队列是否为空
    def is_empty(self):
        return len(self.__list) == 0

    # 从队尾添加元素
    def add_front(self, item):
        self.__list.append(item)

    # 从队头添加元素
    def add_rare(self, item):
        self.__list.insert(0, item)

    # 从队尾移除元素
    def remove_front(self):
        if not self.is_empty():
            return self.__list.pop()
        else:
            raise IndexError("pop from an empty deque")

    # 从队头移除元素
    def remove_rare(self):
        if not self.is_empty():
            return self.__list.pop(0)
        else:
            raise IndexError("popleft from an empty deque")

    # 获取队列的大小
    def size(self):
        return len(self.__list)

# 示例
A = Deque()
B = Deque()

# 向队列 A 和 B 中添加元素
A.add_front(1)
A.add_front(2)
A.add_front(3)

B.add_front(4)
B.add_front(5)
B.add_front(6)

# 初始化一个新的队列 C 用于存储交替合并的结果
C = Deque()

# 开始交替合并队列 A 和 B 的过程
# 当队列 A 或队列 B 中至少有一个不为空时，继续循环
while not A.is_empty() or not B.is_empty():
    # 如果队列 A 不为空，则从队列 A 的前端移除一个元素，添加到队列 C 的后端
    if not A.is_empty():
        C.add_front(A.remove_rare())
    
    # 如果队列 B 不为空，则从队列 B 的前端移除一个元素，添加到队列 C 的后端
    if not B.is_empty():
        C.add_front(B.remove_rare())

# 循环结束后，队列 A 和 B 中的所有元素都已按交替顺序合并到队列 C 中

# 打印合并后的队列
print("合并后的队列：", C._Deque__list)  # 直接访问队列内部的列表
