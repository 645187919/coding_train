#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/14 20:04 
# @Author : magician 
# @File : queue.py 
# @Software: PyCharm


class queue(object):
    def __init__(self):
        self.data=list()
        self.size=0


    def en_queue(self,val):
        self.data.append(val)
        self.size+=1
        return self.data

    def de_queue(self):
        if self.size==0:
            raise IndexError("queue is empty")

        self.data.pop(0)
        self.size-=1
        return self.data

    def get_front(self):
        if self.size==0:
            raise IndexError("queue is empty")

        return self.data[0]

    def is_empty(self):
        return True if self.size==0 else False

    def get_size(self):
        return self.size


q = queue()
for i in range(5):
    print(q.en_queue(i))
    # print(q)
# print(q)
print(q.de_queue())

print(q.get_front())

print(q.get_size())

print(q.is_empty())
# print(q.clear())
# print(q.is_empty())


