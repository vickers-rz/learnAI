class Node:
    """
    单链表节点类

    链表中的每个节点包含两个部分：
    1. data: 存储节点的数据（可以是任意类型）
    2. next: 指向下一个节点的指针（引用）

    示例：
    node1 = Node(100)  # 创建一个数据为100的节点
    node2 = Node(200)  # 创建一个数据为200的节点
    node1.next = node2  # 将node1指向node2，形成链式结构
    """

    def __init__(self, data):
        """
        初始化节点

        参数:
            data: 节点存储的数据
        """
        self.data = data  # 节点数据域，存储实际数据
        self.next = None  # 节点指针域，指向下一个节点，默认为None


class LinkList:
    """
    不带头节点的单链表类

    与带头节点的链表的主要区别：
    1. __head直接指向第一个数据节点，而不是指向一个空的头节点
    2. 空链表时，__head为None
    3. 对第一个节点的操作需要特殊处理，因为没有头节点作为中介
    """

    def __init__(self):
        """
        初始化链表

        与带头节点版本的主要差异：
        1. 不再接受node参数，因为不使用头节点
        2. __head直接初始化为None，表示空链表
        """
        # __head直接指向第一个数据节点，空链表时为None
        self.__head = None

    def is_empty(self):
        """
        判断链表是否为空

        返回值:
            bool: 如果链表为空返回True，否则返回False

        与带头节点版本无差异：
        - 空链表的判断仍然是self.__head == None
        """
        return self.__head == None

    def length(self):
        """
        获取链表长度（节点个数）

        返回值:
            int: 链表中节点的数量

        与带头节点版本无差异：
        - 遍历过程相同，从__head开始直到None结束
        """
        # current指针指向当前正在访问的节点，初始指向头节点
        current = self.__head
        count = 0  # 计数器初始化为0

        # 循环遍历链表直到末尾(None)
        while current != None:
            count += 1  # 每访问一个节点计数器加1
            current = current.next  # 移动到下一个节点

        return count

    def travel(self):
        """
        遍历链表并打印所有节点的数据

        实现原理：
        1. 使用current指针从头节点开始遍历
        2. 依次打印每个节点的数据
        3. 当current为None时，说明到达链表末尾，结束遍历

        与带头节点版本无差异：
        - 遍历逻辑完全相同
        """
        current = self.__head

        # 循环遍历链表直到末尾(None)
        while current != None:
            print(current.data, end=" ")  # 打印当前节点的数据，不换行
            current = current.next        # 移动到下一个节点

        print("")  # 遍历结束后换行

    def add(self, data):
        """
        在链表头部添加新节点（头插法）

        参数:
            data: 新节点的数据

        实现原理：
        1. 创建新的节点
        2. 将新节点的next指向原来的第一个节点
        3. 更新头节点指针指向新节点

        与带头节点版本无差异：
        - 操作逻辑完全相同，因为都是在链表最前端插入节点
        """
        new_node = Node(data)  # 创建新节点
        new_node.next = self.__head  # 新节点指向原来的第一个节点（或None）
        self.__head = new_node  # 头指针指向新节点

    def append(self, data):
        """
        在链表尾部添加新节点（尾插法）

        参数:
            data: 新节点的数据

        实现原理：
        1. 如果链表为空，则直接将新节点作为头节点
        2. 如果链表不为空，则找到最后一个节点，在其后面添加新节点

        与带头节点版本无差异：
        - 逻辑相同，只是没有头节点的中介
        """
        new_node = Node(data)  # 创建新节点

        # 如果链表为空，直接将新节点作为头节点
        if self.is_empty():
            self.__head = new_node
        else:
            # 链表不为空，需要找到最后一个节点
            current = self.__head
            # 当current.next为None时，current就是最后一个节点
            while current.next != None:
                current = current.next  # 移动到下一个节点

            # 将最后一个节点的next指向新节点
            current.next = new_node

    def insert(self, pos, data):
        """
        在指定位置插入新节点

        参数:
            pos: 插入位置（从0开始）
            data: 新节点的数据

        实现原理：
        1. 如果位置<=0，则在头部插入（调用add方法）
        2. 如果位置>=链表长度，则在尾部插入（调用append方法）
        3. 否则找到指定位置的前一个节点，在其后插入新节点。

        与带头节点版本的主要差异：
        1. 当pos == 0时，插入位置是第一个数据节点前，而不是头节点后
        2. 查找过程相同，但需要特别处理在位置0插入的情况
        """
        # 如果位置小于等于0，在头部插入
        if pos <= 0:
            self.add(data)
        # 如果位置超出范围，在尾部插入
        elif pos > (self.length() - 1):
            self.append(data)
        else:
            # 在中间插入
            new_node = Node(data)  # 创建新节点
            pre = self.__head  # pre首先初始化指到第一个节点
            count = 0  # 计数器

            # 找到要插入位置的前一个节点
            while count < (pos - 1):
                count += 1
                pre = pre.next

            # 修改指针完成插入操作
            new_node.next = pre.next  # 新节点继承原位置的节点的next信息
            pre.next = new_node  # 将上个节点原来的next信息更新指到新节点

    def remove(self, data):
        """
        删除第一个匹配的节点

        参数:
            data: 要删除的节点数据

        实现原理：
        1. 遍历链表找到要删除的节点
        2. 使用两个指针pre（前一个节点）和current（当前节点）
        3. 将pre节点的next改成current节点的next，以跳过要删除的节点

        与带头节点版本的主要差异：
        1. 删除第一个节点（头节点）时，需要特殊处理
        2. 不再有头节点作为中介，所以对头节点的删除需要直接修改__head指针
        """
        current = self.__head  # current指向当前节点
        pre = None  # pre指向前一个节点，初始为None

        # 遍历链表寻找要删除的节点
        while current != None:
            if current.data == data:
                # 找到了要删除的节点
                if pre == None:
                    # 要删除的是第一个节点（头节点）
                    # 直接将__head指向下一个节点
                    self.__head = current.next
                else:
                    # 要删除的是中间或尾部节点
                    pre.next = current.next
                break  # 删除完成后退出循环
            else:
                # 继续查找下一个节点
                pre = current
                current = current.next

    def search(self, data):
        """
        查找节点是否存在

        参数:
            data: 要查找的节点数据

        返回值:
            bool: 如果找到返回True，否则返回False

        与带头节点版本无差异：
        - 查找逻辑完全相同
        """
        current = self.__head  # 从头节点开始

        # 遍历链表
        while current != None:
            if current.data == data:
                return True  # 找到了
            current = current.next  # 移动到下一个节点

        return False  # 没找到


