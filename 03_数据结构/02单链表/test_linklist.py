#!/usr/bin/env python3

from LinkList import *

def main():
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

if __name__ == '__main__':
    main()