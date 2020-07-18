#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/20 17:20 
# @Author : magician 
# @File : queue.py 
# @Software: PyCharm


class Queue(object):
    def __init__(self):
        """
        队列
        """
        self.queue=[]

    def en_queue(self,value):
        #append方法不返会object，所以return  self.queue.append(value)的时候，打印出来的是None

        self.queue.append(value)
        return self.queue

    def de_queue(self):
        try:
            self.queue.pop(0)
        except IndexError as e:
            print("index error")
        return self.queue

    def get_front(self):
        try:
            front_value=self.queue[0]
        except IndexError as e:
            print("index error")
        return front_value
    def get_size(self):
        return len(self.queue)

    def is_impty(self):
        return True if len(self.queue)==0 else False

    def clear(self):
        return self.queue.clear()

q = Queue()
for i in range(5):
    print(q.en_queue(i))
    # print(q)
# print(q)
print(q.de_queue())

print(q.get_front())

print(q.get_size())

print(q.is_impty())
print(q.clear())
print(q.is_impty())

