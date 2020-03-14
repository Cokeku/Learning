# -*- coding: utf-8 -*-
# Author: Hao Zhao


"""
循环队列：
为充分利用向量空间，克服"假上溢"现象的方法是：将向量空间想象为一个首尾相接的圆环，并称这种向量为循环向量。存储在其中的队列称为循环队列（Circular Queue）。
即：循环队列中进行出队、入队操作时，头尾指针仍要加1，朝前移动。只不过当头尾指针指向向量上界（QueueSize-1）时，其加1操作的结果是指向向量的下界0

队空条件：rear=front；
队满条件：(rear+1)%capacity=front。
    有两种情况：1.front=rear+1；
                2.front=0且rear=capacity-1。使用取余运算可以简单涵盖这两种情况；
队列长度：(rear-front+capacity)%capacity；
入队：rear=(rear+1)%capacity；
出队：front=(front+1)%capacity

应用场景：

"""

class CircleQueue(object):
    def __init__(self,capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0

    def is_emtpy(self):
        return self.rear == self.front

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self,value):
        if self.is_full():
            raise Exception("Queue is full!")
        else:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.capacity

    def dequeue(self):
        if self.is_emtpy(self):
            raise IndexError("Queue is empty!")
        else:
            tmp = self.queue(self.front)
            self.queue[self.front] = None
            self.front = (self.front + 1 ) % self.capacity
            return tmp

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        else:
            return self.queue[self.front]

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        else:
            # return self.queue[(self.rear - 1 + self.capacity) % self.capacity]
            return self.queue[self.rear]

    def print_queue(self):
        tmp = self.front
        ls = []
        while tmp != self.rear:
            ls.append(self.queue[tmp])
            tmp = (tmp + 1) % self.capacity
        return ls

if __name__ == "__main__":
    CQ = CircleQueue()

