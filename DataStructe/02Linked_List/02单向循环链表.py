# -*- coding: utf-8 -*-
# Author: Hao Zhao

"""
应用场景：

"""

class SingleNode(object):
    """单向循环链表节点"""
    def __init__(self,item):
        self.item = item
        self.next = None

class CircularLinklist(object):
    """单向循环链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def add(self,item):
        """
        1. 创建新节点
        2. 判断链表是否为空
            a) 链表为空：(头指针和头节点的next必须都指向头节点)
                头指针指向新节点 --->  self.__head = Node
                新节点的next指向头节点 --->  Node.next = self.__head

            b) 链表不为空：
                新节点的next指向头节点 ---> Node.next = self.__head
                尾节点的next指向头节点 ---> ptr.next = Node
                头指针指向新节点 ---> self.__head = Node
        """
        Node = SingleNode(item)
        if self.is_empty():
            self.__head = Node
            Node.next = self.__head

        else:
            Node.next = self.__head
            # 向链表尾部移动ptr指针
            ptr = self.__head
            while ptr.next != self.__head:
                ptr = ptr.next
            ptr.next = Node
            self.__head = Node

    def append(self,item):
        """
        1. 创建新节点
        2. 判断链表是否为空
            a) 链表尾空：
                新节点的next指向头节点 --->  Node.next = self.__head
                头指针指向新节点 --->  self.__head = Node
            b) 链表不为空：
                新节点的next指向指向头节点 ---> Node.next = self.__head
                尾节点的next指向新节点 ---> ptr.next = Node
        """

        Node = SingleNode(item)
        if self.is_empty():
            Node.next = self.__head
            self.__head = Node
        else:
            Node.next = self.__head
            # 向链表尾部移动ptr指针
            ptr = self.__head
            while ptr.next !=  self.__head:
                ptr = ptr.next
            ptr.next = Node

    def length(self):
        """返回链表长度"""
        if self.is_empty():
            return 0
        ptr = self.__head
        count = 1
        while ptr.next != self.__head:
            count += 1
            ptr = ptr.next
        return count

    def insert(self,pos,item):
        """
        在链表指定pos位置插入元素：
        1. 判断pos位置：
            a) pos <= 0 ---> self.add(item)
            b) pos > length() -1 ---> self.append(item)
        2. 创建新节点
        3. 找到指定pos位置，将新节点的next指向pos位置的后一个节点
        4. 将pos位置的next指向新节点
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            Node = SingleNode(item)
            # 移动ptr指针到指定位置
            ptr = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                ptr = ptr.next
            Node.next = ptr.next
            ptr.next = Node
    def is_exit(self,item):
        """
        判断某个元素是否在链表中：
        1. ptr指针指向头节点
        2. ptr指针向后移动，当ptr.item等于item时，返回True，否则返回False
        """
        ptr = self.__head
        while ptr.next != self.__head:
            if ptr.item == item:
                return True
            else:
                ptr = ptr.next
        if ptr.item == item:
            return True
        else:
            print("%d不再链表中！"%item)
            return False

    def remove(self,item):
        """
        删除链表中某个元素:
        1. 若链表为空或删除元素不在链表中直接返回Fasle
        2. 若删除的元素为头节点（并且不是最后一个节点）：
            a) 将末节点的next指向头节点的后个节点
            b) 将头指针指向头节点的后个节点
        3. 通过ptr找到删除元素，将pre指针的next指向ptr指针的next ---> pre.next = ptr.next（注意尾节点）
        """
        ptr = self.__head
        if self.is_empty():
            return False
        elif not self.is_exit(item):
            return False
        # 头部删除
        elif ptr.item == item:
            # 不仅仅有1个节点
            if ptr.next != self.__head:
                # 找到尾节点
                while ptr.next != self.__head:
                    ptr = ptr.next
                # 将尾节点的next指向头节点的后个节点
                ptr.next = self.__head.next
                # 将头指针指向头节点的后个节点
                self.__head = self.__head.next
            # 只有头节点
            else:
                self.__head = None
        else:
            pre = self.__head
            while ptr.next != self.__head:
                if ptr.item == item:
                    pre.next = ptr.next
                    return
                else:
                    pre = ptr
                    ptr = ptr.next
            # 尾部删除
            if ptr.item == item:
                pre.next = ptr.next

    def travel(self):
        """遍历单向循环链表"""
        if self.is_empty():
            return None
        ptr = self.__head
        # 打印头节点的item
        print(self.__head.item)
        # 打印链表中节点的item
        while ptr.next != self.__head:
            ptr = ptr.next
            print(ptr.item)

if __name__ == "__main__":
        CLL = CircularLinklist()
        CLL.add(10)
        CLL.add(0)
        CLL.append(20)
        CLL.insert(2,15)
        CLL.travel()
        result = CLL.length()
        print("链表长度为：%d"%result)
        re = CLL.is_exit(20)
        print(re)
        CLL.remove(30)
        CLL.travel()
        CLL.remove(20)
        CLL.travel()