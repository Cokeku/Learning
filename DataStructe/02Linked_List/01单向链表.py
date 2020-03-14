# -*- coding: utf-8 -*-
# Author: Hao Zhao
"""
应用场景：

"""

class SingleNode(object):
    """单向链表节点"""
    def __init__(self,item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None

class SingleLinkList(object):
    """单向链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        # 当条件成立，头节点值为None，返回True；反之返回False
        return self.__head == None

    def addhead(self,item):
        """
        在链表头部添加元素:
        1. 创建新节点
        2. 新节点的next指向头节点
        3. 链表的头指针指向新节点
        """
        Node = SingleNode(item)
        Node.next = self.__head
        self.__head = Node

    def addtail(self,item):
        """
        在链表尾部添加元素：
        1. 创建新节点
        2. 判断链表是否为空：
            a) 链表为空：将头指针指向新节点
            b) 链表不为空：将尾部节点的next指向新节点
        """
        Node = SingleNode(item)
        if self.is_empty():
            self.__head = Node
        else:
            # 寻找尾部节点
            ptr = self.__head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = Node

    def length(self):
        """
        判断链表长度：
        1. ptr指针从头节点开始，依次向后移动
        2. 当ptr指针是否为None时，到达链表末尾
        3. 返回count值即为链表长度
        """
        ptr = self.__head
        count = 0
        while ptr != None:
            count += 1
            ptr = ptr.next
        return count

    def insert(self,item,ops):
        """
        在指定位置添加元素：
        1. 如果ops小于0 ---> self.addhead(item)
        2. 如果ops大于length()-1 ---> self.addtail(item)
        3. 声明pre指针指向pos-1位置的节点，将新节点的next指向插入节点的位置(pre.next)
        4. 将post-1位置的节点的next指向新节点
        """
        if ops <= 0:
            self.addhead(item)
        elif ops > (self.length()-1):
            self.addtail(item)
        # 找到指定位置
        else:
            Node = SingleNode(item)
            count = 0
            # 用pre来指向指定位置pos前一个位置pos-1，初始从头开始移动到指定位置
            pre = self.__head
            while count < (ops - 1):
                count += 1
                pre = pre.next
            Node.next = pre.next
            pre.next = Node

    def remove(self,itme):
        """
        删除指定元素：
        1. 找到指定元素
            a) 如果第一个就是删除的节点，将头指针指向后面一个节点(pre.next)
            b) 将前一个节点的next指向删除位置的后一个节点
        2. 找不到指定元素，返回False
        """
        ptr = self.__head
        pre = None
        while ptr != None:
            if ptr.item == itme:
                if not pre:
                    self.__head = ptr.next
                else:
                    pre.next = ptr.next
                break
            else:
                pre = ptr
                ptr = ptr.next
                while ptr == None:
                    print("Not Exsited!")
                    return False

    def exist(self,item):
        """链表查找节点是否存在，返回True或False"""
        ptr = self.__head
        while ptr != None:
            if ptr.item == item:
                return True
            ptr = ptr.next
        return False

    def travel(self):
        """遍历列表"""
        ptr = self.__head
        while ptr != None:
            # print(ptr.item)
            ptr = ptr.next

    def reserver(self):
        """
        反转单链表：
        1. 声明三个指针: ptr=head, ptr1=None , ptr2
        2. ptr向循环后节点移动：
            a) ptr2 移动到 ptr1位置
            b) ptr1 移动到 ptr位置
            c) ptr 向后移动
        3. 头指针指向最后一个节点位置 ---> ptr1
        """
        ptr = self.__head
        ptr1 = None
        while ptr != None:
            ptr2 = ptr1
            ptr1 = ptr
            ptr = ptr.next
            ptr1.next = ptr2
            # print(ptr.item,ptr1.item)
        self.__head = ptr1
        # print(self.__head)



if __name__ == '__main__':
    Linklist = SingleLinkList()
    Linklist.addhead(1)
    Linklist.addtail(3)
    Linklist.addtail(5)
    Linklist.insert(10,2)
    Linklist.travel()
    Linklist.remove(4)
    re = Linklist.exist(3)
    Linklist.reserver()
    Linklist.travel()







