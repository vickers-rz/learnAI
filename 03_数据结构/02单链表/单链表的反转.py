# 单链表的反转,通过两种方法（迭代和递归）来完成

class Node:
    """
    单链表节点类
    """
    def __init__(self, data):
        """
        初始化节点
        参数:
            data: 节点存储的数据
        """
        self.data = data
        self.next = None


class LinkList:
    """
    单链表类
    """
    def __init__(self):
        """
        初始化链表
        """
        self.__head = None

    def is_empty(self):
        """
        判断链表是否为空
        返回:
            True: 链表为空
            False: 链表不为空
        """
        return self.__head == None

    def length(self):
        """
        获取链表长度
        返回:
            count: 链表中节点的个数
        """
        current = self.__head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def travel(self):
        """
        遍历整个链表并打印节点数据
        """
        current = self.__head
        while current != None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def add(self, data):
        """
        在链表头部添加元素（头插法）
        参数:
            data: 要添加的数据
        """
        new_node = Node(data)
        new_node.next = self.__head
        self.__head = new_node

    def append(self, data):
        """
        在链表尾部添加元素（尾插法）
        参数:
            data: 要添加的数据
        """
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
        else:
            current = self.__head
            while current.next != None:
                current = current.next
            current.next = new_node

    def reverse_iteration(self):
        """
        使用迭代方法反转链表（推荐初学者理解）
        
        原理：
        假设链表为: 1 -> 2 -> 3 -> None
        反转后为: 3 -> 2 -> 1 -> None
        
        步骤：
        1. 定义三个指针：prev(前一个节点)、current(当前节点)、next_node(下一个节点)
        2. 初始化：prev = None, current = self.__head
        3. 循环处理：
           - 保存current的下一个节点到next_node
           - 将current的next指针指向前一个节点prev
           - prev和current都向前移动一步
        4. 循环结束后，prev就是新的头节点
        """
        # 如果链表为空或只有一个节点，直接返回
        if self.__head == None or self.__head.next == None:
            return
        
        # 初始化三个指针
        prev = None              # 前一个节点，初始为None
        current = self.__head    # 当前节点，初始为头节点
        next_node = None         # 下一个节点，初始为None
        
        # 开始迭代反转
        while current != None:
            # 保存下一个节点，防止断链
            next_node = current.next
            
            # 反转当前节点的指针方向
            current.next = prev
            
            # 移动指针到下一个位置
            prev = current       # prev向前移动
            current = next_node  # current向前移动
        
        # 反转完成后，prev成为新的头节点
        self.__head = prev

    def reverse_recursion(self, node=None):
        """
        使用递归方法反转链表（供进阶学习）
        
        原理：
        递归思路是将问题分解为更小的子问题
        1. 基础情况：如果节点为空或只有一个节点，直接返回该节点
        2. 递归情况：反转以当前节点下一个节点为头的子链表
        3. 调整指针：将当前节点的下一个节点的next指针指向当前节点
        4. 将当前节点的next指针设为None
        
        参数:
            node: 当前处理的节点，如果为None则从头节点开始
        返回:
            反转后链表的头节点
        """
        # 如果是第一次调用，从头节点开始
        if node == None:
            node = self.__head
        
        # 基础情况：如果节点为空或只有一个节点
        if node == None or node.next == None:
            # 更新头节点
            self.__head = node
            return node
        
        # 递归反转以node.next为头的子链表
        new_head = self.reverse_recursion(node.next)
        
        # 调整指针方向
        node.next.next = node   # 将下一个节点的next指向当前节点
        node.next = None        # 将当前节点的next设为None
        
        return new_head

    def reverse(self):
        """
        反转链表的公共接口，默认使用迭代方法
        """
        self.reverse_iteration()


# 测试和演示代码 ，
"""
将测试和演示代码放在 if __name__ == "__main__" 下是Python的最佳实践。
既保证了代码的可测试性，又确保了模块的可重用性。
"""
if __name__ == "__main__":
    print("=== 单链表反转教学演示 ===\n")
    
    # 创建链表并添加测试数据
    print("1. 创建链表并添加元素:")
    ll = LinkList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    print("原始链表: ", end="")
    ll.travel()
    print(f"链表长度: {ll.length()}\n")
    
    # 使用迭代方法反转链表
    print("2. 使用迭代方法反转链表:")
    ll.reverse_iteration()
    print("反转后链表: ", end="")
    ll.travel()
    print()
    
    # 再次反转，恢复原始状态
    print("3. 再次反转，恢复原始状态:")
    ll.reverse_iteration()
    print("恢复后链表: ", end="")
    ll.travel()
    print()
    
    # 使用递归方法反转链表
    print("4. 使用递归方法反转链表:")
    ll.reverse_recursion()
    print("递归反转后: ", end="")
    ll.travel()
    print()
    
    # 演示空链表和单节点链表的反转
    print("5. 特殊情况测试:")
    
    # 空链表
    empty_list = LinkList()
    print("空链表反转前: ", end="")
    empty_list.travel()
    empty_list.reverse_iteration()
    print("空链表反转后: ", end="")
    empty_list.travel()
    
    # 单节点链表
    single_list = LinkList()
    single_list.append(42)
    print("单节点链表反转前: ", end="")
    single_list.travel()
    single_list.reverse_iteration()
    print("单节点链表反转后: ", end="")
    single_list.travel()