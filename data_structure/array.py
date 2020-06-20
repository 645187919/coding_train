#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/15 21:34
# @Author : magician
# @File : array.py
# @Software: PyCharm
from functools import singledispatch

class array(object):
    def __init__(self,capacity,fillvalue=None):
        self._items=list()#声明self的一个属性items,有这个属性才能做后续的操作
        self.str=""

        for count in range(capacity):
            self._items.append(fillvalue)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        if index is None or index>=len(self._items):
            raise Exception("index is None or index over")
        return self._items[index]

    def __setitem__(self, index, new_value):
        self._items[index]=new_value
        return self._items

    def addlast(self,value):
        self._items.append(value)
        return self._items

    def __add__(self, index,value):
        self._items.insert(index,value)
        return self._items

    def toString(self):
        for i in range(len(self._items)):
            self.str+=str(self._items[i])
            if i !=(len(self._items)-1):
                self.str+=","
        return self.str

    def __contains__(self, item):
        for i in self._items:
            if i==item:
                return True
        return False
    def find(self,value):

        for i in range(len(self._items)):
            if self._items[i]==value:
                return i
        return -1

    def add(self,index,value):
        #先扩充一位
        self._items.append(1)

        if index is None or index>=len(self._items):
            raise IndexError("index error")

        for i in range((len(self._items)-2),0,-1):
            if i>=index:
                self._items[i+1]=self._items[i]
        self._items[index]=value
        return self._items




if __name__ == '__main__':
    a = array(6)
    print(a)
    print(a.__len__())
    for i in range(len(a)):
        a[i]=i+1
    print(a)
    print(a.__getitem__(3))
    print(a.__setitem__(3,100))
    print(a.addlast(200))
    print(a.__add__(1, 299))
    print(a.toString())
    print(a.__contains__(399))
    print(a.find(3))
    print(a.add(3,3))



