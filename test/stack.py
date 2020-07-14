#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/14 19:55 
# @Author : magician 
# @File : stack.py 
# @Software: PyCharm



class stack(object):
    def __init__(self):
        self.data=list()
        self.size=0

    def push(self,val):

        self.data.append(val)
        self.size+=1
        return self.data

    def pop(self):
        if self.size==0:
            raise IndexError("stack is empty")

        self.data.pop(-1)
        self.size-=1
        return self.data

    def peek(self):
        if self.size==0:
             raise IndexError("stack is empty")

        return self.data[-1]

    def get_size(self):
        return self.size

    def is_empty(self):
        return True if self.size==0 else False

#FILO
s = stack()
# print(s)
# print(type(s))
for i in range(6):
    print(s.push(i))

print(s.push(1))
print(s.push(2))

# print(s.push(2))
print(s.pop())
print(s.peek())
print(s.pop())
print(s.is_empty())
print(s.get_size())