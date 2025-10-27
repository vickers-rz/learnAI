class Node:
    """单链表节点类"""
    
    def __init__(self, data):
        self.data = data  # 节点存储的数据
        self.next = None  # 指向下一个节点的指针


class SingleLinkedList:
    """单链表类"""
    
    def __init__(self):
        """初始化单链表"""
        self.head = None  # 头节点
    
    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None
    
    def length(self):
        """返回链表的长度"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def travel(self):
        """遍历链表并打印所有元素"""
        if self.is_empty():
            print("链表为空")
            return
        
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def add(self, data):
        """在链表头部添加节点"""
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def append(self, data):
        """在链表尾部添加节点"""
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    
    def insert(self, pos, data):
        """在指定位置插入节点"""
        if pos <= 0:
            self.add(data)
        elif pos >= self.length():
            self.append(data)
        else:
            node = Node(data)
            current = self.head
            count = 0
            # 找到要插入位置的前一个节点
            while count < pos - 1:
                current = current.next
                count += 1
            node.next = current.next
            current.next = node
    
    def remove(self, data):
        """删除第一个匹配的节点"""
        current = self.head
        prev = None
        
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False
    
    def search(self, data):
        """查找节点是否存在"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


# 测试单链表功能
if __name__ == "__main__":
    # 创建单链表实例
    sll = SingleLinkedList()
    
    # 测试是否为空
    print("链表是否为空:", sll.is_empty())
    
    # 添加元素
    sll.add(1)
    sll.add(2)
    sll.append(3)
    sll.append(4)
    
    print("当前链表内容:")
    sll.travel()
    
    print("链表长度:", sll.length())
    
    # 插入元素
    sll.insert(2, 5)
    print("在位置2插入5后:")
    sll.travel()
    
    # 查找元素
    print("查找元素3:", sll.search(3))
    print("查找元素6:", sll.search(6))
    
    # 删除元素
    sll.remove(2)
    print("删除元素2后:")
    sll.travel()