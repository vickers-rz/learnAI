#定义一个节点的类
class Node:
    def __init__(self, data):
        self.data = data   #数据域
        self.next = None   #指针域


#定义一个链表类
class LinkedList:
    def __init__(self,node=None):
        self.__head = node

    #判断该链表是否为空链表
    def is_empty(self):
        return self.__head==None

    #判断该链表的元素个数
    #插入:
    #<1>.头插法
    def add(self,data):
        #<1>.创建新节点
        newnode=Node(data)
        #<2>.使用头插法
        #<2.1>.保护好头节点后的所有
        newnode.next = self.__head
        #<2.2>.更新头节点
        self.__head = newnode

    #<2>.尾插法
    def append(self,data):
        #<1>.创建新节点
        newnode=Node(data)
        #<1---1>.特殊处理，如果是空链表，直接将newnode赋值给self.__head
        if self.is_empty():
            self.__head = newnode

        #<2>.找到尾结点:next==None
        cur=self.__head
        while cur.next!=None:
            cur=cur.next

        #<3>.将新节点插入到尾结点之后
        cur.next=newnode
    #<3>.在任意位置插入    pos>length-1:尾插法  pos<0:头插法  else:在中间插入

    #链表的遍历
    def travel(self):
        #<1>.定义一个临时变量初始化第一个节点
        cur=self.__head
        #<2>.在cur!=None的情况下,输出数据域,循环移动cur
        while cur!=None:
            print(cur.data," ")
            cur=cur.next  #移动到下一个结点的指针
        print()

if __name__ == '__main__':
    linked_list=LinkedList()
    linked_list.add(10)  #头插法
    linked_list.add(20)
    linked_list.add(30)
    linked_list.add(40)
    linked_list.travel()