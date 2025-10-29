# 双端队列
class Deque:
    """双端队列"""

    def __init__(self):
        self.__list = []

    def add_front(self, data):
        # 从队列头加入一个元素
        self.__list.insert(0, data)

    def add_rear(self, data):
        # 从队列尾加入一个元素
        self.__list.append(data)

    def remove_front(self):
        #从队列头删除一个元素,还要## 返回删除的元素
        """
        return 千万不能忘记写
        """
        return self.__list.pop(0)

    def remove_rear(self):
        # 从队列尾删除一个元素,并返回删除的元素
        return self.__list.pop()

    def size(self):
        # 返回队列的大小
        return len(self.__list)

    def is_empty(self):
        # 判断队列是否为空
        return self.__list == []


if __name__ == "__main__":
    deque = Deque()
    deque.add_front(4)
    deque.add_front(3)
    deque.add_rear(2)

    # 以下方法均有返回值，故可打印输出
    print(deque.remove_front())
    print(deque.size())
    print(deque.remove_rear())
    print(deque.remove_front())
    print(deque.size())
    # deque.remove_front() # 已经删光了会报IndexError: pop from empty list
    print(deque.is_empty())