# -*- coding: utf-8 -*-
# Author: Hao Zhao

"""
应用场景：

"""

class SingleNode(object):
    def __init__(self,item):
        self.item = item
        self.right = None
        self.left = None

class DoubleLinkList(object):
    def __init__(self):
        self.__head = None


    def is_empty(self):
        return self.__head == None

    def add(self,item):
        """
        在链表头部添加头节点：
        """
        Node = SingleNode(item)
        if self.is_empty():
            self.__head = Node
        else:
            # 将Node的后继区指向原头节点
            Node.right = self.__head
            # 将原头节点的前继区指向Node
            self.__head.left = Node
            # 将头指针指向新的头节点
            self.__head = Node

    def append(self,item):
        """在链表尾部添加尾节点"""
        Node = SingleNode(item)
        ptr = self.__head
        if self.is_empty():
            self.__head = Node
        else:
            # 将ptr指向尾节点
            while ptr.right:
                ptr = ptr.right
            # 将尾节点的后继区指向新节点
            ptr.right = Node
            # 将新节点的前继区指向原尾节点
            Node.left = ptr

    def length(self):
        """判断链表长度"""
        ptr = self.__head
        count = 0
        while ptr:
            ptr = ptr.right
            count += 1
        return count

    def travel(self):
        """遍历链表"""
        ptr = self.__head
        while ptr:
            print(ptr.item)
            ptr = ptr.right

    def insert(self,pos,item):
        """插入新节点"""
        if pos < 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            Node = SingleNode(item)
            ptr = self.__head
            count = 0
            # 找到新节点的pos位置
            while count < pos:
                count += 1
                ptr = ptr.right
            # 此时ptr指向pos位置的原节点
            # 先去指定新节点的前后继区
            Node.right = ptr
            Node.left = ptr.left
            # 将ptr的前继区的后继区指向新节点
            ptr.left.right = Node
            # 将ptr的前继区指向新节点
            ptr.left = Node
    def search(self,value):
        """查询链表中的节点"""
        ptr = self.__head
        while ptr:
            if ptr.item == value:
                return True
            else:
                ptr = ptr.right
        return None

    def remove(self,value):
        if self.is_empty():
            return None
        if not self.search(value):
            return None
        ptr = self.__head
        while ptr:
            if ptr.item == value:
                 # value为头节点
                if ptr == self.__head:
                    self.__head = self.__head.right
                    self.__head.left = None
                    return True
                else:
                    # value为尾节点
                    if ptr.right == None:
                        ptr.left.right = None
                        return True

                    # value为中间节点
                    else:
                        ptr.left.right = ptr.right
                        ptr.right.left = ptr.left
                        return True
            else:
                ptr = ptr.right


if __name__ == "__main__":
    DLL = DoubleLinkList()
    DLL.add(1)
    DLL.append(20)
    DLL.insert(1,10)
    DLL.insert(-1,0)
    DLL.insert(4,30)
    DLL.travel()
    re_le = DLL.length()
    print(re_le)
    re_re = DLL.search(30)
    print(re_re)
    DLL.remove(0)
    DLL.remove(30)
    DLL.remove(10)
    DLL.travel()




