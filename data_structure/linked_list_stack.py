#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/21 21:34 
# @Author : magician 
# @File : linked_list_stack.py 
# @Software: PyCharm

from data_structure.linked_list import Linked_list
class Linked_list_stack(Linked_list):

    def __init__(self):
        self.list=Linked_list()

    def push(self,value):
        self.list.add_first(value)


    def pop(self):
        return self.list.remove_first()

    def peak(self):
        return self.list.get_first()


if __name__ == '__main__':
    ls = Linked_list_stack()
    print(ls.push(1))
    print(ls.push(2))
    print(ls.peak())
    print(ls.pop())
    print(ls.peak())


