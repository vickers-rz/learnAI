class Queue:
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        self.__list.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.__list.pop(0)

    def is_empty(self):
        return len(self.__list) == 0

    def size(self):
        return len(self.__list)
    
    # 实现 __iter__ 方法使队列可迭代
    def __iter__(self):
        return iter(self.__list)

# 示例使用
queueA = Queue()
queueA.enqueue(1)
queueA.enqueue(2)
queueA.enqueue(3)

# 现在可以遍历队列了
for item in queueA:
    print(item)  # 输出：1 2 3
