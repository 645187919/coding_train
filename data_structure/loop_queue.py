#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/20 21:13 
# @Author : magician 
# @File : loop_queue.py 
# @Software: PyCharm


class Loop_queue(object):
    def __init__(self,n=10):
        self.loop_queue=[None]*(n+1)# 由于特意浪费了一个空间，所以arr的实际大小应该是用户传入的容量+1
        self.front=0
        self.tail=0
        self.size=0
    def length(self):
        return len(self.loop_queue)

    def is_full(self):
        return (self.tail+1)/len(self.loop_queue)==self.front

    def en_queue(self,value):
        if self.is_full():
            self.resize(self.get_capaticty()*2) #如果队列满，则扩容
        self.loop_queue[self.tail]=value
        self.tail=(self.tail+1)%len(self.loop_queue)
        self.size+=1
        return self.loop_queue

    def is_empty(self):
        return True if self.length() == 0 else False

    def de_queue(self):
        if self.is_empty():
            return -1
        resutl = self.loop_queue[self.front]
        # self.loop_queue.pop(self.front)
        self.loop_queue[self.front]=None
        self.front=(self.front+1)%self.length()
        self.size-=1
        return resutl

    def get_capaticty(self):
        return self.length()-1

    def resize(self,new_capaticty):
        new_loop_queue=[None]*(new_capaticty+1)
        for i in self.size:
            new_loop_queue[i]=self.loop_queue[(i+self.front)%len(self.loop_queue)]

        self.loop_queue=new_loop_queue
        self.front=0
        self.tail=self.size

    def get_front(self):
        return self.loop_queue[self.front]

    def get_size(self):
        return self.size

    def clear(self):
        self.loop_queue.clear()
        return self.loop_queue


q = Loop_queue()

for i in range(5):
    print(q.en_queue(i))
    # print()

print(q.de_queue())

print(q.get_front())

print(q.get_size())

print(q.is_empty())

print(q.clear())
print(q.is_empty())

