#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/26 15:55 
# @Author : magician 
# @File : linked_list_set.py 
# @Software: PyCharm


from data_structure.linked_list import Linked_list


class Linked_list_set(Linked_list):
    def __init__(self):

        self.link_list_set=Linked_list()

    def add(self,value):
        if ~self.link_list_set.contains(value):
            self.link_list_set.add_first(value)


    def get_size(self):
        return self.link_list_set.get_first()

    def is_empty(self):
        return self.link_list_set.is_empty()

    def contains(self,value):
        return self.link_list_set.contains(value)

