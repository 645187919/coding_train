#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/20 14:55 
# @Author : magician 
# @File : stack.py 
# @Software: PyCharm


class Stack(object):
    def __init__(self):
        self._stack=[]


    def push(self,value):
        self._stack.append(value)
        return self._stack

    def pop(self):
        self._stack.pop(-1)
        return self._stack

    def is_empty(self):
        return True if len(self._stack)==0 else False

    def peek(self):
        # peek_value = self._stack[-1]
        return  self._stack[-1]
    def get_size(self):
        return len(self._stack)

    def to_string(self):
        tmp_str="["

        for i,v in enumerate(self._stack):
            #实现方法1
            # if i==len(self._stack)-1:
            #     tmp_str+=str(v)
            # else:
            #     cell=str(v)+","
            #     tmp_str+=cell
            #实现方法二
            tmp_str+=str(v)
            if i!=len(self._stack)-1:
                tmp_str+=","
        tmp_str+="]"
        return tmp_str


s = Stack()
# print(s)
# print(type(s))
for i in range(6):
    print(s.push(i))

print(s.push(1))
print(s.push(2))
print(s.to_string())
print(type(s.to_string()))
# print(s.push(2))
print(s.pop())
print(s.peek())
print(s.pop())
print(s.is_empty())
print(s.get_size())
# for i in range(6):
#     s.ap


