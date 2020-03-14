# -*- coding: utf-8 -*-
# Author: Hao Zhao

"""
队列(Queue)也是一种运算受限的线性表。它只允许在表的一端进行插入，而在另一端进行删除。允许删除的一端称为队头(front)，允许插入的一端称为队尾(rear)。先进先出(FIFO)

应用场景：

"""

class Queue(object):
    def __init__(self,maxsize):
        self.queue = []
        self.maxsize = maxsize

    def is_emptry(self):
        return len(self.queue) == 0

    def is_full(self):
        # maxsize <= 0 意味着队列没有大小限制
        if self.maxsize <= 0:
            return False
        else:
            return len(self.queue) == self.maxsize

    def enqueue(self,value):
        if self.is_full():
            raise Exception("Queue is full!")
        else:
            self.queue.append(value)

    def dequeue(self):
        if self.is_emptry():
            raise IndexError("Queue is emtpy!")
        else:
            self.queue.pop()

    def get_front(self):
        if self.is_emptry():
            raise IndexError("Queue is emtpy!")
        else:
            return self.queue[0]

    def get_rear(self):
        if self.is_emptry():
            raise IndexError("Queue is emtpy!")
        else:
            return self.queue[-1]

    def size(self):
        return len(self.queue)

    def print_queue(self):
        return self.queue

if __name__ == "__main__":
    Q = Queue()