"""
详细使用示例:

# 1. 创建链表对象
link_list = LinkList()
print("链表是否为空:", link_list.is_empty())  # True

# 2. 添加元素
link_list.add(10)      # 头插法添加10: 10
link_list.add(20)      # 头插法添加20: 20 -> 10
link_list.append(30)   # 尾插法添加30: 20 -> 10 -> 30
link_list.insert(1, 50) # 在位置1插入50: 20 -> 50 -> 10 -> 30

# 3. 查看链表信息
print("链表长度:", link_list.length())  # 4
print("遍历链表:")
link_list.travel()  # 输出: 20 50 10 30

# 4. 查找元素
print("是否存在元素50:", link_list.search(50))  # True
print("是否存在元素100:", link_list.search(100))  # False

# 5. 删除元素
link_list.remove(50)   # 删除50: 20 -> 10 -> 30
print("删除50后遍历链表:")
link_list.travel()     # 输出: 20 10 30
"""

# 测试代码
if __name__ == "__main__":
    link_list = LinkList()
    print("链表是否为空:", link_list.is_empty())  # True

    # 添加元素
    link_list.add(10)      # 头插法添加10: 10
    link_list.add(20)      # 头插法添加20: 20 -> 10
    link_list.append(30)   # 尾插法添加30: 20 -> 10 -> 30
    link_list.insert(1, 50) # 在位置1插入50: 20 -> 50 -> 10 -> 30

    # 查看链表信息
    print("链表长度:", link_list.length())  # 4
    print("遍历链表:")
    link_list.travel()  # 输出: 20 50 10 30

    # 查找元素
    print("是否存在元素50:", link_list.search(50))  # True
    print("是否存在元素100:", link_list.search(100))  # False

    # 删除元素
    link_list.remove(50)   # 删除50: 20 -> 10 -> 30
    print("删除50后遍历链表:")
    link_list.travel()     # 输出: 20 10 30