class Node:
    """创建单链表节点"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self, node=None):
        # __head是私有属性
        self.__head = node

    def is_empty(self):
        # 链表是否为空
        return self.__head is None

    def length(self):
        # 链表长度
        current = self.__head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def travel(self):
        # 遍历整个链表
        current = self.__head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("")

    def add(self, data):
        # 将新节点添加到链表头部（头插法）
        # 新节点将成为链表的第一个节点
        new_node = Node(data)
        new_node.next = self.__head
        self.__head = new_node

    def append(self, data):
        # 链表尾部添加元素, 尾插法
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
        else:
            current = self.__head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert(self, pos, data):
        # 指定位置添加元素
        # pos: 要插入位置的索引（从0开始）
        if pos <= 0:
            self.add(data)
        elif pos >= self.length():
            self.append(data)
        else:
            new_node = Node(data)
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            new_node.next = pre.next
            pre.next = new_node

    def remove(self, data):
        # 删除节点
        current = self.__head
        pre = None
        while current is not None:
            if current.data == data:
                # 判断当前节点元素，与要删除的元素是否相等
                if current == self.__head:
                    self.__head = current.next
                else:
                    pre.next = current.next
                return True  # 删除成功
            else:
                pre = current
                current = current.next
        return False  # 未找到要删除的节点

    def search(self, data):
        # 查找节点是否存在
        current = self.__head
        while current is not None:
            if current.data == data:
                return True
            else:
                current = current.next
        return False

    def get(self, pos):
        # 获取指定位置的元素
        if pos < 0 or pos >= self.length():
            return None
        current = self.__head
        count = 0
        while count < pos:
            current = current.next
            count += 1
        return current.data

    def clear(self):
        # 清空链表
        self.__head = None


if __name__ == "__main__":
    linklist = LinkList()

    # 判断链表是否为空
    print("链表是否为空:", linklist.is_empty())
    # 打印链表长度
    print("链表长度:", linklist.length())

    linklist.add(10)  # 10
    linklist.add(20)  # 20,10
    linklist.add(30)  # 30,20,10
    linklist.append(100)
    linklist.append(200)  # 30,20,10,100,200

    print("当前链表:")
    linklist.travel()
    
    print("在位置2插入500:")
    linklist.insert(2, 500)  # 30,20,500,10,100,200
    linklist.travel()
    
    print("在位置-1插入123:")
    linklist.insert(-1, 123)  # 123,30,20,500,10,100,200
    linklist.travel()
    
    print("在位置20插入678:")
    linklist.insert(20, 678)  # 123,30,20,500,10,100,200,678
    linklist.travel()
    
    print("查找500:", linklist.search(500))
    print("查找666:", linklist.search(666))
    
    print("获取位置3的元素:", linklist.get(3))
    
    print("删除元素20:")
    linklist.remove(20)
    linklist.travel()