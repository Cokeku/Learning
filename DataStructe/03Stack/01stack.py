# -*- coding: utf-8 -*-
# Author: Hao Zhao
"""
Python中实现的栈的方式有两种：
1. 数组结构（List）：简单但是大小事先规划和声明好
2. 链表结构：复杂但是随时可以动态改变链表长度

栈的基本运算：
1. create：创建一个空堆栈
2. push：压入栈顶
3. pop：弹出栈顶
4. is_emptry：判断是否为空
5. full：判断堆栈是否满

应用场景：
    1. 栈由操作系统自动分配释放 ，用于存放函数的参数值、局部变量等

堆和栈的区别：https://blog.csdn.net/K346K346/article/details/80849966
"""


#第一种：用列表实现堆栈
class ListStack(object):
    def __init__(self):
        self.value = []

    def push(self,value):
        self.value.append(value)

    def pop(self):
        return self.value.pop()

    def is_emptry(self):
        return self.value == []

    def is_full(self):
        pass

#第二种：用链表实现堆栈
class SingleNode(object):
    def __init__(self,value):
        self.value = self.value
        self.next = None

class LinkStack(object):
    def __init__(self):
        self.top = None

    def push(self,value):
        Node = SingleNode(value)
        Node.next = self.top
        self.top = Node

    def pop(self):
        if self.top == None:
            raise Exception("This is an empty stack")
        self.top = self.top.next

    def is_empty(self):
        return not self.top


