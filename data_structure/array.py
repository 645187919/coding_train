#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/15 21:34
# @Author : magician
# @File : array.py
# @Software: PyCharm

class array(object):
    def __init__(self,capacity,fillvalue=None):
        self._items=list()#声明self的一个属性items,有这个属性才能做后续的操作
        for count in range(capacity):
            self._items.append(fillvalue)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, new_value):
        self._items[index]=new_value
        return self._items


if __name__ == '__main__':
    a = array(6)
    print(a.__len__())
    for i in range(len(a)):
        a[i]=i+1
    print(a)
    print(a.__getitem__(3))
    print(a.__setitem__(3,100))




