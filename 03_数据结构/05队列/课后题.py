
"""
要求在Queue类中实现一个方法，该方法将两个队列的元素按顺序合并成一个新的队列。
例如，队列A中的元素是[1,2,3]，队列B中的元素是[4,5,6]，合并后的新队列应为[1,2,3,4,5,6]。

可能的实现思路：
	使用两个队列的元素，依次入队到新队列中：可以使用enqueue()方法将元素从队列A和队列B依次加入到新队列中。
	遍历队列A和队列B，将它们的元素按照顺序逐个添加到新队列中。

具体实现步骤：
	定义一个新的队列。
	从队列A中取出每个元素并将其加入新队列。
	从队列B中取出每个元素并将其加入新队列。
"""

# 通过在类里添加__iter__ 迭代的方法的实现
"""
from traceback import print_exc


class Queue:
    def __init__(self):
        self.__list = []

    def enqueue(self, data):
        self.__list.append(data)

    def dequeue(self):
        return self.__list.pop(0)

    def size(self):
        return len(self.__list)

    def is_empty(self):
        return self.__list == []

    # 实现 __iter__ 方法使队列可迭代
    def __iter__(self):
        return iter(self.__list)

'''
以下__iter__ 方法的实现比较特别，
它通过 dequeue 方法逐个从队列中取出元素并 yield 出去。
每次迭代都会从队列中移除一个元素，这意味着这个队列一旦被迭代过一次，就会变为空队列。
因此，迭代后的队列是被“消费”掉的，元素不再保留。
'''
    # def __iter__(self):
    #     while not self.is_empty():
    #         yield self.dequeue()

if __name__ == "__main__":
    queueA = Queue()
    queueA.enqueue(1)
    queueA.enqueue(2)
    queueA.enqueue(3)

    for A in queueA:
        print(A)

    queueB = Queue()
    queueB.enqueue(4)
    queueB.enqueue(5)
    queueB.enqueue(6)

    for B in queueB:
        print(B)

    '''
    将队列queueA和queueB直接作为元素入队new_queue时，
    这样做并不会按预期将队列的元素合并，
    而是将整个队列对象作为单个元素加入。
    '''
    # new_queue = Queue()
    # new_queue.enqueue(queueA)
    # new_queue.enqueue(queueB)


    new_queue = Queue()

    # 将当前队列的元素加入新队列
    for item in queueA:
        new_queue.enqueue(item)

    # 将另一个队列的元素加入新队列
    for item in queueB:
        new_queue.enqueue(item)

    for new in new_queue:
        print(new)
"""

'''
以下两种方法不是迭代方法。
首先创建一个新的 Queue 对象用于存储合并后的元素。
然后，通过循环依次将第一个队列中的元素出队并添加到新队列中，直到第一个队列为空。
接着，再通过循环将第二个队列中的元素出队并添加到新队列中，直到第二个队列为空。
这样就实现了两个队列元素按照顺序合并到新队列中。
'''
# 1. 扩展写法
"""
from queue import Queue

queue1 = Queue()
queue2 = Queue()
merged_queue = Queue()

# 示例数据
for item in [1, 2, 3]:
    queue1.put(item)
for item in ['a', 'b', 'c']:
    queue2.put(item)

while not queue1.empty():
    merged_queue.put(queue1.get())

while not queue2.empty():
    merged_queue.put(queue2.get())

while not merged_queue.empty():
    print(merged_queue.get())

"""
# 2. 普通写法

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0



if __name__ == "__main__":
    queue1 = Queue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)

    queue2 = Queue()
    queue2.enqueue(4)
    queue2.enqueue(5)
    queue2.enqueue(6)

    merged_queue = Queue()
    while not queue1.is_empty():
        merged_queue.enqueue(queue1.dequeue())

    while not queue2.is_empty():
        merged_queue.enqueue(queue2.dequeue())

    while not merged_queue.is_empty():
        print(merged_queue.dequeue())


